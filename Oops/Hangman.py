def display_word(clue_word, guessed_letters):
   
    return ' '.join(letter if letter in guessed_letters else '_' for letter in clue_word)

def play_hangman():

    clue_word = "EVAPORATE"
    guessed_letters = set()
    incorrect_guesses = set()

    print("Welcome to Hangman!")
    print(display_word(clue_word, guessed_letters))
    
    while True:
        guess = input("Guess your letter: ").upper()

        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print(f"You already guessed '{guess}'.")
            continue

        if guess in clue_word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            incorrect_guesses.add(guess)
            print("Incorrect!")

        current_display = display_word(clue_word, guessed_letters)
        print(current_display)

        # Check if the word is completely guessed
        if all(letter in guessed_letters for letter in clue_word):
            print("Congratulations! You've guessed the word correctly!")
            break

if __name__ == "__main__":
    play_hangman()
