from random import *

class Block():
    
    def __init__(self):
        
#         self.kind = randint(1, 7)
        self.kind = 7
        self.status = 1
        self.xloc = 4
        self.yloc = 2


    def __str__(self):
        return "kind = " + str(self.kind) + ", status = " + str(self.status) + ", x = " + str(self.xloc) + ", y = " + str(self.yloc)
        