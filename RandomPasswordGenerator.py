#shkipper

import numbers
import random

SmallerCaseLetters = ['a',"b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UpperCaseLetters =   ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Numbers =            ["1","2","3","4","5","6","7","8","9"]
Symbols =            ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]","|",":",";",'"',"'","<",",",">",".","?","/",]
Password = []

BigList = [SmallerCaseLetters,UpperCaseLetters,Numbers,Symbols]

for i in range(16): #The number 16 represents the amount of characters in a password
    RandomizedList = random.choice(BigList)
    RandomizedCharacter = random.choice(RandomizedList)
    Password.append(RandomizedCharacter)

print(''.join(map(str,Password))) 