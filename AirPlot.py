from time import perf_counter
import ctypes
import numpy as np
import pyqtgraph as pg

#### Configure Refernece IMU ####
import threading
import serial

# Open serial port on COM4 at a baud rate of 115200
ser = serial.Serial('COM4', 115200)

# Create a class to store sensor data
class SensorData:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

# Create instances of SensorData class
ref_gyro = SensorData()
ref_accel = SensorData()
ref_mag = SensorData()

# Define a function to read and process the serial data in a separate thread
def read_serial_data():
    while True:
        #read line from serial port
        line = ser.readline().decode('ascii' , errors='replace')
        #split based on comma
        line = line.split(',')
        #Determine which sensor is sending data
        match line[1]:
            case '0':
                ref_gyro.x = line[3]
                ref_gyro.y = line[4]
                ref_gyro.z = line[5]
                #print(gyro.x, gyro.y, gyro.z)
            case '1':
                ref_accel.x = line[3]
                ref_accel.y = line[4]
                ref_accel.z = line[5]
                #print(accel.x, accel.y, accel.z)
            case '2':
                ref_mag.x = line[3]
                ref_mag.y = line[4]
                ref_mag.z = line[5]
                #print(mag.x, mag.y, mag.z)

# Create and start the thread
serial_thread = threading.Thread(target=read_serial_data)
serial_thread.start()

#### Configure DLL ####
# Load the DLL
mydll = ctypes.cdll.LoadLibrary("./DevDLL/AirAPI_Windows.dll")

# Set the return type of the GetQuaternion function to a float pointer
mydll.GetRawGyro.restype = ctypes.POINTER(ctypes.c_float)
mydll.GetRawAccel.restype = ctypes.POINTER(ctypes.c_float)

# Call StartConnection
print("Attempting to connect to AirAPI_Driver...")
connection = mydll.StartConnection()

def getRawGyro():
    # Call a function from the DLL
    gyroPtr = mydll.GetRawGyro()
    rawGyro = [gyroPtr[i] for i in range(3)]
    return rawGyro

def getRawAccel():
    # Call a function from the DLL
    AccelPtr = mydll.GetRawAccel()
    rawAccel = [AccelPtr[i] for i in range(3)]
    return rawAccel


#### Configure Data sources ####
rawGyroReading = [0,0,0]
rawAccelReading = [0,0,0]
##Air Data source
def pollAirData():
    global rawGyroReading
    global rawAccelReading

    rawGyroReading = getRawGyro()
    rawAccelReading = getRawAccel()
    return


## Air data will be drawn grey
def getGyroX():
    return rawGyroReading[0]

## Reference data will be drawn red
def getRefGyroX():
    return ref_gyro.x

def getGyroY():
    return rawGyroReading[1]

def getRefGyroY():
    return ref_gyro.y

def getGyroZ():
    return rawGyroReading[2]

def getRefGyroZ():
    return ref_gyro.z

def getAccelX():
    return rawAccelReading[0]

def getRefAccelX():
    return ref_accel.x

def getAccelY():
    return rawAccelReading[1]

def getRefAccelY():
    return ref_accel.y

def getAccelZ():
    return rawAccelReading[2]

def getRefAccelZ():
    return ref_accel.z

def getMagX():
    return 0

def getRefMagX():
    return ref_mag.x

def getMagY():
    return 0

def getRefMagY():
    return ref_mag.y

def getMagZ():
    return 0

def getRefMagZ():
    return ref_mag.z

def create_plot(window, title,source, ref_source=None,XRange=None,YRange=None, row=None, colspan=2):
    plot = window.addPlot(title=title, colspan=colspan, row=row)
    plot.setLabel('bottom', 'Time', 's')
    if(XRange != None):
        plot.setXRange(XRange[0], XRange[1])
    else:
        plot.setXRange(-10, 0)
    plot.addLegend()
    if(YRange != None):
        plot.setYRange(YRange[0], YRange[1])

    data = np.empty((chunkSize, 2))
    data[:, 0] = np.linspace(-10, 0, chunkSize)
    data[:, 1] = np.nan
    
    ref_data = np.empty((chunkSize, 2)) if ref_source else None
    if ref_data is not None:
        ref_data[:, 0] = np.linspace(-10, 0, chunkSize)
        ref_data[:, 1] = np.nan

    ptr = 0

    main_curve = plot.plot(name="Air")
    ref_curve = plot.plot(name="Ref", pen='r') if ref_source else None

    def update():
        nonlocal data, ref_data, ptr, main_curve, ref_curve
        now = perf_counter()

        data[:-1] = data[1:]
        data[-1] = [now - startTime, source()]

        if ref_data is not None:
            ref_data[:-1] = ref_data[1:]
            ref_data[-1] = [now - startTime, ref_source()]

        plot.setXRange(now - startTime - 5, now - startTime)

        main_curve.setData(x=data[:, 0], y=data[:, 1])

        if ref_curve:
            ref_curve.setData(x=ref_data[:, 0], y=ref_data[:, 1])

        ptr += 1

    return update


win = pg.GraphicsLayoutWidget(show=True, size=(1400, 800))
win.setWindowTitle('AirPlot')

chunkSize = 100
maxChunks = 10
startTime = perf_counter()

# Set X range to 10 seconds
gyroXRange = [-10,0]
accelXRange = [-10,0]
magXRange = [-10,0]

# Set Y range
gyroYRange = [-120,120] #Min Max Degrees per second
accelYRange = [-2,2] #Min Max G's
magYRange = [-5,5] #Min Max Gauss


updateGyroX = create_plot(win, "Gyro X", getGyroX, getRefGyroX, XRange=gyroXRange, YRange=gyroYRange)
updateAccelX = create_plot(win, "Accel X", getAccelX, getRefAccelX, XRange=accelXRange, YRange=accelYRange)
updateMagX = create_plot(win, "Mag X", getMagX,getRefMagX, XRange=magXRange, YRange=magYRange)

win.nextRow()

updateGyroY = create_plot(win, "Gyro Y", getGyroY, getRefGyroY, XRange=gyroXRange, YRange=gyroYRange)
updateAccelY = create_plot(win, "Accel Y", getAccelY, getRefAccelY, XRange=accelXRange, YRange=accelYRange)
updateMagY = create_plot(win, "Mag Y", getMagY,getRefMagY, XRange=magXRange, YRange=magYRange)

win.nextRow()

updateGyroZ = create_plot(win, "Gyro Z", getGyroZ, getRefGyroZ, XRange=gyroXRange, YRange=gyroYRange)
updateAccelZ = create_plot(win, "Accel Z", getAccelZ, getRefAccelZ, XRange=accelXRange, YRange=accelYRange)
updateMagZ = create_plot(win, "Mag Z", getMagZ, getRefMagZ,XRange=magXRange, YRange=magYRange)


def update():
    pollAirData()

    updateGyroX()
    updateAccelX()
    updateMagX()

    updateGyroY()
    updateAccelY()
    updateMagY()

    updateGyroZ()
    updateAccelZ()
    updateMagZ()


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

if __name__ == '__main__':
    pg.exec()
