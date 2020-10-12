import sys, time, threading
from threading import Timer
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPalette, QColor

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("my_rgb.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    
    def __init__(self) :
        super().__init__()
        self.index = 0
        self.setupUi(self)
        self.startButton.clicked.connect(self.onClicked)
        
    
    def onClicked(self):
        t1 = threading.Thread(target=self.realChangefunc, args=())
        t1.start()
        
        
    def realChangefunc(self):
        
        while True:
            if self.index%3 == 0 :
                
#                 self.le1.setStyleSheet("background-color: #ff0000")
#                 self.le2.setStyleSheet("background-color: #00ff00")
#                 self.le3.setStyleSheet("background-color: #0000ff")
#                   
#                 self.pe1.setStyleSheet("background-color: #ff0000")
#                 self.pe2.setStyleSheet("background-color: #00ff00")
#                 self.pe3.setStyleSheet("background-color: #0000ff")
                 
                self.gv1.setStyleSheet("background-color: #ff0000")
                self.gv2.setStyleSheet("background-color: #00ff00")
                self.gv3.setStyleSheet("background-color: #0000ff")
                
                
#                 self.lbl1.setStyleSheet("QLabel { color: #ff0000; background-color: #ff0000; }")
#                 self.lbl2.setStyleSheet("QLabel { color: #00ff00; background-color: #00ff00; }")
#                 self.lbl3.setStyleSheet("QLabel { color: #0000ff; background-color: #0000ff; }") 
#                 
#                 self.lbl1.setText("R")
#                 self.lbl2.setText("G")
#                 self.lbl3.setText("B")
                
            elif self.index%3 == 1 :
                
#                 self.le1.setStyleSheet("background-color: #0000ff")
#                 self.le2.setStyleSheet("background-color: #ff0000")
#                 self.le3.setStyleSheet("background-color: #00ff00")
#                  
#                 self.pe1.setStyleSheet("background-color: #0000ff")
#                 self.pe2.setStyleSheet("background-color: #ff0000")
#                 self.pe3.setStyleSheet("background-color: #00ff00")
                 
                self.gv1.setStyleSheet("background-color: #0000ff")
                self.gv2.setStyleSheet("background-color: #ff0000")
                self.gv3.setStyleSheet("background-color: #00ff00")
                
                
#                 self.lbl1.setStyleSheet("QLabel { color: #0000ff; background-color: #0000ff; }")
#                 self.lbl2.setStyleSheet("QLabel { color: #ff0000; background-color: #ff0000; }")
#                 self.lbl3.setStyleSheet("QLabel { color: #00ff00; background-color: #00ff00; }")
#                 
#                 self.lbl1.setText("B")
#                 self.lbl2.setText("R")
#                 self.lbl3.setText("G")
                
            elif self.index%3 == 2 :
                
#                 self.le1.setStyleSheet("background-color: #00ff00")
#                 self.le2.setStyleSheet("background-color: #0000ff")
#                 self.le3.setStyleSheet("background-color: #ff0000")
#                  
#                 self.pe1.setStyleSheet("background-color: #00ff00")
#                 self.pe2.setStyleSheet("background-color: #0000ff")
#                 self.pe3.setStyleSheet("background-color: #ff0000")
                 
                self.gv1.setStyleSheet("background-color: #00ff00")  
                self.gv2.setStyleSheet("background-color: #0000ff")  
                self.gv3.setStyleSheet("background-color: #ff0000")  
                
#                 self.lbl1.setStyleSheet("QLabel { color: #00ff00; background-color: #00ff00; }")
#                 self.lbl2.setStyleSheet("QLabel { color: #0000ff; background-color: #0000ff; }")
#                 self.lbl3.setStyleSheet("QLabel { color: #ff0000; background-color: #ff0000; }")
#                 
#                 self.lbl1.setText("G")
#                 self.lbl2.setText("B")
#                 self.lbl3.setText("R")
           
            self.index += 1
            time.sleep(1)
    
        
        

        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()