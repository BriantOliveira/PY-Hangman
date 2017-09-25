import os

class Hangman():

    def __init__(self):
        print("Welcome to 'Hangman', are you ready to die?")
        print("(1)Yes, I'm ready to challenge death.\n(2)No, get me outta here!")
        user_choice_1 = input("->")

        if user_choice_1 == '1':
            print("LOADING... IF YOU WANT TO SURVIVE YOU MUST FOLLOW THE NUMBERS...IF YOU DON'T YOU WILL DIE")
            self.start_game()
        elif user_choice_1 == '2':
            print("Bye bye Felicia...")
            exit()
        else:
            print("I'm sorry, I could not understand your dumb ass, can you repeat that?")
            self.__init__()

    def clear(self):
        os.system("clear")

    def start_game(self):
        print("1) I need to tell you a secret. Look at 5")
        print("2) The answer is YOU GOT ONLY ONE CHANCE TO SCAPE DEATH, now look at 11")
        print("3) You can't scape me... look at 15")
        print("4) You can try to run, but you won't succeed. In order to run you must look at 13.")
        print("5) To know how this game works first look at 2.")
        print("6) You can only make six wrong choices but look at 12.")
        print("7) I just wanted to say that you are a Hangman already...Say your last words.")
        print("8) What I wanted to tell you is...I'll see you in hell soon, look at 14")
        print("9) You really want to live hun?! Look at 4.")
        print("10) This is the last to run away, I'm around the corner. Now look at 7.")
        print("11) I hope you're not mad when I say this look at 6.")
        print("12) Sorry looser look at 8.")
        print("13) DEATH is faster then you think. To keep running look at 10.")
        print("14) I don't know how to say this so clearly so your dumb ass can undersand but look at 3.")
        print("15) You must sacrifice your knowledge at this point, in order to live look at number 9.")
        self.core_game()


    def core_game(self):
        guesses = 0
        letters_used = []
        the_word = ['e', 's', 'c', 'a', 'p', 'e']
        progress = ["_", "_", "_", "_", "_","_"]

        while guesses < 6:
            guess = input("Guess a letter ->")
            if guess in the_word and guess not in letters_used:
                print("You may be lucky this time, let's see how long it will last!")
                letters_used +=  "," + guess
            if letters_used == guess:
                progress[i] = guess
                self.hangman_graphic(guesses)
                print("Progress: " + "".join(progress))
                print("Letter used: " + " ".join(letters_used))

            elif guess not in the_word and guess not in letters_used:
                guesses += 1
                letters_used += "," + guess
                self.hangman_graphic(guesses)
                print("Roses are red, violets are blue... you are one step closer to losing your life. too!")
                print("Noose aren't noose, they are weapons. You can save them in your pocket until you need them.")
                print("You know what they say about hope. It breeds eternal misery")
                print("Progress:" + "".join(progress))
                print("Letter used: " + "".join(letters_used))

            else:
                print("Mirror, mirror on the wall, will this be the death to end it all?")
                print("Muahaha wrong letter...")

    def hangman_graphic(self, guesses):
        if guesses == 0:
         print("________      ")
         print("|      |      ")
         print("|             ")
         print("|             ")
         print("|             ")
         print("|             ")
        elif guesses == 1:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|             ")
         print("|             ")
         print("|             ")
        elif guesses == 2:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|     /       ")
         print("|             ")
         print("|             ")
        elif guesses == 3:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|     /|      ")
         print("|             ")
         print("|             ")
        elif guesses == 4:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|     /|\     ")
         print("|             ")
         print("|             ")
        elif guesses == 5:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|     /|\     ")
         print("|     /       ")
         print("|             ")
        else:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|     /|\     ")
         print("|     / \     ")
         print("|             ")
         print("Don't get too comfortable. It's not over until I say it is.")
         print("Ding Dong welcome to the kingdom of hell")
         print("GAME OVER!!!")
         self.__init__()

    def __replay__(self):
        print("Do you want to die again?")
        print("(1)Yes, I'm ready to challenge death again.\n(2)No, sorry!")
        user_choice_1 = input("->")

        if user_choice_1 == '1':
            print("Loading nooses, murderers, rapists, thiefs, lunatics...")
            self.start_game()
        elif user_choice_1 == '2':
            print("Bye bye Felicia...")
            exit()
        else:
            print("I'm sorry, I could not understand your dumb ass, can you repeat that?")
            self.__init__()

    def progress_updater(self, guess, the_word, progress):
        i = 0
        while i < len(the_word):
            if guess == the_word[i]:
                    progress[i] = guess
                    i += 1
            else:
                    i+= 1

        return"".join(progress)
game =  Hangman()



