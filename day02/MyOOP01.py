

class Unit(object):

    tribe = ""      # 종족
    name = ""       # 이름
    hp = 0;         # 체력
    attck = 0;      # 공격력
    
    
    def __init__(self):
        self.result = 0
        
        
        
    def setTribe(self, tribe):
        self.tribe = tribe
    def getTribe(self):
        return self.tribe    
    
    
    
    
    def setHP(self, hp):
        self.hp = hp
    def getHP(self):
        return self.hp
        
        
        
        
        
    def setAttack(self, attck):
        self.attck = attck
    def getAttack(self):
        return self.attck
        
        
        
        

class Marin(Unit):
    
    def __init__(self):
        pass
  
    def setName(self, name):
        self.name = name
        
        
        


class Jurge(Unit):
    
    def __init__(self):
        pass
  
    def setName(self, name):
        self.name = name
        
        
        

class Teran(Unit):
    
    def __init__(self):
        pass
  
    def setName(self, name):
        self.name = name






unit1 = Marin()
unit2 = Jurge()

unit1.setTribe("인간")
unit1.setHP(100)
unit1.setAttack(15)


unit2.setTribe("저그")
unit2.setHP(250)
unit2.setAttack(20)



print(unit1.getTribe())
print(unit2.getTribe())

