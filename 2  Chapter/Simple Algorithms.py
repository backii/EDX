import random



#################
"""
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
"""

##### Secret number #####


print("Please think of a number between 0 and 100!")


answer = ""
low = 0
high = 100

computer_guess = int((low + high)/2)

while not False:

    print("Is your secret number", str(computer_guess) + "?")
    answer = input("Enter 'h' to indicate the guess is too high."
                   "Enter 'l' to indicate the guess is too low. "
                   "Enter 'c' to indicate I guessed correctly. ")
    if answer is "l":
        low = computer_guess
    elif answer is "h":
        high = computer_guess
    elif answer is "c":
        break
    else:
        print("Sorry, I did not understand your input")

    computer_guess = int((low+high)/2)


print("Game over. Your secret number was:", computer_guess)