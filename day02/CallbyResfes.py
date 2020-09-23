

def increate(a):
    a += 1

def increateRef(a):
    a[0] += 1
    
    
a = 1
b = [3]
print(a)
print(b)




increate(a)
increateRef(b)
print(a)
print(b)
