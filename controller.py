# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from samplethread import samplethread
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class Controller(QtCore.QObject):

    result = QtCore.Signal(int)
    progress = QtCore.Signal(int)
    finished = QtCore.Signal()
    started = QtCore.Signal()
    resetLoop = QtCore.Signal()

    def __init__(self):
        super().__init__(None)
        self.worker = samplethread()
        self.worker.result.connect(self.result)
        self.worker.progress.connect(self.progress)
        self.worker.started.connect(self.started)
        self.worker.finished.connect(self.finished)
        self.resetLoop.connect(self.worker.handle_reset)


    @QtCore.Slot()
    def start(self):
        print("starting thread...")
        self.worker.start()
        QtCore.QThread.sleep(2)
        print("finished start method")

    @QtCore.Slot()
    def stop(self):
        self.worker.requestInterruption()
        print("stop requested")
        self.worker.wait()
        self.worker.quit()

    @QtCore.Slot()
    def resetThreadloop(self):
        self.resetLoop.emit()
