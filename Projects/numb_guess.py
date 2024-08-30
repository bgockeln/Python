#Guess the Numbers Game
import random
progloop = 0
print("Guess the Number Game, enter two numbers to set the range")
a = int(input("Enter the first Number: "))
b = int(input("Enter the second Number: "))
num = random.randrange(a, b)
attempts = int(input("How many tries do you want?: "))
appts = attempts
print("Guess the number between {} and {}".format(a, b))
while progloop < attempts:
    c = int(input("Your guess: "))
    if c < num:
        print("Too low")
        progloop += 1
        appts -= 1
        print(appts, "attempts remaining")
    elif c > num:
        print("Too high")
        progloop += 1
        appts -= 1
        print(appts, "attempts remaining")
    elif c == num:
        print("Got it, you win")
        progloop = attempts
        appts -= 1

