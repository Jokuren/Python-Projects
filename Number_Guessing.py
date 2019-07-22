import random 

#Guess between 1 and 10 game.

rand = random.randrange(1,10)
guess = 0

while guess != rand:
    text = input("Guess Between 1 and 10: ")

#Turns text input into an int, and checks to see if the value is an integer and less than 1 or greater than 10, else returns an exception.
    try:
        guess = int(text)
        if (guess > 10 or guess < 1):
            raise Exception("\n The input number can't be higher than 10 or lower than 1")
    except ValueError:
        raise Exception("\n Input a number.")

#Checks to see if the inputted int is less/greater or equal to the randomly chosen number.
    if(guess < rand):
        print("Too low") 
    elif(guess > rand):
        print("Too high")
    elif (guess == rand):
        print("Correct")