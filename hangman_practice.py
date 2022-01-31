import random
import hangman_art
import hangman_words
print(hangman_art.title)
word_list = [hangman_words.word_list]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives = 6 
#Testing code
#print(f'{chosen_word}')

display = []

# specifies the len of the chosen word "print(_)" will show the number value. 
for _ in range(word_length):
  display += "_"
#print(display)
#print(_)
end_of_game = False
#While loops require a change of condition from False to true or true to false
while not end_of_game: 
  guess = input("Guess a letter: ").lower()

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose!")
      break
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You Win!")
    break

  print(hangman_art.stages[lives])
