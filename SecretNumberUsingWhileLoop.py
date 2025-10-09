# This program is about to guess the secret number using while loop

secret_number = int(input("Enter the number: "))
guess = 0

while guess != secret_number:
    try:
        guess = int(input("Guess the secret number between 1 and  100: "))
        if guess < secret_number:
            print("Too low ! Try again")
        elif guess > secret_number:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number. ")

print(f"Congratulation! You guessed the secret number: {secret_number}")