import random
from collections import Counter

#Rolls a six sided die.

end = "e"
start = True
roll = "r"

while start == True:
      text = input("Type in 'r' to roll the die or 'e' to stop: ")

      assert(text == roll or text == end), "\n Type in either 'r' to roll or 'e' to stop " 

      if text == roll:
              print(random.randrange(1,7)) #The range is between 1-7 because the very last number (7) isn't accounted for.

      elif (text == end):
              start = False