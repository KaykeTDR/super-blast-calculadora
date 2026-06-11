import qdarkstyle
from PySide6.QtWidgets import QApplication

def setup_theme(app:QApplication)-> None:
    app.setStyleSheet(
        qdarkstyle.load_stylesheet_pyside6()
        +"""
        QMainWindow{
                background-color: rgb(231, 213, 218);

        }
        QPushButton {
            font-size: 16px;
            border-radius: 6px;
            border: 2px solid rgb(117, 158, 175);
            padding: 8px;
            background-color: rgb(100, 140, 160); 
            color: white;
        }
        QPushButton:hover{
           background-color: rgb(53, 121, 255);
        }
        QPushButton:pressed{
            background-color:rgb(39, 61, 119);
        }
        QLineEdit {
    QLineEdit {
        background-color: rgb(244, 249, 255);
        color: rgb(39, 61, 119);
        border: 2px solid rgb(122, 187, 213);
        border-radius: 8px;
}
          
        }
        """
    )