# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path
from controller import Controller
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle



if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    controller = Controller()
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
