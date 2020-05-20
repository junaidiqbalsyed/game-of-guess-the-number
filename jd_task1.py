import random


game = " "

while game == " ":
    game = int(input("Enter the number of games you wanna play "))


for g in range (0, game):
    number = random.randint(0,25)
    attempt = 0
    

    while True:
        guess =  int(input("guess the number  "))
        if guess > number:
            attempt = attempt+1
            print("choose a smaller number")
        elif guess < number:
            attempt = attempt+1
            print("choose a larger number")     
        elif guess == number:
            attempt = attempt+1
            print(f'Correct! the number was {number}  and number of attmpts are {attempt} ')
            break
