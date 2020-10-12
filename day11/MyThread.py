import threading, time

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += 1
        time.sleep(1)
        print("subThread", total)
    
if __name__ == "__main__":   
    t = threading.Thread(target=sum, args=(1, 20))
    t.start()
    
    print("main Thread")    
    print(chr(65))