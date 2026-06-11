import sys
from style import setup_theme
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from display import Display, Info,Botao
from enviromente import WINDOW_ICON_PATH
from mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Super Blast Calculadora")
    app.setWindowIcon(QIcon(str(WINDOW_ICON_PATH)))

    window = MainWindow()

    # info
    info = Info()
    info.setText('conta')
    window.add_to_layout(info)
   
    # Display
    display = Display()
    display.setPlaceholderText('digite algo')
    window.add_to_layout(display)
   
    #botao
    botao_ = Botao('7')
    window.add_to_layout(botao_)

    setup_theme(app)
    window.adjust_fixed_size()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()