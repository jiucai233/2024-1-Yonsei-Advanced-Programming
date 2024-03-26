import random

def play_russian_roulette():
    while True:
        user_num = int(input("Welcome to Russian Roulette! Please input a number between 1 and 6: "))
        if user_num < 1 or user_num > 6:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        num = random.randint(1, 6)
        if user_num == num:
            print("You lost!")
            break
        else:
            print("Congratulations! You survived this round.")

        play_again = input("Do you want to play again? (y/n) ")
        if play_again != "y":
            print("Thanks for playing!")
            break

play_russian_roulette()