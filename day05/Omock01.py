import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QPixmap
from PyQt5.uic.Compiler.qtproxies import QtCore

from PyQt5 import QtCore, QtGui, QtWidgets
import functools


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Omock01.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
   
    
    playerWB = True
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.ie = QtGui.QIcon('0.jpg')
        self.iw = QtGui.QIcon("1.jpg")
        self.ib = QtGui.QIcon("2.jpg")
        
        self.playerWB = False
        
        self.arr2d = [[0]*10 for i in range(10)]
        self.int2d = [[0]*10 for i in range(10)]
        
        
        self.initUI()    
        
        
        
        
        
    
    
    def showInt2d(self):
        print()
        for i in range(10):
            for j in range(10):
                print(self.int2d[i][j], end=' ')
            print()
        
        print()
    
    
    
    
    
    def myrender(self):
        for i in range(10):
            for j in range(10):
                
                if self.int2d[i][j] == 1:
#                     self.arr2d[i][j].setIcon(self.iw)
                    self.sender().setIcon(self.iw)
                    
                
                elif self.int2d[i][j] == 2:
#                     self.arr2d[i][j].setIcon(self.ib)
                    self.sender().setIcon(self.ib)
                    
    
    
    
    
    
    
    def alreadyinChk(self, firstL, secondL):
        
        
        if self.int2d[int(firstL)][int(secondL)] != 0:
            self.result = True
        else:
            self.result = False
    
        return self.result
    
    
    
    
    
    
    
    
    
    def resultView(self, firstL, secondL, playerWB):
        
        if playerWB == True:
            self.player = 1
        else:
            self.player = 2
            
        # 세로 라인
        self.upCount = self.getUp(int(firstL), int(secondL), int(self.player))
        self.downCount = self.getDown(int(firstL), int(secondL), int(self.player))
        self.collinecount = int(self.upCount) + int(self.downCount) + 1
        
        
        
        
        
        
        
        
        
        
        
        
         
        if self.player == 1:
            plNm = "흰돌"
        else:
            plNm = "검은돌"
             
        print(plNm+" : "+str(self.collinecount))
            
    
    
    
    
    
    
    def getUp(self, firstL, secondL, player):
        
        cnt = 0
        print(str(firstL)+","+str(secondL))
        print(self.int2d[int(firstL)][int(secondL)])
         
         
        try:
            while True:
                firstL = int(firstL) - 1
                if self.int2d[int(firstL)][int(secondL)] == player:
                    cnt+=1
                     
                else:
                    break
        except:
            return cnt
        
        return cnt
    
    
    
    
    
    
    def getDown(self, firstL, secondL, player):
        
        self.cnt = 0
        
        try:
             
            while True:
                firstL+=1
                if self.int2d[firstL][secondL] == player:
                     
                    self.cnt+=1
                else:
                    break
        except:
            return self.cnt
        
        return self.cnt
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def initUI(self):
        super().__init__()
        self.setupUi(self)
#         self.ie = QtGui.QIcon('0.jpg')
#         self.iw = QtGui.QIcon("1.jpg")
#         self.ib = QtGui.QIcon("2.jpg")

        for i in range(10):
            for j in range(10):
                
                self.qpbtn = QPushButton(self)
                self.qpbtn.setGeometry(75*j, 75*i, 75, 75) # x, y, width, height
                self.qpbtn.setIconSize(QtCore.QSize(75,75))
                self.qpbtn.setIcon(self.ie)
                self.qpbtn.setWhatsThis(str(i)+","+str(j))
                print(self.qpbtn.whatsThis(), end=' ')
                self.arr2d[i][j] = self.qpbtn.whatsThis()
                
                self.qpbtn.clicked.connect(self.clickedFunction)
            print()
         
        self.showInt2d() 
        self.resize(750,750)   
    
    
    
    
    
    
    def clickedFunction(self):
        self.location = self.sender().whatsThis().split(",")
        
#         print(self.sender().whatsThis())
        self.firstL = self.location[0]
        self.secondL = self.location[1]
         
        print("선택한 위치 : " + str(self.firstL) + "," + self.secondL)
         
         
        self.alInchk = self.alreadyinChk(int(self.firstL), int(self.secondL))
         
        print(self.alInchk)
         
         
        if self.alInchk == False:
               
            if self.playerWB == True:
                self.int2d[int(self.firstL)][int(self.secondL)] = 2
                self.playerWB = False
                self.gameResult = self.resultView(int(self.firstL), int(self.secondL), self.playerWB)
                   
            elif self.playerWB == False:
                self.int2d[int(self.firstL)][int(self.secondL)] = 1
                self.playerWB = True
                self.gameResult = self.resultView(int(self.firstL), int(self.secondL), self.playerWB)
               
        self.showInt2d()
        self.myrender()










if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    