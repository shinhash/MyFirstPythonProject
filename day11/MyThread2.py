import threading, time

       
def printChar(start, end):
    printchr = ""
    for i in range(start, end):
        printchr += chr(i)
        if i%100 == 0:
            print(printchr)
            printchr = ""
       
    
    

def printNumber(start, end):
    printnum = "";
    for i in range(start, end):
        printnum += str(i)
        if i%100 == 0:
            print(printnum)
            printnum = ""

def keyPressEvent(self, e):
    getKey = e.key()
    self.printTest(getKey)
    

def printTest(key):
    i = 1
    while True:
        print(i)
        print(key)
        i += 1
        time.sleep(1)


    
if __name__ == "__main__":   
    pNum = threading.Thread(target=printNumber, args=(1, 10000))
    pChar = threading.Thread(target=printChar, args=(1, 10000))
    PTest = threading.Thread(target=printTest, args=("d"))
    
    
#     pNum.start()
#     pChar.start()
#     PTest.start()
    
    
    print("main Thread")    
