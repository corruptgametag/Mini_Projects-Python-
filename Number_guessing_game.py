import random


up_limit = int(input('Enter lower limit: '))
lo_limit = int(input('Enter upper limit: '))

random_num = random.randint(up_limit, lo_limit)
print("You will have to choose a number between ", up_limit, " and ", lo_limit)

chances = 0
while chances < 8:
    chances += 1
    guess = int(input("Enter your guess: "))
    if random_num == guess:
        print("Congratulations, you did it. The number was ", random_num)
        break
    elif guess < random_num:
        print("You guessed a small number.")
    elif guess > random_num:
        print("You guessed a large number.")
    if chances == 7:
        print("\n You've run out of chances")
        print("\n The number was ", random_num)
        print("Better luck next time")
        break
print("\n")