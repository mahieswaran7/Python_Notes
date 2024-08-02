import random

def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    number = ''.join(map(str, digits[:4]))
    return number

def get_cows_and_bulls(secret, guess):
    cows = sum(s == g for s, g in zip(secret, guess))
    bulls = sum(g in secret for g in guess) - cows
    return cows, bulls

def play_game():
    secret_number = generate_number()
    attempts = 0

    print("Welcome to the Cows and Bulls Game!")
    while True:
        guess = input("Enter a 4-digit number: ")
        
        # Check if the input is valid
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        attempts += 1
        cows, bulls = get_cows_and_bulls(secret_number, guess)
        
        if cows == 4:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
            break
        
        print(f"{cows} cow(s), {bulls} bull(s)")

if __name__ == "__main__":
    play_game()
