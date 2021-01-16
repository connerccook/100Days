import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
lives = 6
display = []
counter = 0
game_solved = 0
guessed_letters = []
guess = ""
for letter in chosen_word:
    display += "_"
    counter += 1
print(hangman_art.stages[lives])
while(lives != 0):
    if counter == 0:
        game_solved = 1
        break
    already_guessed = 0
    while already_guessed == 0:
        guess = input("Guess a letter: ").lower()
        if(guessed_letters.count(guess) > 0):
            print(f"{guess} is already used. Please try again.")
        else:
            already_guessed = 1
            guessed_letters.append(guess)
    flag = 0
    for it in range(0, len(chosen_word)):
        if guess == chosen_word[it]:
            display[it] = guess
            flag += 1
    if flag > 0:
        counter -= flag
    else:
        lives -= 1
        print(f"{guess} is not in the word")
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])
if game_solved == 0:
    print("game over")
else:
    print("You won!")
