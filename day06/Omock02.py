import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QPixmap
from PyQt5.uic.Compiler.qtproxies import QtCore

from PyQt5 import QtCore, QtGui, QtWidgets
import functools


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Omock02.ui")[0]

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
        self.gameEnd = False
        self.gameResult = False
        
        self.arr2d = [[0]*10 for i in range(10)]
        self.int2d = [[0]*10 for i in range(10)]
        
        
        self.initUI()    
        
        
        
        
        
    
    
    def showInt2d(self):
        print()
        for i, val in enumerate(self.arr2d):
            for j, val in enumerate(self.arr2d):
                print(self.int2d[i][j], end=' ')
            print()
        
        print()
    
    
    
    
    
    def myrender(self):
        for i, val in enumerate(self.arr2d):
            for j, val in enumerate(self.arr2d):
                
                if self.int2d[i][j] == 1:
                    self.arr2d[i][j].setIcon(self.iw)
#                     self.sender().setIcon(self.iw)
                    
                
                if self.int2d[i][j] == 2:
                    self.arr2d[i][j].setIcon(self.ib)
#                     self.sender().setIcon(self.ib)
                
                if self.int2d[i][j] == 0:
                    self.arr2d[i][j].setIcon(self.ie)
    
    
    
    
    
    
    def alreadyinChk(self, firstL, secondL):
        
        
        if self.int2d[int(firstL)][int(secondL)] != 0:
            self.result = True
        else:
            self.result = False
    
        return self.result
    
    
    
    
    
    
    
    
    
    def resultView(self, firstL, secondL, playerWB):
        
        self.res = False
        
        if playerWB == True:
            self.player = 1
        else:
            self.player = 2
            
            
            
            
        # 세로 라인
        self.upCount = self.getUp(int(firstL), int(secondL), int(self.player))
        self.downCount = self.getDown(int(firstL), int(secondL), int(self.player))
        self.colLineCount = int(self.upCount) + int(self.downCount) + 1
        print("세로 : " + str(self.colLineCount))
        
        
        
        
        # 가로 라인
        self.leftCount = self.getLeft(int(firstL), int(secondL), int(self.player))
        self.rightCount = self.getRight(int(firstL), int(secondL), int(self.player))
        self.rowLineCount = int(self.leftCount) + int(self.rightCount) + 1
        print("가로 : " + str(self.rowLineCount))
        
        
        
        
        # 좌측 대각선
        self.leftUpCount = self.getLeftUp(int(firstL), int(secondL), int(self.player))
        self.rightDownCount = self.getRightDown(int(firstL), int(secondL), int(self.player))
        self.leftDiaCount = int(self.leftUpCount) + int(self.rightDownCount) + 1
        print("좌측 대각선 : " + str(self.leftDiaCount))
        
        
        
        
        # 우측 대각선
        self.rightUpCount = self.getRightUp(int(firstL), int(secondL), int(self.player))
        self.leftDownCount = self.getLeftDown(int(firstL), int(secondL), int(self.player))
        self.rightDiaCount = int(self.rightUpCount) + int(self.leftDownCount) + 1
        print("우측 대각선 : " + str(self.rightDiaCount))
        
        
        
        self.resultArr = [0 for i in range(4)]
        self.resultArr[0] = self.colLineCount
        self.resultArr[1] = self.rowLineCount
        self.resultArr[2] = self.leftDiaCount
        self.resultArr[3] = self.rightDiaCount
        
        
        for i in range(4):
            if self.player == 1:
                plNm = "흰돌"
            else:
                plNm = "검은돌"
            
            if self.resultArr[i] == 5:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("결과")
                msgBox.setText(plNm+" 이 우승했습니다. !!")
                msgBox.exec_()
                self.res = True
    
        return self.res
    
    
    
    
    
    # upCount
    def getUp(self, firstL, secondL, player):
        
        cnt = 0
        try:
            while True:
                firstL = int(firstL) - 1
                if firstL < 0 or firstL > len(self.int2d)-1:
                    return cnt
                if self.int2d[int(firstL)][int(secondL)] == player:
                    cnt+=1
                else:
                    break
        except:
            return cnt
        
        return cnt
    
    
    
    
    # downCount
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # leftCount
    def getLeft(self, firstL, secondL, player):
        
        self.cnt = 0
        try:
            while True:
                secondL-=1
                if secondL < 0:
                    return self.cnt
                if self.int2d[firstL][secondL] == player:
                    self.cnt+=1
                else:
                    break
        except:
            return self.cnt
        
        return self.cnt
    
    
    
    # rightCount
    def getRight(self, firstL, secondL, player):
        
        self.cnt = 0
        try:
            while True:
                secondL+=1
                if secondL > len(self.int2d)-1:
                    return self.cnt
                if self.int2d[firstL][secondL] == player:
                    self.cnt+=1
                else:
                    break
        except:
            return self.cnt
        
        return self.cnt
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # leftUpCount
    def getLeftUp(self, firstL, secondL, player):
        
        self.cnt = 0
        try:
            while True:
                firstL-=1
                secondL-=1
                if firstL < 0 or secondL < 0:
                    return self.cnt
                if self.int2d[firstL][secondL] == player:
                    self.cnt+=1
                else:
                    break
        except:
            return self.cnt
        
        return self.cnt    
    
    
    
    # rightDownCount
    def getRightDown(self, firstL, secondL, player):
        
        self.cnt = 0
        try:
            while True:
                firstL+=1
                secondL+=1
                if firstL > len(self.int2d)-1 or secondL > len(self.int2d)-1:
                    return self.cnt
                if self.int2d[firstL][secondL] == player:
                    self.cnt+=1
                else:
                    break
        except:
            return self.cnt
        
        return self.cnt
    
    
    
    
    
    # rightUpCount
    def getRightUp(self, firstL, secondL, player):
        
        self.cnt = 0
        try:
            while True:
                firstL-=1
                secondL+=1
                if firstL < 0 or secondL > len(self.int2d)-1:
                    return self.cnt
                if self.int2d[firstL][secondL] == player:
                    self.cnt+=1
                else:
                    break
        except:
            return self.cnt
        
        return self.cnt
    
    
    
    # leftDownCount
    def getLeftDown(self, firstL, secondL, player):
        
        self.cnt = 0
        try:
            while True:
                firstL+=1
                secondL-=1
                if firstL > len(self.int2d)-1 or secondL < 0:
                    return self.cnt
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

        for i, val in enumerate(self.arr2d):
            for j, val in enumerate(self.arr2d):
                
                self.qpbtn = QPushButton(self)
                self.qpbtn.setGeometry(75*j, 75*i, 75, 75) # x, y, width, height
                self.qpbtn.setIconSize(QtCore.QSize(75,75))
                self.qpbtn.setIcon(self.ie)
                self.qpbtn.setWhatsThis(str(i)+","+str(j))
                self.arr2d[i][j] = self.qpbtn
                
                self.qpbtn.clicked.connect(self.clickedFunction)
            print()
         
        self.showInt2d() 
        self.resize(750,750)   
    
    
    
    
    
    
    def clickedFunction(self):
        
        if self.gameEnd == True:
            return
        
        self.location = self.sender().whatsThis().split(",")
         
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
                if self.gameResult == True:
                    self.gameEnd = True
                
                    
            elif self.playerWB == False:
                self.int2d[int(self.firstL)][int(self.secondL)] = 1
                self.playerWB = True
                self.gameResult = self.resultView(int(self.firstL), int(self.secondL), self.playerWB)
                if self.gameResult == True:
                    self.gameEnd = True
                
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
    
    
    
    
    
    
    
    
    
    
    