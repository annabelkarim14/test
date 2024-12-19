# Usage: python d007.py

from os import name, system
import random

stages = [
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

def main() -> None:
  # Set lives to one less than the amount of stages
  lives = len(stages)- 1

  word_list = ["aardvark", "baboon", "camel"]
  chosen_word = random.choice(word_list)

  # Comment out the answer
  #print(chosen_word)

  placeholder = ""

  word_length = len(chosen_word)

  for position in range(word_length):
    placeholder += "_"

  print(placeholder)

  game_over = False
  correct_letters = []

  while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
      if letter == guess:
        display += letter
        correct_letters.append(guess)

      elif letter in correct_letters:
        display += letter

      else:
        display += "_"

    clear_screen()
    print(display)

    if guess not in chosen_word:
      lives -= 1

      if lives == 0:
        game_over = True
        print("You lose.")
        print(f"The answer was {chosen_word}.")
    
    if "_" not in display:
      game_over = True
      print("You win !")

    print(stages[lives])


def clear_screen() -> None:
  # Windows
  if name == "nt":
    system("cls")
  
  # macOS and Linux
  else:
      system("clear")


if __name__ == "__main__":
    main()
