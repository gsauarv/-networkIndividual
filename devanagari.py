from random import shuffle
from string import printable
nepali_letters =["क","ख","ग","घ","ङ","च","छ","ज","झ","ण","त","थ","द","ध","न","प","फ","ब","भ","म","य","र","ल","व","स","श","ष","ह","ञ"]
nepali_symbols=["ै","ौ","ृ","ु","ू","ि","ी","ो","ा","े"]
english_letters = list(printable)
final_maps = nepali_letters+nepali_symbols+english_letters

#keys for dict
keys = list(final_maps)
shuffleKey = list(final_maps)
shuffle(shuffleKey)

# dict for encryption
maps = dict(zip(keys,shuffleKey))
reverseMap = dict(zip(shuffleKey,keys))

def encryption(plaintext):
    cipher = []
    for letters in plaintext:
        cipher_letter = maps[letters]
        cipher.append(cipher_letter)
    ciphers = "".join(cipher)
    return cipher

def decryption(cipherText):
    plaintext = []
    for letters in cipherText:
        plain_letters = reverseMap[letters]
        plaintext.append(plain_letters)
    
    return "".join(plaintext)

from tkinter import *
root = Tk()
root.title("Encryption And Decryption")
root.geometry("500x500")
label = Label(root,text = "Enter PlainText")
label.grid(row = 0,column = 0,sticky = W)
planTextEntry = Entry(root,width = 50)
planTextEntry.grid(row=1,column = 0,ipady = 5,ipadx = 5)
def btn1():
    result = Label(root,text= "Result")
    result.grid(row = 6,column= 0,sticky =W)
    Encryptresult = Label(root,text= encryption(planTextEntry.get()))
    Encryptresult.grid(row = 7,column = 0 , sticky = W)



encryptBtn = Button(root,text = "Encrypt",width = 10,command = btn1)
encryptBtn.grid(row = 2,column = 0,sticky = W,pady = 20,ipady = 5,ipadx = 15)

label1 = Label(root,text = "Enter cipherText")
label1.grid(row = 3,column = 0,sticky = W)

cipherEntry = Entry(root,width = 50)
cipherEntry.grid(row=4,column = 0,ipady = 5,ipadx = 5)

def btn2():
    result = Label(root,text= "Result")
    result.grid(row = 6,column = 0,sticky = W)
    Decryptresult = Label(root,text= encryption(cipherEntry.get()))
    Decryptresult.grid(row = 8,column = 0 , sticky = W)

decryptBtn = Button(root,text = "Decrypt",width = 10 ,command = btn2)
decryptBtn.grid(row = 5,column = 0,sticky = W,pady = 20,ipady = 5,ipadx = 15)


root.mainloop()














