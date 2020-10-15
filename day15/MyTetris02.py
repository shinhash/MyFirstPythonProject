import sys

from PyQt5 import uic
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic.Compiler.qtproxies import QtWidgets, QtGui

from day15.MyTetris import scren2D

from day15.Block import Block

form_class = uic.loadUiType("tetris.ui")[0]

class WindowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.block2D = []
        self.stack2D = []
        self.scren2D = []
        self.palete = []
        
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
                self.palete[y][x] = self.lbl
                 
        self.myRender()
        
        
    
        
        
    def keyPressEvent(self, e):
        
        x = Block.xloc
        y = Block.yloc
        
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Up:
            Block.yloc -= 1
            
        elif e.key() == Qt.Key_Down:
            Block.yloc += 1
            
        elif e.key() == Qt.Key_Left:
            Block.xloc -= 1
            
        elif e.key() == Qt.Key_Right:
            Block.xloc += 1        
        
        
        if Block.xloc < 0:
            Block.xloc = x
            
        try:
            self.setBlock2DWithBlock()
            self.moveStackBlock2Scrin()
        except:
            Block.xloc = x
            Block.yloc = y
            
            self.setBlock2DWithBlock()
            self.moveStackBlock2Scrin()
            
        self.print2D(self.scren2D)
        self.myRender()
            
            
            
            

    def print2D(self, arr):
        for line in arr:
            print(line)        
        
        
    def setBlock2DWithBlock(self):
        print("==============================")
        print(Block.yloc, ",", Block.xloc)
        
        for y, val in enumerate(self.scren2D):
            for x, val in enumerate(self.scren2D[y]):
                self.block2D[y][x] = 0
                self.scren2D[y][x] = self.block2D[y][x] + self.stack2D[y][x]
        
        if Block.kind == 1:
            self.block2D[Block.yloc][Block.xloc] = Block.kind
            self.block2D[Block.yloc][Block.xloc+1] = Block.kind
            self.block2D[Block.yloc+1][Block.xloc] = Block.kind
            self.block2D[Block.yloc+1][Block.xloc+1] = Block.kind
             
        if Block.kind == 2:
            self.block2D[Block.yloc][Block.xloc] = Block.kind  
                   
        if Block.kind == 3:
            self.block2D[Block.yloc][Block.xloc] = Block.kind
             
        if Block.kind == 4:
            self.block2D[Block.yloc][Block.xloc] = Block.kind
             
        if Block.kind == 5:
            self.block2D[Block.yloc][Block.xloc] = Block.kind
             
        if Block.kind == 6:
            self.block2D[Block.yloc][Block.xloc] = Block.kind
             
        if Block.kind == 7:
            self.block2D[Block.yloc][Block.xloc] = Block.kind
            
    
        
        
        
        
        
    def initBlockStackScren2D(self):
        for i in range(20):
            self.block2D.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.stack2D.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.scren2D.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            
            self.temp = []
            for j in range(10):
                self.temp.append(QLabel(self))
                
            self.palete.append(self.temp)



    
    
    def moveStackBlock2Scrin(self):
        for y, val in enumerate(self.scren2D):
            for x, val in enumerate(self.scren2D[y]):
                self.scren2D[y][x] = self.block2D[y][x] + self.stack2D[y][x]
    

    def myRender(self):
        for y, val in enumerate(self.scren2D):
            for x, val in enumerate(self.scren2D[y]):
                
                if self.scren2D[y][x] == 0:
                    self.palete[y][x].setStyleSheet("background-color: #666666;")
                    
                if self.scren2D[y][x] == 1:
                    self.palete[y][x].setStyleSheet("background-color: #FF0000;")
    
                if self.scren2D[y][x] == 2:
                    self.palete[y][x].setStyleSheet("background-color: #FF6600;")
    
                if self.scren2D[y][x] == 3:
                    self.palete[y][x].setStyleSheet("background-color: #FFFF00;")
    
                if self.scren2D[y][x] == 4:
                    self.palete[y][x].setStyleSheet("background-color: #00FF00;")
    
                if self.scren2D[y][x] == 5:
                    self.palete[y][x].setStyleSheet("background-color: 0#000FF;")

                if self.scren2D[y][x] == 6:
                    self.palete[y][x].setStyleSheet("background-color: #00FFFF;")

                if self.scren2D[y][x] == 7:
                    self.palete[y][x].setStyleSheet("background-color: #FF0099;")
                    
                if self.scren2D[y][x] == 11:
                    self.palete[y][x].setStyleSheet("background-color: #660000;")
                    
                if self.scren2D[y][x] == 12:
                    self.palete[y][x].setStyleSheet("background-color: #CC3300;")
                
                if self.scren2D[y][x] == 13:
                    self.palete[y][x].setStyleSheet("background-color: #996600;")
                
                if self.scren2D[y][x] == 14:
                    self.palete[y][x].setStyleSheet("background-color: #003300;")
                
                if self.scren2D[y][x] == 15:
                    self.palete[y][x].setStyleSheet("background-color: #000066;")
                    
                if self.scren2D[y][x] == 16:
                    self.palete[y][x].setStyleSheet("background-color: #006666;")
                    
                if self.scren2D[y][x] == 17:
                    self.palete[y][x].setStyleSheet("background-color: #660033;")
                    
                    
                    
                    
                    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    
    
    
    
    