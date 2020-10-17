import sys, time, threading
from threading import Timer

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore  # QtCore를 명시적으로 보여주기 위해



from PyQt5 import uic
from PyQt5.Qt import Qt, QThread
from PyQt5.QtWidgets import *
from PyQt5.uic.Compiler.qtproxies import QtWidgets, QtGui

from day15.MyTetris import scren2D

from day16.Block import Block
from sys import excepthook
from skimage.viewer.qt import QtCore

form_class = uic.loadUiType("tetris.ui")[0]

class WindowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.block2D = []
        self.stack2D = []
        self.scren2D = []
        self.lbl2D = []
        
        self.block = Block()
        
        
        self.initBlockStackScren2D()
        
        self.stack2D[19][0] = 17
        self.stack2D[19][1] = 17
        self.stack2D[19][2] = 17       
        self.stack2D[19][3] = 17
        
        self.setBlock2DWithBlock()
        self.moveStackBlock2Scrin()
        self.print2D(self.scren2D)
        
        for y, val in enumerate(self.scren2D):
            for x, val in enumerate(self.scren2D[y]):
                self.lbl = QLabel(self)
                self.lbl.setGeometry(31*x, 31*y, 30, 30)
                self.lbl2D[y][x] = self.lbl
                 
        self.myRender()
        
        myThread = threading.Thread(target=self.autoDownAction, args=())
