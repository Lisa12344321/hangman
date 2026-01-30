from random import choice

guesses_left = 8
word_list = ["kycklingprinskorv", "choklad", "bedbug", "bugbed", "sabylla incidenten", "trocadero incidenten", "mmm marabou", "benfri kotlettrad", "supercalifragilisticexpialidocious"]
word = choice(word_list)
guessed_letters = []
guessed_word = ["_"] * len(word)

if  " " in word:
    index = word.index(" ")
    guessed_word[index] = " "


run = True

while run and guesses_left > 0:
    for i in range(2):
        print()
    print(" ".join(guessed_word))
    for i in range(2):
        print()

    guess = input("Gissa på en bokstav: ")
    guessed_letters.append(guess)
    
    if guess in word and guesses_left > 0:

        for i in range(len(word)):
            try:
                index = word.index(guess, i, len(word))
                guessed_word[index] = guess
            except ValueError:
                print()
                
        
    else:
        guesses_left -= 1
    

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
