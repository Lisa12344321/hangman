from random import choice

guesses_left = 8
word_list = ["test", "hej"]
word = choice(word_list)
guessed_letters = []
guessed_word = ["_"] * len(word)
print(word)
print(guessed_word)
run = True

while run:
    guess = input("Gissa på en bokstav: ")
    if guess in word:
        index = word.find(guess)
        guessed_word[index] = guess
        print(guessed_word)
    else:
        print("nej")
