#### Configure DLL ####
import ctypes
import time
# Load the DLL
AirAPI = ctypes.cdll.LoadLibrary("./DevDLL/AirAPI_Windows.dll")

# Set the return type of the GetQuaternion function to a float pointer
#AirAPI.GetRawGyro.restype = ctypes.POINTER(ctypes.c_float)
#AirAPI.GetRawAccel.restype = ctypes.POINTER(ctypes.c_float)
AirAPI.GetEuler.restype = ctypes.POINTER(ctypes.c_float)
#AirAPI.GetRawMag.restype = ctypes.POINTER(ctypes.c_float)

#set return type of GetAirTimestamp to uint64
#AirAPI.GetAirTimestamp.restype = ctypes.c_uint64


# Call StartConnection
print("Attempting to connect to AirAPI_Driver...")
connection = AirAPI.StartConnection()

while True:
    print("meh")
    #sleep 100ms
    time.sleep(0.1)

#write a function that generates prime numbers and devide the number by 101

