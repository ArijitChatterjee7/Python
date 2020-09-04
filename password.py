import random
char='1234567890!@#$^&*qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
num=input("Number of passwords=")
num=int(num)
length=input("Password length=")
length=int(length)
for i in range(num):
    password=''
    for j in range(length):
        password += random.choice(char)
    print (password)
        
