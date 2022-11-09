from decimal import ROUND_HALF_DOWN
import random
import string

def passwordGenerator(pwd_len, pwd_mode):
    flagOK = True

    if pwd_mode == 1:
        chars = string.digits
    elif pwd_mode == 2:
        chars = string.ascii_letters
    elif pwd_mode == 3:
        chars = string.digits + string.ascii_letters
    elif pwd_mode == 4:
        chars = string.digits + string.ascii_letters + string.punctuation
    else:
        print("*** error: invalid password mode !!!")
        flagOK = False
        return None

    if flagOK:
        chars_len = len(chars)
        if pwd_len > chars_len:
            pwd_len = chars_len
            print("*** warning: the password length was too long")
           
        pwd = random.sample(chars, pwd_len)
        pwd = "".join(pwd)         
        
        return pwd

while True:  
    pwd_mode = int(input("please enter a password mode:\n1: digits only\n2: letters only\n3: digits + letters\n4: digits + letters + punctuations\n"))
    pwd_len = int(input("please enter you password length: "))
    pwd = passwordGenerator(pwd_len, pwd_mode)
    print("\nthe password is :", pwd)
    ans = input("do you want to run again ? (y/n) : ")
    if ans == "n" or ans == "N":
        break