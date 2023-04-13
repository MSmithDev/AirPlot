import ctypes
import time

# Load the DLL
mydll = ctypes.cdll.LoadLibrary("./DevDLL/AirAPI_Windows.dll")

# Set the return type of the GetQuaternion function to a float pointer
#mydll.GetQuaternion.restype = ctypes.POINTER(ctypes.c_float)
mydll.GetRawGyro.restype = ctypes.POINTER(ctypes.c_float)


# Call StartConnection
print("Attempting to connect to AirAPI_Driver...")
connection = mydll.StartConnection()

def getQuaternion():
    # Call a function from the DLL
    qtPtr = mydll.GetQuaternion()
    quaternion = [qtPtr[i] for i in range(4)]
    return quaternion

def getRawGyro():
    # Call a function from the DLL
    gyroPtr = mydll.GetRawGyro()
    rawGyro = [gyroPtr[i] for i in range(3)]
    return rawGyro

#rawGyro = mydll.GetRawGyro()

# Convert the result pointer to an array of four floats


#rawGyroArr = [rawGyro[i] for i in range(3)]

# Print the connection result
print(connection)

if(1 == 2):
    print("Failed to StartConnection")
else:
    while True:
        print("Printing Data")
        test = getRawGyro()
        print("Raw Gyro: ", test[0])
        #print("Raw Gyro: ", rawGyroArr)
        #wait 1 second
        time.sleep(0.5)

#print raw gyro
#print(rawGyroArr)