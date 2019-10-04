#Program that takes in 2 int inputs, first int determines the range and the last one is the max count.
#Randomly chooses ints within said range and checks which one reaches the max count first.

import random
from collections import Counter

list = []
n_gen = False
val_correct = False
text_r = False
reset = False

while text_r == False:
    if reset == False:      
        text = input ("Enter number: ")
        text2 = input ("Enter the max count you want to see: ")
        n = int(text)
        n2 = int(text2) #Turned into an int to avoid infinite loop.
    
    while n_gen == False:
        rando = random.randrange(1, n + 1) #Adds + 1 to n because the very last number is always omitted.
        list.append(rando)
        cnt = Counter(list).most_common(1)
        #print ("\n Random number: ", rando,"\n Current List of numbers:", list,"\n Current number with highest count: ", cnt)
        cnt = "".join(map(str, cnt)) #Turns cnt into a string.

        for _ in cnt:
            if (", " + str(n2) in cnt): #n2 is turned back into a string and ", " is added before it so that it can read only the count amount.
                n_gen = True
                text_r = True
                list = []
    print ("\n Random number: ", rando,"\n Number with highest count: ", cnt)
    text3 = input("Press 'e' to exit, 'r' to do it again with the same number or 'n' to do it again with a new number: ")
    if text3.lower() in {'e'}:
        text_r = True
    elif text3.lower() in {'r'}:
        text_r = False
        n_gen = False
        reset = True
    elif text3.lower() in {'n'}:
        text_r = False
        n_gen = False
        reset = False
            