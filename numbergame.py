import random
number = random.randint(1, 11)

player_name = input("Hello,What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ',Guess a number between 1 and 10:')

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('WOOOOHOOOOOO........You guessed the correct number in ' + str(number_of_guesses) + ' try!')
else:
    print('OPPPPPSSSSS.........You did not guess the wrong number, The number was ' + str(number))