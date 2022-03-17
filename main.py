from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('Stock Chart') 
        self.resize(800, 1000)
        
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.stock_tab(), 'Stock Chart')
        self.tabs.addTab(self.watchlist(), 'Watchlist')
        layout.addWidget(self.tabs)

        layout = QVBoxLayout()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
