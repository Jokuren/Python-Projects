#Program that takes in 3 int inputs, first two determine the range and the last one is the max count.
#Randomly chooses ints within said range and checks which one reaches the max count first.

import random
from collections import Counter
import keyboard

list = []
n_gen = False
val_correct = False

text = input("Enter the starting number: ")
text2 = input ("Enter the last number: ")
text3 = input ("Enter the max count you want to see: ")

#Turns all text inputs into ints and checks to see if the first two numbers given are equal.
try:
    n = int(text)
    n2 = int(text2)
    n3 = int(text3) #Turned into an int to avoid infinite loop.
    if(n < n2):
        val_correct = True
    else:
        print("\n The starting number can't be greater or equal to the range's last number.")

except ValueError:
    print("\n All inputs must be numbers.")


while n_gen == False and val_correct == True:
    rando = random.randrange(n, n2 + 1) #Adds + 1 to n2 because the very last number is always omitted.
    list.append(rando)
    cnt = Counter(list).most_common(1)
    print ("\n Random number: ", rando,"\n Current List of numbers:", list,"\n Current number with highest count: ", cnt)
    cnt = "".join(map(str, cnt)) #Turns cnt into a string.

    for _ in cnt:
        if (", " + str(n3) in cnt): #n3 is turned back into a string and ", " is added before it so that it can read only the count amount.
            n_gen = True

# Allows you to view the value that reached the max count first and then exit on your own.
print ("\n Press the 'Enter' key to exit.")
keyboard.wait("Enter")
