import random
from words import words
from hangman_visual import lives_visual_dict
word = random.choice(words)
length = len(word)
#print(word)
#print(f"The Word has {length} letters")
letter_lst=list(word)
print("* "*length)
inpt=["*"]*length
lives=7
Lose_Flag=False
def allocate(index,test):
    inpt[index]=f"{test}"

print(lives_visual_dict[lives])
for i in range(length):
    test = input("\na letter:")
    Flag= False
    while(Flag!=True and lives > 0):
        try:
            index = letter_lst.index(test)
        except ValueError:
            test = input(f"Wrong letter ({lives} lives left): ")
            lives = lives - 1
            print(lives_visual_dict[lives])
        else:
            Flag = True
        if (lives==0):
            break
    if (lives==0):
        Lose_Flag=True
        break
    letter_lst[index]=""
    allocate(index,test)
    for i in range(length):
        print(inpt[i], end="")
if (Lose_Flag==True):
    print("You Lost The Man Has died")
else:
    print("\nWell Done You Found The Name :), The Man was released")
