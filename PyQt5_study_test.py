#! usr/bin/python
# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel,QVBoxLayout,QSlider
from PyQt5.QtCore import Qt

class Data():
    def __init__(self):
        self.count=0

class MainForm(QWidget):

    def __init__(self,data):
        super().__init__()
        
        self.data=data
        self.init_UI()
        
    def init_UI(self):
        self.Push_Me = QPushButton('点击me')
        self.Push_you = QPushButton('点击you')
        self.Label_Info = QLabel('Not push me yet!')
        self.Slider_Info = QSlider(Qt.Horizontal)
        
        v_box_layout = QVBoxLayout()
        v_box_layout.addWidget(self.Push_Me)
        v_box_layout.addWidget(self.Push_you)
        v_box_layout.addWidget(self.Label_Info)
        v_box_layout.addWidget(self.Slider_Info)
        
        self.Push_Me.pressed.connect(self.btn_clicked)
        self.Push_you.pressed.connect(self.btn_clicked)
        
        self.setLayout(v_box_layout)
        
        self.setWindowTitle('me')
        self.show()
        
    def btn_clicked(self):
        rr = self.sender().text()

        self.data.count+=1
        self.Slider_Info.setValue(self.data.count)
        if rr=='点击me':
            self.Label_Info.setText('You push me !'+rr+str(self.data.count))
        else:
            self.Label_Info.setText('You push you !'+rr+str(self.data.count))
        
        
def main():
    app = QApplication(sys.argv)
    a = MainForm(Data())
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()