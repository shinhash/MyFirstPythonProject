
import random


user = ""
com = ""
result = ""


user = input("가위바위보 시작 : \n")
comprocess = random.randint(1, 4)



if comprocess == 1:
    com = "가위"
elif  comprocess == 2:
    com = "바위"
elif comprocess == 3:
    com = "보"
    
if com == user:
    result = "비겼습니다."
elif (com == "가위" and user == "바위") or (com == "보" and user == "가위") or (com == "바위" and user == "보"):
    result = "이겼습니다."
elif (com == "가위" and user == "보") or (com == "보" and user == "바위") or (com == "바위" and user == "가위"):
    result = "졌습니다."

print("컴퓨터 : {}, 유저 : {}, 결과 : {}".format(com, user, result))




    