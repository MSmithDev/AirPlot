"""
Various methods of drawing scrolling plots.
"""

from time import perf_counter

import numpy as np

import pyqtgraph as pg

win = pg.GraphicsLayoutWidget(show=True, size=(1400,800))
win.setWindowTitle('AirPlot')




#Gyro X axis#

# 3) Plot in chunks, adding one new plot curve for every 100 samples
chunkSize = 100
# Remove chunks after we have 10
maxChunks = 10
startTime = perf_counter()
GyroX = win.addPlot(title="Gyro X",colspan=2)
GyroX.setLabel('bottom', 'Time', 's')
GyroX.setXRange(-10, 0)
GXcurves = []
GXdata = np.empty((chunkSize+1,2))
ptrGyroX = 0

def updateGyroX():
    global GyroX, GXdata, ptrGyroX, GXcurves
    now = perf_counter()
    for c in GXcurves:
        c.setPos(-(now-startTime), 0)
    
    i = ptrGyroX % chunkSize
    if i == 0:
        GXcurve = GyroX.plot()
        GXcurves.append(GXcurve)
        last = GXdata[-1]
        GXdata = np.empty((chunkSize+1,2))        
        GXdata[0] = last
        while len(GXcurves) > maxChunks:
            c = GXcurves.pop(0)
            GyroX.removeItem(c)
    else:
        GXcurve = GXcurves[-1]
    GXdata[i+1,0] = now - startTime
    GXdata[i+1,1] = np.random.normal() #replace with realtime data 
    GXcurve.setData(x=GXdata[:i+2, 0], y=GXdata[:i+2, 1])
    ptrGyroX += 1

#Accel X axis#

AccelX = win.addPlot(title="Accel X",colspan=2)
AccelX.setLabel('bottom', 'Time', 's')
AccelX.setXRange(-10, 0)
AXcurves = []
AXdata = np.empty((chunkSize+1,2))
ptrAccelX = 0

def updateAccelX():
    global AccelX, AXdata, ptrAccelX, AXcurves
    now = perf_counter()
    for c in AXcurves:
        c.setPos(-(now-startTime), 0)
    
    i = ptrAccelX % chunkSize
    if i == 0:
        AXcurve = AccelX.plot()
        AXcurves.append(AXcurve)
        last = AXdata[-1]
        AXdata = np.empty((chunkSize+1,2))        
        AXdata[0] = last
        while len(AXcurves) > maxChunks:
            c = AXcurves.pop(0)
            AccelX.removeItem(c)
    else:
        AXcurve = AXcurves[-1]
    AXdata[i+1,0] = now - startTime
    AXdata[i+1,1] = np.random.normal() #replace with realtime data 
    AXcurve.setData(x=AXdata[:i+2, 0], y=AXdata[:i+2, 1])
    ptrAccelX += 1

#Mag X axis#

MagX = win.addPlot(title="Mag X",colspan=2)
MagX.setLabel('bottom', 'Time', 's')
MagX.setXRange(-10, 0)
MXcurves = []
MXdata = np.empty((chunkSize+1,2))
ptrMagX = 0

def updateMagX():
    global MagX, MXdata, ptrMagX, MXcurves
    now = perf_counter()
    for c in MXcurves:
        c.setPos(-(now-startTime), 0)
    
    i = ptrMagX % chunkSize
    if i == 0:
        MXcurve = MagX.plot()
        MXcurves.append(MXcurve)
        last = MXdata[-1]
        MXdata = np.empty((chunkSize+1,2))        
        MXdata[0] = last
        while len(MXcurves) > maxChunks:
            c = MXcurves.pop(0)
            MagX.removeItem(c)
    else:
        MXcurve = MXcurves[-1]
    MXdata[i+1,0] = now - startTime
    MXdata[i+1,1] = np.random.normal() #replace with realtime data 
    MXcurve.setData(x=MXdata[:i+2, 0], y=MXdata[:i+2, 1])
    ptrMagX += 1


#Gyro Y axis#

win.nextRow()

GyroY = win.addPlot(title="Gyro Y",colspan=2)
GyroY.setLabel('bottom', 'Time', 's')
GyroY.setXRange(-10, 0)
GYcurves = []
GYdata = np.empty((chunkSize+1,2))
ptrGyroY = 0

def updateGyroY():
    global GyroY, GYdata, ptrGyroY, GYcurves
    now = perf_counter()
    for c in GYcurves:
        c.setPos(-(now-startTime), 0)
    
    i = ptrGyroY % chunkSize
    if i == 0:
        GYcurve = GyroY.plot()
        GYcurves.append(GYcurve)
        last = GYdata[-1]
        GYdata = np.empty((chunkSize+1,2))        
        GYdata[0] = last
        while len(GYcurves) > maxChunks:
            c = GYcurves.pop(0)
            GyroY.removeItem(c)
    else:
        GYcurve = GYcurves[-1]
    GYdata[i+1,0] = now - startTime
    GYdata[i+1,1] = np.random.normal() #replace with realtime data 
    GYcurve.setData(x=GYdata[:i+2, 0], y=GYdata[:i+2, 1])
    ptrGyroY += 1

#Accel Y axis#

AccelY = win.addPlot(title="Accel Y",colspan=2)
AccelY.setLabel('bottom', 'Time', 's')
AccelY.setXRange(-10, 0)
AYcurves = []
AYdata = np.empty((chunkSize+1,2))
ptrAccelY = 0

