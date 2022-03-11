import random
from words import words
word = random.choice(words)
length = len(word)
print(word)
print(f"The Word has {length} letters")
letter_lst=list(word)
print("* "*length)
inpt=["*"]*length

def allocate(index,test):
    inpt[index]=f"{test}"

for i in range(length):
    test = input("\na letter:")
    Flag= False
    while(Flag!=True):
        try:
            index = letter_lst.index(test)
        except ValueError:
            test=input("Wrong letter : ")
        else:
            Flag = True
    letter_lst[index]=""
    allocate(index,test)
    for i in range(length):
        print(inpt[i], end="")
print("\nWell Done You Found The Name :)")