from PySide6.QtWidgets import ( QLineEdit,
                                QLabel,
                                QPushButton)
from enviromente import big_font,text_margin ,small_font,medium_font
from PySide6.QtCore import Qt

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.config_style()

    def config_style(self):
    
        self.setStyleSheet(f'font-size:{big_font}px;')
        self.setMinimumHeight(big_font*2*1/2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(text_margin,text_margin,text_margin,text_margin)
        self.setMinimumWidth(400)


class Info(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.config_style()
    def config_style(self):
        self.setStyleSheet(f'font-size: {small_font}px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

class Botao(QPushButton):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.config_style_sheet()
    
    def config_style_sheet(self):
        font = self.font()
        font.setPixelSize(medium_font)
        self.setMinimumSize(30,30)