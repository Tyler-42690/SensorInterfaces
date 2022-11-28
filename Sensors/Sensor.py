import os
import glob
import time
import serial
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


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

class ConductivitySensor(Sensor):
    def __init__(self):
        # Create the I2C bus
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Create the ADC object using the I2C bus
        self.ads = ADS.ADS1115(self.i2c)

        # Create single-ended input on channel 0
        self.chan = AnalogIn(self.ads, ADS.P1)


        # Create differential input between channel 0 and 1
        #chan = AnalogIn(ads, ADS.P0, ADS.P1)

    def get_measurement_raw(self):
        return super().get_measurement_raw()
    
    def get_measurement(self):
        print("{:>5}\t{:>5}".format('raw', 'v'))

        while True:
            voltage = self.chan.voltage
            tdsValue=(477.79*self.chan.voltage-2.53)
            print(tdsValue)
            time.sleep(0.5)