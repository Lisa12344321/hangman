from random import choice

guesses_left = 8
word_list = ["tetst", "hej"]
word = choice(word_list)
guessed_letters = []
guessed_word = ["_"] * len(word)
print(word)
print(guessed_word)
run = True

while run:
    guess = input("Gissa på en bokstav: ")
    guessed_letters.append(guess)

    if guess in word and guesses_left > 0:
        letter_count = word.count(guess)
        #from_index = 0

        if letter_count > 1:
            for i in range(len(word)):
                index = word.index(guess, i, len(word))
            # from_index += 1
                guessed_word[index] = guess
        else:
            index = word.index(guess)
            guessed_word[index] = guess

        #söker framifrån
        # index = word.find(guess)
        # guessed_word[index] = guess
        # #söker bakifrån
        # index2 = word.rfind(guess)
        # guessed_word[index2] = guess
        #söker i mitten
        # index3 = word.find(guess, index, index2)
        # guessed_word[index3] = guess

        
        
    else:
        print("nej")
        guesses_left -= 1
    
    print(letter_count)
    print(guessed_word)
    print(guessed_letters)
    print(guesses_left)
    print(len(word))
