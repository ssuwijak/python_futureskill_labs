import string
import random
import string
import tkinter as tk
import pyperclip as pc
"""
def gen_pwd():
    txt_pwd.delete(0, tk.END)
    len = pwd_len.get()
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    sym = string.punctuation
    
    mode0 = lower
    mode1 = lower + upper
    mode2 = mode1 + num
    mode3 = mode2 + sym
    
    pwd = ""
    
    i = pwd_mode.get()
    if i == 0:
        mode0 = mode1
    elif i == 1:
        mode0 = mode2
    elif i == 2:
        mode0 = mode3
        
    for i in range(len):
        pwd = pwd + random.choice(mode0)
        
    txt_pwd.insert(0, pwd)
    
def copy_pwd():
    pwd = txt_pwd.get()
    pc.copy(pwd)
    
"""

root = tk.Tk()

pwd_len = tk.IntVar()
pwd_mode = tk.IntVar()

root.title("Random Password Generator")

fra_pwd_len = tk.LabelFrame(root, text = "Password Length")
fra_pwd_len.grid(column=0, row=0, padx=5, pady=5)

lbl_pwd_len = tk.Label(fra_pwd_len, text = "Password Length :").grid(row = 0, column = 0)
spn_pwd_len = tk.Spinbox(fra_pwd_len, from_ = 6, to = 15, textvariable = pwd_len).grid(row = 0, column = 1)


fra_pwd_mode = tk.LabelFrame(root, text = "Password Strength")
fra_pwd_len.grid(column=0, row=1, padx=5, pady=5)

# lbl_pwd_mode = tk.Label(root, text = "Password Strength :").grid(row = 0, column = 2)
rad_pwd_mode1 = tk.Radiobutton(fra_pwd_mode, text = "Low", variable = pwd_mode, value = 0).grid(row = 1, column = 0)
rad_pwd_mode2 = tk.Radiobutton(fra_pwd_mode, text = "Medium", variable = pwd_mode, value = 1).grid(row = 1, column = 1)
rad_pwd_mode3 = tk.Radiobutton(fra_pwd_mode, text = "High", variable = pwd_mode, value = 2).grid(row = 1, column = 2)

#lbl_pwd = tk.Label(root, text = "Password :").grid(row = 2, column = 0)
#txt_pwd = tk.Entry(root) #.grid(row = 1, column = 1)
#txt_pwd.grid(row = 2, column = 1)

#btn_pwd = tk.Button(root, text = "Generate Password", command = gen_pwd).grid(row = 2, column = 2)
#btn_copy = tk.Button(root, text = "Copy Password", command = copy_pwd).grid(row = 2, column = 3)

root.mainloop()

quit()
