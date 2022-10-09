import os
import glob
import time
import serial

class Sensor():
    def __init__(self) -> None:
        '''Constructor for Overall Sensor Class'''
        pass

    def get_measurement_raw(self):
        pass

    def get_measurement(self):
        '''Use in While for continuous readings with sleep(Less than 1 second)'''
        pass

class PHSensor(Sensor):
    def __init__(self) -> None:
        super(self)
        self.port = serial.Serial("/dev/ttyAMA0",baudrate=9600, timeout=1.0)
        pass

    def get_measurement_raw(self):
        pass

    def get_measurement(self):
        counter = 10
        for i in range(counter):
            rcv = self.port.readLine()
            if len(rcv) > 4:
                stuck = True
                break
        else:
            counter += 1
        while stuck:
            measurement = rcv.split(',')
            stuck = False
            return float(measurement[0].split(':'))
class TempSensor(Sensor):
    def __init__(self) -> None:
        super(self)
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-term')
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir+'28*')[0]
        self.device_file = device_folder + '/w1_slave'
        return

    def get_measurement_raw(self):
      with open(self.device_file, 'r') as file:
        lines = file.readlines()
        return lines
    
    def get_measurement(self):
        lines = self.get_measurement_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.get_measurement_raw()
        equal_position = lines[1].find('t=')
        if equal_position != -1:
            temp_string = lines[1][equal_position+2:]
            temp_celsius = float(temp_string)/1000.0
            temp_fahrenheit = temp_celsius*9.0/5.0+32.0
            return temp_celsius, temp_fahrenheit