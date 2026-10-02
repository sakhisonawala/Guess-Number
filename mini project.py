import random
target = random.randint(1,100)
while True:
    usernumber= (input("Guess the target or Quit(Q) :"))
    if(usernumber == "Q" or usernumber == "q"):
        break
    usernumber= int(usernumber)
    if(usernumber ==target):
        print ("SUCCESS YOU GUESSED IT RIGHT")
        break
    elif (usernumber<target):
        print("your guess is too low")
    else:
        print("your guess is too high")


print("------ GAME OVER -------")