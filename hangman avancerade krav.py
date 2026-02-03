from random import choice

guesses_left = 8
word_list = ["kycklingprinskorv", "choklad", "bedbug", "bugbed", "sabylla incidenten", "trocadero incidenten", "mmm marabou", "benfri kotlettrad", "supercalifragilisticexpialidocious", "fioccinaucinihilipilification"]
word = choice(word_list)
guessed_letters = []
guessed_word = ["_"] * len(word)
win = False
lose = False

if  " " in word:
    index = word.index(" ")
    guessed_word[index] = " "


run = True

while run and guesses_left > 0:

    print()
    print(" ".join(guessed_word))
    print()
    print(f"Gissningar kvar: {guesses_left}", "  |  ", f"Gissade bokstäver: {" ".join(guessed_letters)}")
    guess = input("Gissa på en bokstav: ")
    guess = guess.lower()
    print()


    if not len(guess) > 1 and guess not in guessed_letters and not guess == "" and not guess == " " and guess.isalpha():
        guessed_letters.append(guess)
    
        if guess in word and guesses_left > 0:

            for i in range(len(word)):
                try:
                    index = word.index(guess, i, len(word))
                    guessed_word[index] = guess
                except:
                    None
                    
            
        else:
            guesses_left -= 1

    if guesses_left == 8:
        print()

    elif guesses_left == 7:
        print(" _ _")
        print("|   |")

    elif guesses_left == 6:
        for i in range(4):
            print("  |")
        print(" _ _")
        print("|   |")

    elif guesses_left == 5:
        print("   _ _ _")
        for i in range(4):
            print("  |")
        print(" _ _")
        print("|   |")

    elif guesses_left == 4:
        print("   _ _ _")
        print("  |     |")
        for i in range(3):
            print("  |")
        print(" _ _")
        print("|   |")
    
    elif guesses_left == 3:
        print("   _ _ _")
        print("  |     |")
        print("  |     O")
        for i in range(2):
            print("  |")
        print(" _ _")
        print("|   |")
    
    elif guesses_left == 2:
        print("   _ _ _")
        print("  |     |")
        print("  |     O")
        print("  |     |")
        for i in range(1):
            print("  |")
        print(" _ _")
        print("|   |")
    
    elif guesses_left == 1:
        print("   _ _ _")
        print("  |     |")
        print("  |     O")
        print("  |    /|\\")
        for i in range(1):
            print("  |")
        print(" _ _")
        print("|   |")
    
    elif guesses_left == 0:
        print("   _ _ _")
        print("  |     |")
        print("  |     O")
        print("  |    /|\\")
        print("  |    / \\")
        print(" _ _")
        print("|   |")
        

    

    if "".join(guessed_word) == word:
        print("......................................................")
        print()
        print(f"Rätt! Ordet var: {word}")
        print(f"Du fick {guesses_left} poäng!")
        print()
        win = True

    if guesses_left <= 0:
        print()
        print("Du förlorade")
        lose = True

    if lose or win:
        play_again = input("Spela igen (ENTER)? ")
        if play_again == "":
            guesses_left = 8
            word = choice(word_list)
            guessed_letters = []
            guessed_word = ["_"] * len(word)
            win = False
            lose = False

            if  " " in word:
                index = word.index(" ")
                guessed_word[index] = " "
        else:
            run = False
