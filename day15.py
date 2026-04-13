secret = 7
guesses = 0

while True:
    guess = int(input("Enter your guess: "))
    guesses = guesses + 1
    if guess == secret:
        print("Correct! you got it in", guesses, "guesses!")
        break
    elif guesses >= 5:
        print("❌ Out of guesses! The secret number was", str(secret) + ".")
        break
    elif guess < secret:
        print("Too low! Try again")
    else:
        print("Too high! Try again")


