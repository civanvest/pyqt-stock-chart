import sys
import numpy as np
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QLabel,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Stock Chart")
        self.setLayout(self.layout)

    def initUI(self):
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        self.layout = layout



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())