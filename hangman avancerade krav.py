from random import choice
import os

os.system("cls")
for i in range(7):
    print()
guesses_left = 8
word_list = ["kycklingprinskorv", "choklad", "bedbug", "bugbed", "sabylla incidenten", "trocadero incidenten", "mmm marabou", "benfri kotlettrad", "supercalifragilisticexpialidocious", "fioccinaucinihilipilification"]
word = choice(word_list)
guessed_letters = []
guessed_word = ["_"] * len(word)
win = False
lose = False

# om det är mellanslag i ordet behöver man inte gissa att det ska vara ett mellanslag
if  " " in word:
    for i in range(len(word)):
        try:
            index = word.index(" ", i, len(word))
            guessed_word[index] = " "
        except:
            None


run = True

while run and guesses_left > 0:

    print()
    print(" ".join(guessed_word)) # guessed_word är en lista men printas som en string med mellanslag mellan alla tecken
    print()
    print(f"Gissningar kvar: {guesses_left}", "  |  ", f"Gissade bokstäver: {" ".join(guessed_letters)}") # samma sak med guessed_letters
    guess = input("Gissa på en bokstav: ")
    guess = guess.lower() # spelar ingen roll om det är stor eller liten bokstav som man skriver
    print()


    if not len(guess) > 1 and guess not in guessed_letters and not guess == "" and not guess == " " and guess.isalpha(): # bara gissa 1 bokstav, gissningen får inte redan ha gissats, man kan inte gissa mellanslag eller ENTER, gissningen måste vara en bokstav
        guessed_letters.append(guess)
    
        if guess in word and guesses_left > 0:

            for i in range(len(word)): # repeterar för varje bokstav i ordet
                try:
                    index = word.index(guess, i, len(word)) # hittar indexet var bokstaven finns i ordet | kommer hitta indexet mellan i och slutet på ordet, intervallet blir mindre och mindre, måste göra så här för annars kommer den bara hitta det första indexet där bokstaven finns
                    guessed_word[index] = guess # byter ut "_" mot gissningen där bokstaven finns
                except:
                    None
                    
            
        else:
            guesses_left -= 1 # om bokstaven inte finns

    os.system("cls")

    # streckgubben
    if guesses_left == 8:
        for i in range(7):
            print()

    elif guesses_left == 7:
        for i in range(5):
            print()
        print(" _ _")
        print("|   |")

    elif guesses_left == 6:
        print()
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
        print("  |    /|\\") # måste skriva \\ istället för \, för det funkar inte att skriva \ i en string | kommer printas som bara \
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
        

    

    if "".join(guessed_word) == word: # guessed_word blir en string | om guessed_word är samma som word vinner man
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
        if play_again == "": # om man trycker ENTER
            # resettar
            os.system("cls")
            for i in range(7):
                print()
            guesses_left = 8
            word = choice(word_list) # nytt ord
            guessed_letters = []
            guessed_word = ["_"] * len(word)
            win = False
            lose = False

            if  " " in word:
                for i in range(len(word)):
                    try:
                        index = word.index(" ", i, len(word))
                        guessed_word[index] = " "
                    except:
                        None
        else:
            run = False # om man skriver nåt annat avslutas spelet
