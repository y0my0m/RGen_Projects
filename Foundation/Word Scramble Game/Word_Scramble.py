import random

print("Welcome to Obo's Word Unscrambler Challenge!")

print("Unscramble Earth words to help Obo learn and earn points.")
  
  
  
def read_words_from_file(filename):
    file = open(filename, 'r')
    words = []
    for line in file:
        word = line.strip()
        words.append(word)
    file.close()
    return words

def scramble_word(word):
     # Step 1: Turn the word into a list of letters
    letter_list = []
    for letter in word:
        letter_list.append(letter)

    # Step 2: Shuffle the letters around
    random.shuffle(letter_list)

    # Step 3: Put the letters back together into a word
    scrambled_word = ""
    for letter in letter_list:
        scrambled_word = scrambled_word + letter

    # Step 4: Give back the scrambled word
    return scrambled_word

def play_round(word):
    returned_scrambled = scramble_word(word)
    print(f"\nUnscramble this word: {returned_scrambled}")

    for attempt in range(3):
        guess = input(f"Attempt {attempt + 1}/3: ").lower()
        if guess == word:
            print(f"Correct! The word was {word}.")
            return 3 - attempt

    print(f"Sorry, you're out of attempts. The word was {word}.")
    return 0
returned_words = read_words_from_file("earth_words.txt")
playing = True
Score = 0

while playing:
    word = random.choice(returned_words)
    Score = Score + play_round(word)
    play_again = input("Do you want to unscramble another word? (yes / no)").lower()
    if play_again == 'no':
        playing = False
        

print(f"\nGame Over! Your Final Score is {Score}.")
print(f"\nObo Thanks You For Your Help In Learing Earth Words")



