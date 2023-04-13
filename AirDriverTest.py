import ctypes
import atexit
from ctypes import c_float, POINTER, windll

# Replace "your_dll_name.dll" with the name of your DLL file
dll_path = "AirAPI_Windows.dll"

# Load kernel32.dll
kernel32 = windll.kernel32

# Load your DLL using LoadLibrary from kernel32.dll
dll_handle = kernel32.LoadLibraryA(dll_path.encode('utf-8'))

if not dll_handle:
    raise Exception("Failed to load DLL: {}".format(dll_path))

# Get the GetQuaternion function address
get_quaternion_func = ctypes.CFUNCTYPE(POINTER(c_float * 4))(("GetQuaternion", windll.kernel32))

# Call the GetQuaternion function
quaternion_ptr = get_quaternion_func()

# Extract the array of 4 floats from the returned pointer
quaternion = list(quaternion_ptr.contents)

print("Quaternion:", quaternion)

def unload_dll():
    print("Unloading DLL: {}".format(dll_path))
    if not kernel32.FreeLibrary(dll_handle):
        raise Exception("Failed to unload DLL: {}".format(dll_path))

# Register the cleanup function to be called upon exit
atexit.register(unload_dll)
