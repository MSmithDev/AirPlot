from time import perf_counter

import numpy as np

import pyqtgraph as pg

## Configure Data sources
def getGyroX():
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
    curves = []
    ref_curves = [] if ref_source else None
    data = np.empty((chunkSize + 1, 2))
    ref_data = np.empty((chunkSize + 1, 2)) if ref_source else None
    ptr = 0

    def update():
        nonlocal data, ref_data, ptr, curves, ref_curves
        now = perf_counter()
        for c in curves:
            c.setPos(-(now - startTime), 0)
        if ref_curves:
            for c in ref_curves:
                c.setPos(-(now - startTime), 0)

        i = ptr % chunkSize
        if i == 0:
            curve = plot.plot(name="Data")
            curves.append(curve)
            if ref_source:
                ref_curve = plot.plot(pen='r')
                ref_curves.append(ref_curve)
            last = data[-1]
            data = np.empty((chunkSize + 1, 2))
            data[0] = last
            if ref_source:
                last = ref_data[-1]
                ref_data = np.empty((chunkSize + 1, 2))
                ref_data[0] = last
            while len(curves) > maxChunks:
                c = curves.pop(0)
                plot.removeItem(c)
                if ref_curves:
                    c = ref_curves.pop(0)
                    plot.removeItem(c)
        else:
            curve = curves[-1]
            if ref_curves:
                ref_curve = ref_curves[-1]
        data[i + 1, 0] = now - startTime
        data[i + 1, 1] = source()
        curve.setData(x=data[:i + 2, 0], y=data[:i + 2, 1])
        if ref_curves:
            ref_data[i + 1, 0] = now - startTime
            ref_data[i + 1, 1] = ref_source()
            ref_curve.setData(x=ref_data[:i + 2, 0], y=ref_data[:i + 2, 1])
        ptr += 1

    return update



win = pg.GraphicsLayoutWidget(show=True, size=(1400, 800))
win.setWindowTitle('AirPlot')

chunkSize = 100
maxChunks = 10
startTime = perf_counter()

updateGyroX = create_plot(win, "Gyro X", getGyroX, getMagX)
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
