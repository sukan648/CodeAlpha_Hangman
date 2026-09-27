import random

words = ["python", "computer", "programming", "hangman", "developer"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if all(letter in guessed_letters for letter in word):
        print("🎉 You won! The word was:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

else:
    print("\n💀 Game Over!")
    print("The word was:", word)