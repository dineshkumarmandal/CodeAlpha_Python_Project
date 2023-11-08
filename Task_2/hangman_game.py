import random
import hangman_stages
import hangman_words_file
#word_list = ["apple", "beautiful", "potato"]
lives = 6
chosen_word = random.choice(hangman_words_file.words)
print(chosen_word)
display = []
for i in range(len(chosen_word)): # 0 1 2 3 4 5 6 ...
    display += '_'

print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter : ").lower()
    for position in range(len(chosen_word)): #0 1 2 3 4 5 ..
        letter = chosen_word[position]
        if letter == guessed_letter:
            #print("Matched")
            display[position] = guessed_letter
        #else:
            #print("Not match")
    print(display)

    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You loss!!")
    if '_' not in display:
        game_over = True
        print("You win!!")
    
    print(hangman_stages.stages[lives])
            

