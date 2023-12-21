import random
import math

Upper = int(input("Enter the upper number:"))
Lower = int(input("Enter the lower number:"))

x = random.randint(Lower,Upper)
print("\n You have only ", round(math.log(Upper - Lower +1, 2)), "chances to guess the number.")

count = 0

while count < math.log(Upper - Lower + 1, 2):
    count+=1


    guess = int(input("Guess a number:"))

    if x == guess:
        print("Congratulation!, You got it correct.")
        break
    elif x > guess:
        print("You guessed it too small.")
    elif x < guess:
        print("You guessed it too large.")

    if count > math.log(Upper - Lower + 1, 2):
        print("The number is:",x)
        print("\tBetter luck next time.")