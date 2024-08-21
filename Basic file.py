import random

def guess_the_number():
    # Step 1: Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Step 2: Initialize the number of attempts
    attempts = 0
    
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Step 3: Loop until the user guesses the number
    while True:
        # Step 4: Get the user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Step 5: Check the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break  # Exit the loop since the guess is correct

# Call the function to start the game
guess_the_number()