def updateAccelY():
    global AccelY, AYdata, ptrAccelY, AYcurves
    now = perf_counter()
    for c in AYcurves:
        c.setPos(-(now-startTime), 0)
    
    i = ptrAccelY % chunkSize
    if i == 0:
        AYcurve = AccelY.plot()
        AYcurves.append(AYcurve)
        last = AYdata[-1]
        AYdata = np.empty((chunkSize+1,2))        
        AYdata[0] = last
        while len(AYcurves) > maxChunks:
            c = AYcurves.pop(0)
            AccelY.removeItem(c)
    else:
        AYcurve = AYcurves[-1]
    AYdata[i+1,0] = now - startTime
    AYdata[i+1,1] = np.random.normal() #replace with realtime data 
    AYcurve.setData(x=AYdata[:i+2, 0], y=AYdata[:i+2, 1])
    ptrAccelY += 1

#Mag Y axis#

MagY = win.addPlot(title="Mag Y",colspan=2)
MagY.setLabel('bottom', 'Time', 's')
MagY.setXRange(-10, 0)
MYcurves = []
MYdata = np.empty((chunkSize+1,2))
ptrMagY = 0

def updateMagY():
    global MagY, MYdata, ptrMagY, MYcurves
    now = perf_counter()
    for c in MYcurves:
        c.setPos(-(now-startTime), 0)
    
    i = ptrMagY % chunkSize
    if i == 0:
        MYcurve = MagY.plot()
        MYcurves.append(MYcurve)
        last = MYdata[-1]
        MYdata = np.empty((chunkSize+1,2))        
        MYdata[0] = last
        while len(MYcurves) > maxChunks:
            c = MYcurves.pop(0)
            MagY.removeItem(c)
    else:
        MYcurve = MYcurves[-1]
    MYdata[i+1,0] = now - startTime
    MYdata[i+1,1] = np.random.normal() #replace with realtime data 
    MYcurve.setData(x=MYdata[:i+2, 0], y=MYdata[:i+2, 1])
    ptrMagY += 1


win.nextRow()

GyroZ = win.addPlot(title="Gyro Z",colspan=2)
GyroZ.setLabel('bottom', 'Time', 's')
GyroZ.setXRange(-10, 0)
GZcurves = []
GZdata = np.empty((chunkSize+1,2))
ptrGyroZ = 0

def updateGyroZ():
    global GyroZ, GZdata, ptrGyroZ, GZcurves
    now = perf_counter()
    for c in GZcurves:
        c.setPos(-(now-startTime), 0)
    
    i = ptrGyroZ % chunkSize
    if i == 0:
        GZcurve = GyroZ.plot(name='Gyro Z')
        GZcurves.append(GZcurve)
        last = GZdata[-1]
        GZdata = np.empty((chunkSize+1,2))        
        GZdata[0] = last
        while len(GZcurves) > maxChunks:
            c = GZcurves.pop(0)
            GyroZ.removeItem(c)
    else:
        GZcurve = GZcurves[-1]
    GZdata[i+1,0] = now - startTime
    GZdata[i+1,1] = np.random.normal() #replace with realtime data 
    GZcurve.setData(x=GZdata[:i+2, 0], y=GZdata[:i+2, 1])
    ptrGyroZ += 1


#Accel Z axis#

AccelZ = win.addPlot(title="Accel Z",colspan=2)
AccelZ.setLabel('bottom', 'Time', 's')
AccelZ.setXRange(-10, 0)
AZcurves = []
AZdata = np.empty((chunkSize+1,2))
ptrAccelZ = 0

def updateAccelZ():
    global AccelZ, AZdata, ptrAccelZ, AZcurves
    now = perf_counter()
    for c in AZcurves:
        c.setPos(-(now-startTime), 0)
    
    i = ptrAccelZ % chunkSize
    if i == 0:
        AZcurve = AccelZ.plot()
        AZcurves.append(AZcurve)
        last = AZdata[-1]
        AZdata = np.empty((chunkSize+1,2))        
        AZdata[0] = last
        while len(AZcurves) > maxChunks:
            c = AZcurves.pop(0)
            AccelZ.removeItem(c)
    else:
        AZcurve = AZcurves[-1]
    AZdata[i+1,0] = now - startTime
    AZdata[i+1,1] = np.random.normal() #replace with realtime data 
    AZcurve.setData(x=AZdata[:i+2, 0], y=AZdata[:i+2, 1])
    ptrAccelZ += 1


#Mag Z axis#

MagZ = win.addPlot(title="Mag Z",colspan=2)
MagZ.setLabel('bottom', 'Time', 's')
MagZ.setXRange(-10, 0)
MZcurves = []
MZdata = np.empty((chunkSize+1,2))
ptrMagZ = 0

def updateMagZ():
    global MagZ, MZdata, ptrMagZ, MZcurves
    now = perf_counter()
    for c in MZcurves:
        c.setPos(-(now-startTime), 0)
    
    i = ptrMagZ % chunkSize
    if i == 0:
        MZcurve = MagZ.plot()
        MZcurves.append(MZcurve)
        last = MZdata[-1]
        MZdata = np.empty((chunkSize+1,2))        
        MZdata[0] = last
        while len(MZcurves) > maxChunks:
            c = MZcurves.pop(0)
            MagZ.removeItem(c)
    else:
        MZcurve = MZcurves[-1]
    MZdata[i+1,0] = now - startTime
    MZdata[i+1,1] = np.random.normal() #replace with realtime data 
    MZcurve.setData(x=MZdata[:i+2, 0], y=MZdata[:i+2, 1])
    ptrMagZ += 1


# update all plots
def update():
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
