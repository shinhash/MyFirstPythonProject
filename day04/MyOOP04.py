



class Human:
    
    def __init__(self, nm):
        self.name = "홍길동"
        self.nm = nm
        print(self.nm + " constructor")
    
    def __del__(self):
        print(self.nm + " distruptor")

















if __name__ == "__main__":
    
    a = Human("a")
    b = Human("b")
