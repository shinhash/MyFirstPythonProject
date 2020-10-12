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
        


    
if __name__ == "__main__":   
    pNum = threading.Thread(target=printNumber, args=(1, 10000))
    pChar = threading.Thread(target=printChar, args=(1, 10000))
    
    
    pNum.start()
    pChar.start()
    
    print("main Thread")    
