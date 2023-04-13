from time import perf_counter

import numpy as np

import pyqtgraph as pg

#### Configure Data sources ####

## Air data will be drawn grey
def getGyroX():
    return np.random.normal()

## Reference data will be drawn red
def getRefGyroX():
    return np.random.normal()

def getGyroY():
    return np.random.normal()

def getGyroZ():
    return np.random.normal()

def getAccelX():
    return np.random.normal()

def getAccelY():
    return np.random.normal()

def getAccelZ():
    return np.random.normal()

def getMagX():
    return np.random.normal()

def getMagY():
    return np.random.normal()

def getMagZ():
    return np.random.normal()

def create_plot(window, title, source, ref_source=None, row=None, colspan=2):
    plot = window.addPlot(title=title, colspan=colspan, row=row)
    plot.setLabel('bottom', 'Time', 's')
    plot.setXRange(-10, 0)
    plot.addLegend()

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

updateGyroX = create_plot(win, "Gyro X", getGyroX, getRefGyroX)
updateAccelX = create_plot(win, "Accel X", getAccelX)
updateMagX = create_plot(win, "Mag X", getMagX)

win.nextRow()

updateGyroY = create_plot(win, "Gyro Y", getGyroY)
updateAccelY = create_plot(win, "Accel Y", getAccelY)
updateMagY = create_plot(win, "Mag Y", getMagY)

win.nextRow()

updateGyroZ = create_plot(win, "Gyro Z", getGyroZ)
updateAccelZ = create_plot(win, "Accel Z", getAccelZ)
updateMagZ = create_plot(win, "Mag Z", getMagZ)


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
