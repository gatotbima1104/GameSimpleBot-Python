
import random
def computer_magic(x):
    low = 1
    high = x
    magic = ''

    while magic != 'r':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        magic = input(f'Is {guess} too Low (l), too High (h), or Right (r) ?? ').lower()
        if magic == 'l':
            low = guess + 1
        elif magic == 'h':
            high = guess - 1

    print (f'Yeay The computer has guessed your number {guess} correclty!!!')

computer_magic(100)

''' The Number which will be guessed is 199'''
    
    