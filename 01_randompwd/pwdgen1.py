from decimal import ROUND_HALF_DOWN
import random
import string

flagOK = True

pwd_mode = int(input("please enter a password mode:\n1: digits only\n2: letters only\n3: digits + letters\n4: digits + letters + punctuations\n"))

if pwd_mode == 1:
    pwd_domain = string.digits
elif pwd_mode == 2:
    pwd_domain = string.ascii_letters
elif pwd_mode == 3:
    pwd_domain = string.digits + string.ascii_letters
elif pwd_mode == 4:
    pwd_domain = string.digits + string.ascii_letters + string.punctuation
else:
    print("*** error: invalid password mode !!!")
    print("*** program exits ***")
    flagOK = False


if flagOK:
    pwd_len = int(input("please enter you password length: "))

    pwd_domain_len = len(pwd_domain)
    if pwd_len > pwd_domain_len:
        pwd_len = pwd_domain_len
        print("*** warning: the password length was too long")
    elif pwd_len < 1:
        pwd_len = pwd_domain_len
        print("*** warning: the password length was invalid")
    else:
        pass
            


    pwd = random.sample(pwd_domain, pwd_len)
    pwd = "".join(pwd)
    print("\nthe password is :", pwd)