#         myThread.daemon()
#         myThread.start()
        

    def print2D(self, arr):
        for line in arr:
            print(line)        
        
        
        
    def setBlock2DWithBlock(self):
        print("==============================")
        print(self.block.yloc, ",", self.block.xloc)
        
        for y, val in enumerate(self.scren2D):
            for x, val in enumerate(self.scren2D[y]):
                self.block2D[y][x] = 0
                self.scren2D[y][x] = self.block2D[y][x] + self.stack2D[y][x]
        
        
        
        if self.block.kind == 1:
            self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
            self.block2D[self.block.yloc][self.block.xloc+1] = self.block.kind
            self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
            self.block2D[self.block.yloc+1][self.block.xloc+1] = self.block.kind
              
              
              
        if self.block.kind == 2:
            if self.block.status == 1:
                self.block2D[self.block.yloc-1][self.block.xloc] = self.block.kind  
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind  
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind  
                self.block2D[self.block.yloc+2][self.block.xloc] = self.block.kind 
                 
            if self.block.status == 2:
                self.block2D[self.block.yloc][self.block.xloc+1] = self.block.kind  
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind  
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind  
                self.block2D[self.block.yloc][self.block.xloc-2] = self.block.kind 
                    
                    
        if self.block.kind == 3:
            if self.block.status == 1:
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc+1] = self.block.kind
                 
            if self.block.status == 2:
                self.block2D[self.block.yloc-1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc-1] = self.block.kind
              
              
              
        if self.block.kind == 4:
            if self.block.status == 1:
                self.block2D[self.block.yloc][self.block.xloc+1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc-1] = self.block.kind
                 
            if self.block.status == 2:
                self.block2D[self.block.yloc-1][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
                 
                 
                 
                 
              
        if self.block.kind == 5:
            if self.block.status == 1:
                self.block2D[self.block.yloc-1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc+1] = self.block.kind
                 
            if self.block.status == 2:
                self.block2D[self.block.yloc-1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc+1] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
                 
            if self.block.status == 3:
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc+1] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
                 
            if self.block.status == 4:
                self.block2D[self.block.yloc-1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
            
        
             
        if self.block.kind == 6:
            if self.block.status == 1:
                self.block2D[self.block.yloc-1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc+1] = self.block.kind
                
            elif self.block.status == 2:
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc+1] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc-1] = self.block.kind
                
            elif self.block.status == 3:
                self.block2D[self.block.yloc-1][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc-1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
                
            elif self.block.status == 4:
                self.block2D[self.block.yloc-1][self.block.xloc+1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc+1] = self.block.kind
                
         
             
        if self.block.kind == 7:
            if self.block.status == 1:
                self.block2D[self.block.yloc-1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc-1] = self.block.kind
                 
            if self.block.status == 2:
                self.block2D[self.block.yloc-1][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc+1] = self.block.kind
                 
            if self.block.status == 3:
                self.block2D[self.block.yloc-1][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc-1][self.block.xloc+1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc] = self.block.kind
                 
            if self.block.status == 4:
                self.block2D[self.block.yloc][self.block.xloc-1] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc] = self.block.kind
                self.block2D[self.block.yloc][self.block.xloc+1] = self.block.kind
                self.block2D[self.block.yloc+1][self.block.xloc+1] = self.block.kind
                
        
        
    def initBlockStackScren2D(self):
        for i in range(20):
            self.block2D.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.stack2D.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.scren2D.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            
            self.temp = []
            for j in range(10):
                self.temp.append(QLabel(self))
                
            self.lbl2D.append(self.temp)



    
    
    def moveStackBlock2Scrin(self):
        for y, val in enumerate(self.scren2D):
            for x, val in enumerate(self.scren2D[y]):
                self.scren2D[y][x] = self.block2D[y][x] + self.stack2D[y][x]
    
    
    
    

    def myRender(self):
        for y, val in enumerate(self.scren2D):
            for x, val in enumerate(self.scren2D[y]):
                
                if self.scren2D[y][x] == 0:
                    self.lbl2D[y][x].setStyleSheet("background-color: gray;")
                    
                if self.scren2D[y][x] == 1:
                    self.lbl2D[y][x].setStyleSheet("background-color: #FF0000;")
    
                if self.scren2D[y][x] == 2:
                    self.lbl2D[y][x].setStyleSheet("background-color: #eF6600;")
    
                if self.scren2D[y][x] == 3:
                    self.lbl2D[y][x].setStyleSheet("background-color: #dFFF00;")
    
                if self.scren2D[y][x] == 4:
                    self.lbl2D[y][x].setStyleSheet("background-color: #c0FF00;")
    
                if self.scren2D[y][x] == 5:
                    self.lbl2D[y][x].setStyleSheet("background-color: #b000FF;")

                if self.scren2D[y][x] == 6:
                    self.lbl2D[y][x].setStyleSheet("background-color: #a0FFFF;")

                if self.scren2D[y][x] == 7:
                    self.lbl2D[y][x].setStyleSheet("background-color: #9F0099;")
                    
                    
                    
                if self.scren2D[y][x] == 11:
                    self.lbl2D[y][x].setStyleSheet("background-color: #660000;")
                    
                if self.scren2D[y][x] == 12:
                    self.lbl2D[y][x].setStyleSheet("background-color: #CC3300;")
                
                if self.scren2D[y][x] == 13:
                    self.lbl2D[y][x].setStyleSheet("background-color: #996600;")
                
                if self.scren2D[y][x] == 14:
                    self.lbl2D[y][x].setStyleSheet("background-color: #003300;")
                
                if self.scren2D[y][x] == 15:
                    self.lbl2D[y][x].setStyleSheet("background-color: #000066;")
                    
                if self.scren2D[y][x] == 16:
                    self.lbl2D[y][x].setStyleSheet("background-color: #006666;")
                    
                if self.scren2D[y][x] == 17:
                    self.lbl2D[y][x].setStyleSheet("background-color: #660033;")
      
        
    def isCollisionFunc(self):
        
        isCrash = False
        for y, val in enumerate(self.scren2D):
            for x, val in enumerate(self.scren2D[y]):
                blockTemp = self.block2D[y][x]
                stackTemp = self.stack2D[y][x]
                if blockTemp != 0 and stackTemp != 0:
                    isCrash = True
                    return isCrash
        return isCrash
    
    
    
    
    def moveBlockToStack2D(self):
        for y, val in enumerate(self.block2D):
            for x, val in enumerate(self.block2D[y]):
                if self.block2D[y][x] > 0:
                    self.stack2D[y][x] = self.block2D[y][x] + 10
     
    
    
    
    def getNotFullStack(self):
        stackTemp = []
        for i, val in enumerate(self.stack2D):
            temp = self.stack2D[i]
            if temp[0] > 0 and temp[1] > 0 and temp[2] > 0 and temp[3] > 0 and temp[4] > 0 and temp[5] > 0 and temp[6] > 0 and temp[7] > 0 and temp[8] > 0 and temp[9] > 0:
                pass
            else:
                strLine = ""
                strLine += str(temp[0]) + ","
                strLine += str(temp[1]) + ","
                strLine += str(temp[2]) + ","
                strLine += str(temp[3]) + ","
                strLine += str(temp[4]) + ","
                strLine += str(temp[5]) + ","
                strLine += str(temp[6]) + ","
                strLine += str(temp[7]) + ","
                strLine += str(temp[8]) + ","
                strLine += str(temp[9])

                stackTemp.append(strLine)
        return stackTemp

    
    
    def blockSpin(self):
        if self.block.kind == 2 or self.block.kind == 3 or self.block.kind == 4:
            if self.block.status == 1:
                self.block.status = 2
            
            elif self.block.status == 2:
                self.block.status = 1
        
        
        if self.block.kind == 5 or self.block.kind == 6 or self.block.kind == 7:
            if self.block.status == 1:
                self.block.status = 2
                
            elif self.block.status == 2:
                self.block.status = 3
                
            elif self.block.status == 3:
                self.block.status = 4
                
            elif self.block.status == 4:
                self.block.status = 1



    def autoDownAction(self):
        while True:
            self.realTimeAction(Qt.Key_Down, "autoDown")
            time.sleep(1)
            


    def keyPressEvent(self, e):
        getKey = e.key()
        comes = "key"
        self.realTimeAction(getKey, comes)
               
              
              
                    
    def realTimeAction(self, key, comes):
