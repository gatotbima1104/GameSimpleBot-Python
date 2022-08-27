import random

def guess(x): 
    
    random_number = random.randint(1, x)
    guess=0

adverb    = input("adverb : ")
verb      = input("verb : ")
your_idol = input("what are you wanna be : ")
madlib    = f"Coding was so {adverb}! It made me so happy to {verb} it. in future \
I will be a {your_idol}"

print(madlib)

    while guess != random_number:
        guess = int (input(f"guess a Number between 1 and {x} : "))

        if guess < random_number:
            print("The number is Too low")

        elif guess > random_number:
            print("The number is Too high")

    print(f"Yeay Congrats. You have guessed the number of {random_number} correctly!!!")

guess(10)



##i developeng banget
