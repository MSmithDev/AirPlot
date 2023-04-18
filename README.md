# AirPlot

This tool is designed to read raw sensor data from an Nreal Air as well as the Fusion pose in euler angles. There is also an optional reference input which is currently setupt to read NMEA packets from a Redshift UM7 AHRS to compare.


## Requirements

```
Python 3.10+
Numpy
Pyqt5
Pyqtgraph
pyserial (optional if using reference input)
```

## Options
If you are not using a reference IMU change this to false
```python
##Use Reference IMU?
useRefImu = True
```
If you are using a different reference IMU you can modify the def returns to suit your needs.
```python
## Air data will be drawn grey
def getGyroX():
    return rawGyroReading[0]

## Reference data will be drawn red
def getRefGyroX():
    return ref_gyro.x
```
