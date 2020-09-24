

class Animal(object):
    
    
    def __init__(self):
        self.age = 1
        
        
    def getOrder(self):
        self.age += 1
        
        
        
class Human(Animal):
    
    
    def __init__(self):
#         Animal.__init__(self)
        super().__init__()
        self.name = "이재용"
    
    def changeName(self, name):
        self.name = name
    
        
        
        

if __name__ == "__main__":


    hum = Human()
    print(hum.name)
    hum.changeName("노승권")
    print(hum.name)
    
    
    print(hum.age)
    hum.getOrder()
    print(hum.age)














