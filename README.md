# SensorInterfaces

Note that these two configurations are used:

PH: https://www.pantechsolutions.net/water-quality-measurement-using-ph-sensor-with-raspberry-pi

Temp: https://pimylifeup.com/raspberry-pi-temperature-sensor/

Documentation:

Camera.py : 
  take_picture() => There are no inputs to the function. Calling this takes a picture from a live video feed.
  
Sensor.py : (Note PHSensor and TempSensor ARE under the same class Sensor and thus share the same behavior)

  get_measurement_raw() => There are no inputs to the function. Calling this takes the measurement recorded by the sensor "instantly" (Python is slow)
  
  get_measurement() => There are no inputs to the function. Calling this takes the measurements recorded by the sensor indefinitely(As long as we allow, it will continue to run)
