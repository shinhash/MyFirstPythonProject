
import random

userbang = ""
combang = ""
result = ""

com = random.randint(1, 2)
user = input("홀,짝 : ")

userbang = user

if com == 1:
    combang = "홀"
else:
    combang = "짝"

if userbang.__eq__(combang):
    result = "you win!!"
else:
    result = "you lose"


print(userbang)
print(combang)
print(result)
