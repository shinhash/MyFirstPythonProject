

class Animal(object):
    
    
    def __init__(self):
        self.age = 0
        
    def order(self):
        self.age += 1



class Bird(object):
    
    def __init__(self):
        self.flyWidth = 5
    
    def fly(self, flyWidth):
        self.flyWidth += flyWidth



        
class Human(Bird,Animal):
    
    def __init__(self):
        Bird.__init__(self)
        Animal.__init__(self)
    
    
    def getFlyWidth(self):
        print("flywidth : {}".format(self.flyWidth))

    
    def getAge(self):
        print("age : {}".format(self.age))
    





if __name__ == "__main__":
    person = Human()
    
    
    person.getAge()
    person.getFlyWidth()
    
    
    
    
    person.order()
    person.fly(5)

    person.getAge()
    person.getFlyWidth()
    
    
    
    
    person.order()
    person.fly(15)
    
    person.getAge()
    person.getFlyWidth()







