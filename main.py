import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from pyqt.stock import UsStock
from pyqt.stock import Crypto
from pyqt.stock import KorStock
from pyqt.util import resource_path


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.read_data()
        self.init_ui()

    def read_data(self):
        self.data_path = resource_path('data/watchlist.csv')
        self.data = pd.read_csv(self.data_path, dtype=str)
        self.data[['Name', 'Crypto']] = self.data[['Name', 'Crypto']].fillna('')

    def init_ui(self):
        self.setWindowTitle('Stock Chart') 
        self.resize(800, 1000)
        
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.stock_tab(), 'Stock Chart')
        self.tabs.addTab(self.watchlist(), 'Watchlist')
        layout.addWidget(self.tabs)

    def stock_tab(self):
        outer_most = QWidget()

        self.layout = QVBoxLayout()

        stock_chart_tab = QWidget()
        stock_chart_tab.setLayout(self.layout)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(stock_chart_tab)
        
        content = QHBoxLayout()
        content.addWidget(self.scroll)
        outer_most.setLayout(content)
        return outer_most

    def watchlist(self):
        watchlist_tab = QWidget()
        layout = QVBoxLayout()
        layout.addLayout(self.add_form())

        self.table = QTableView(self)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.col_len = len(self.data.columns)
        self.content = QStandardItemModel(0, self.col_len, self)
        self.content.setHorizontalHeaderLabels(self.data.columns)
        self.table.setModel(self.content)

        layout.addWidget(self.table)
        self.read_watchlist()

        remove_button = QPushButton('Remove Selected Stock', self)
        remove_button.setFixedWidth(200)
        remove_button.setShortcut('Backspace')
        remove_button.clicked.connect(self.remove_item)
        layout.addWidget(remove_button)

        watchlist_tab.setLayout(layout)
        return watchlist_tab

    def draw_label(self, label_name):
        label = QLabel(label_name, self)
        input_box = QLineEdit(self)
        input_box.setFixedWidth(150)
        return label, input_box

    def add_form(self):
        form_layout = QVBoxLayout()

        symbol_label, self.stock = self.draw_label('Symbol')
        form_layout.addWidget(symbol_label)
        form_layout.addWidget(self.stock)

        company_label, self.company = self.draw_label('Name')
        form_layout.addWidget(company_label)
        form_layout.addWidget(self.company)

        self.check_box = QCheckBox('Crypto', self)
        form_layout.addWidget(self.check_box)

        add_button = QPushButton('Add', self)
        add_button.setFixedWidth(100)
        add_button.setShortcut('Return')
        add_button.clicked.connect(self.add_item)
        form_layout.addWidget(add_button)
        return form_layout

    def group(self, symbol, stock_name, is_crypto: bool=False, is_kor: bool=False):
        group_box = QGroupBox()
        group_box.setFixedHeight(300)

        layout = QVBoxLayout()
        name_layout = QHBoxLayout()
        name = QLabel(stock_name)
        name.setFont(QFont('Arial', 18, weight=QFont.Bold))
        ticker = QLabel(f'({symbol})')
        name_layout.addWidget(name)
        name_layout.addWidget(ticker)
        name_layout.addStretch()
        layout.addLayout(name_layout)
        
        if not is_kor:
            stock = UsStock(symbol)
        elif is_crypto:
            stock = Crypto(symbol)
        else:
            stock = KorStock(symbol)
        price = stock.get_price_now()
        price_layout = QHBoxLayout()
        price_now = round(float(price['c']), 2)
        price_label = QLabel(str(price_now))
        price_label.setFont(QFont('Arial', 14,  weight=QFont.Bold))

        change = int(price['d'])
        if change > 0:
            color = 'green'
            sign = '+'
        elif change < 0:
            color = 'red'
            sign = '-'
        else:
            color = 'white'
            sign = ''
        pct_change = round(float(price['dp']), 2)
        price_group = f'{sign}{change} ({pct_change}%)'
        price_info_label = QLabel(price_group)
        price_info_label.setStyleSheet(f'Color : {color}')
        plot = stock.draw_chart()
        price_layout.addWidget(price_label)
        price_layout.addWidget(price_info_label)
        price_layout.addStretch()
        layout.addLayout(price_layout)

        layout.addWidget(plot)
        layout.addStretch()

        group_box.setLayout(layout)
        return group_box

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
