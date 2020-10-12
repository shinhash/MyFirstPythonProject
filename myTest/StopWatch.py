import sys, time
from threading import Timer
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("StopWatch.ui")[0]

clickable = False
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.startbutton.clicked.connect(self.startBtn)
#         self.stopbutton.clicked.connect(self.stopclickedFunction)
        
        
    def startBtn(self):
#         self.milSeclbl.setText(str(1))
        self.milSecNum = self.milSeclbl.text()
        self.secNum = ""
        self.milSeclbl.setText(str(int(self.milSecNum) + 1))
        
        if self.milSeclbl.text() == str(100):
            self.milSeclbl.setText(str(0))
            self.secNum = self.seclbl.text()
            self.seclbl.setText(str(int(self.secNum) + 1))
            
            
        # 타이머 설정 (1초마다, 콜백함수)
        global timer
        timer = Timer(0.01, self.startBtn)
        timer.start()



    
    def stopclickedFunction(self):
#         global timer
#         timer._stop()
        self.milSeclbl.setText("stop Test")


        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()