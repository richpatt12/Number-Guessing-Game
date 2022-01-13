import random
#Declares random number between 1-10
random_number = random.randint(1,10)
#Asks user for name
print("Hey how are you, What's your name?")
#User input Name and prints it
name = input('')

print(f'Hey {name} lets play a game. I am guessing a number between 1-10')
#declares guess variable 
guess = ''
guess_total=''
while guess != random_number:
    
    guess = int(input('Enter your random number: '))
    
    if guess < random_number:
        print(f'Sorry {guess} is too low')
    elif guess > random_number: 
        print(f'Sorry {guess} is too high')
    else:
        print('You got it!')
        print(f'It took you {guess_total} tries')
#next step count the users guesses
input()
