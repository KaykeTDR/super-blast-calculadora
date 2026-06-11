from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
)

from enviromente import WINDOW_ICON_PATH


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._setup_window()
        self._setup_ui()

    def _setup_window(self):
        self.setWindowTitle("Super Blast Calculadora")
        self.setWindowIcon(QIcon(str(WINDOW_ICON_PATH)))

    def _setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.size())

    def add_to_layout(self, widget: QWidget):
        self.main_layout.addWidget(widget)
