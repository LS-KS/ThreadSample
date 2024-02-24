# This Python file uses the following encoding: utf-8
from PySide6 import QtCore


class samplethread(QtCore.QThread):
    result = QtCore.Signal(int)
    progress = QtCore.Signal(int)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.end = 30
        self.results = []
        self.reset = False

    def run(self):
        print("start long running task")
        i: int = 0
        while i < self.end:
            if self.reset:
                i = 0
                self.reset = False
            if i == 0 or i==1:
                self.results.append(1)
            else:
                self.results.append(self.results[i-1]+self.results[i-2])
            self.result.emit(self.results[i])
            i +=1
            self.progress.emit(i)
            if self.currentThread().isInterruptionRequested():
                print("Thread recognized interrupt")
                QtCore.QThread.sleep(1)
                return
            QtCore.QThread.sleep(1)

    def do_work(self):
        pass

    QtCore.Slot()
    def handle_reset(self):
        self.reset = True
