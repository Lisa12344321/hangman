from random import choice

guesses_left = 8
word_list = ["kycklingprinskorv"] #"choklad", "bedbug", "bugbed", "sabylla", "kycklingprinskorv", 
word = choice(word_list)
guessed_letters = []
guessed_word = ["_"] * len(word)
print(word)
print(len(word))
run = True

while run and guesses_left > 0:

    print(" ".join(guessed_word))
    print()
    guess = input("Gissa på en bokstav: ")
    guessed_letters.append(guess)
    
    if guess in word and guesses_left > 0:
        letter_count = word.count(guess)
        index = 0

        for i in range(len(word)):
            try:
                index = word.index(guess, i, len(word))
                print(index)
                guessed_word[index] = guess
            except ValueError:
                print("nej")
                
        
    else:
        guesses_left -= 1

    # if guess in word and guesses_left > 0:
    #     letter_count = word.count(guess)
    #     index = 0

    #     if letter_count > 1:
    #         for i in range(len(word)):
    #             index = word.index(guess, i, len(word))
    #             print(index)
    #             guessed_word[index] = guess
    #     else:
    #         index = word.index(guess)
    #         guessed_word[index] = guess
        
    # else:
    #     guesses_left -= 1
    

    print()
    print(" ".join(guessed_word))
    print()
    print(f"Gissningar kvar: {guesses_left}", "  |  ", f"Gissade bokstäver: {" ".join(guessed_letters)}")
    print()

    if "".join(guessed_word) == word:
        print("......................................................")
        print()
        print(f"Rätt! Ordet var: {word}")
        print()
        run = False

    if guesses_left <= 0:
        print("Du förlorade")
        run = False