#         self.update()
        self.repaint()
        status = self.block.status
        x = self.block.xloc
        y = self.block.yloc
        flagColBound = False
        flagDown = False
        
        if key == Qt.Key_Escape:
            self.close()
            
        if key == Qt.Key_Up:
            self.blockSpin()
         
        if key == Qt.Key_Down:
            self.block.yloc += 1
            flagDown = True
             
        if key == Qt.Key_Left:
            self.block.xloc -= 1
              
        if key == Qt.Key_Right:
            self.block.xloc += 1        
        
        try:
            self.setBlock2DWithBlock()
            
            
            if self.block.kind == 2:
                if self.block.xloc == -1:  
                    raise Exception
                else:
                    if self.block2D[0][0] == self.block.kind and self.block2D[0][9] == self.block.kind:
                        raise Exception
                    if self.block2D[1][0] == self.block.kind and self.block2D[1][9] == self.block.kind:
                        raise Exception
                    if self.block2D[2][0] == self.block.kind and self.block2D[2][9] == self.block.kind:
                        raise Exception
                    if self.block2D[3][0] == self.block.kind and self.block2D[3][9] == self.block.kind:
                        raise Exception
                    if self.block2D[4][0] == self.block.kind and self.block2D[4][9] == self.block.kind:
                        raise Exception
                    if self.block2D[5][0] == self.block.kind and self.block2D[5][9] == self.block.kind:
                        raise Exception
                    if self.block2D[6][0] == self.block.kind and self.block2D[6][9] == self.block.kind:
                        raise Exception
                    if self.block2D[7][0] == self.block.kind and self.block2D[7][9] == self.block.kind:
                        raise Exception
                    if self.block2D[8][0] == self.block.kind and self.block2D[8][9] == self.block.kind:
                        raise Exception
                    if self.block2D[9][0] == self.block.kind and self.block2D[9][9] == self.block.kind:
                        raise Exception
                    if self.block2D[10][0] == self.block.kind and self.block2D[10][9] == self.block.kind:
                        raise Exception                       
                    if self.block2D[11][0] == self.block.kind and self.block2D[11][9] == self.block.kind:
                        raise Exception                       
                    if self.block2D[12][0] == self.block.kind and self.block2D[12][9] == self.block.kind:
                        raise Exception                       
                    if self.block2D[13][0] == self.block.kind and self.block2D[13][9] == self.block.kind:
                        raise Exception                       
                    if self.block2D[14][0] == self.block.kind and self.block2D[14][9] == self.block.kind:
                        raise Exception                       
                    if self.block2D[15][0] == self.block.kind and self.block2D[15][9] == self.block.kind:
                        raise Exception                       
                    if self.block2D[16][0] == self.block.kind and self.block2D[16][9] == self.block.kind:
                        raise Exception                       
                    if self.block2D[17][0] == self.block.kind and self.block2D[17][9] == self.block.kind:
                        raise Exception                       
                    if self.block2D[18][0] == self.block.kind and self.block2D[18][9] == self.block.kind:
                        raise Exception                       
                    if self.block2D[19][0] == self.block.kind and self.block2D[19][9] == self.block.kind:
                        raise Exception                                                 
                
            else:
                if self.block2D[0][0] == self.block.kind and self.block2D[0][9] == self.block.kind:
                    raise Exception
                if self.block2D[1][0] == self.block.kind and self.block2D[1][9] == self.block.kind:
                    raise Exception
                if self.block2D[2][0] == self.block.kind and self.block2D[2][9] == self.block.kind:
                    raise Exception
                if self.block2D[3][0] == self.block.kind and self.block2D[3][9] == self.block.kind:
                    raise Exception
                if self.block2D[4][0] == self.block.kind and self.block2D[4][9] == self.block.kind:
                    raise Exception
                if self.block2D[5][0] == self.block.kind and self.block2D[5][9] == self.block.kind:
                    raise Exception
                if self.block2D[6][0] == self.block.kind and self.block2D[6][9] == self.block.kind:
                    raise Exception
                if self.block2D[7][0] == self.block.kind and self.block2D[7][9] == self.block.kind:
                    raise Exception
                if self.block2D[8][0] == self.block.kind and self.block2D[8][9] == self.block.kind:
                    raise Exception
                if self.block2D[9][0] == self.block.kind and self.block2D[9][9] == self.block.kind:
                    raise Exception
                if self.block2D[10][0] == self.block.kind and self.block2D[10][9] == self.block.kind:
                    raise Exception                       
                if self.block2D[11][0] == self.block.kind and self.block2D[11][9] == self.block.kind:
                    raise Exception                       
                if self.block2D[12][0] == self.block.kind and self.block2D[12][9] == self.block.kind:
                    raise Exception                       
                if self.block2D[13][0] == self.block.kind and self.block2D[13][9] == self.block.kind:
                    raise Exception                       
                if self.block2D[14][0] == self.block.kind and self.block2D[14][9] == self.block.kind:
                    raise Exception                       
                if self.block2D[15][0] == self.block.kind and self.block2D[15][9] == self.block.kind:
                    raise Exception                       
                if self.block2D[16][0] == self.block.kind and self.block2D[16][9] == self.block.kind:
                    raise Exception                       
                if self.block2D[17][0] == self.block.kind and self.block2D[17][9] == self.block.kind:
                    raise Exception                       
                if self.block2D[18][0] == self.block.kind and self.block2D[18][9] == self.block.kind:
                    raise Exception                       
                if self.block2D[19][0] == self.block.kind and self.block2D[19][9] == self.block.kind:
                    raise Exception
                    
        except:
            flagColBound = True
            print("Except!!")
            
        
        
        self.moveStackBlock2Scrin()

        isCollision = self.isCollisionFunc()
        print("충돌 = " + str(isCollision))
        
        print("comes = " + comes)
        
        
         
        if isCollision == True or flagColBound == True:
            self.block.status = status
            self.block.xloc = x 
            self.block.yloc = y 
            self.setBlock2DWithBlock() # block2D reset
            self.moveStackBlock2Scrin() # stack 데이터를 scrin에 저장
              
            if flagDown == True:
                self.moveBlockToStack2D()
                
                notFullStack = self.getNotFullStack()
                FullStackCnt = len(self.block2D) - len(notFullStack)
                print()
                print("===================================")
                print("FullStackCnt = " + str(FullStackCnt))
                print("===================================")
                
                for temp in range(FullStackCnt):
                    notFullStack.insert(temp, "0,0,0,0,0,0,0,0,0,0")
                for newStack in notFullStack:
                    pass
#                     print(newStack)
                print("===================================")
                    
                for y in range(len(self.stack2D)):
                    stackLine = notFullStack[y]
                    stackTemp = stackLine.split(",")
                    for x in range(len(self.stack2D[y])):
                        self.stack2D[y][x] = int(stackTemp[x])
#                     print(stackLine)
                print("===================================")
                
                
                self.block.__init__()
                self.setBlock2DWithBlock() # block2D reset
                self.moveStackBlock2Scrin() # stack 데이터를 scrin에 저장
                flagDown = False
            
        
        self.myRender()                
        self.print2D(self.scren2D)
            
                    
                    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    
    
    
    
    
