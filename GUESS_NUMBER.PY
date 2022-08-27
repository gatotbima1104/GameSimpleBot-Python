import random

def guess(x): 
    
    random_number = random.randint(1, x)
    guess=0


    while guess != random_number:
        guess = int (input(f"guess a Number between 1 and {x} : "))

        if guess < random_number:
            print("The number is Too low")

        elif guess > random_number:
            print("The number is Too high")

    print(f"Yeay Congrats. You have guessed the number of {random_number} correctly!!!")

guess(10)


##ini develops
