import numpy as np
data = np.load('x_train.npy')
# print(data)

count = 0
strItem = []

for item in data:
    print("=================================================================")
    for textline in item:
        strItem = []
        for text in textline:
        
            if text >= 1:
                text = "X"
            else:
                text = " "
            strItem.append(text)
            print(text, end=", ")
#         strItem.append("\n")
#         print(strItem)
        print()
    print()
    
        