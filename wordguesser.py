print("Loading the word guesser game...")
import random
import json
dictionaryfile = "./assets/words_dictionary.json"
with open(dictionaryfile) as dictfile:
    print("Loading Data")
    rawDictionaryData = json.load(dictfile)
    print("Data loaded")


validLetters = "abcdefghijklmnopqrstuvwxyz"
nameJudgements = ["weird","cool"]


def FilterWords(minimumLength,maximumLength):
    dictionaryData = [word for word in rawDictionaryData if (minimumLength <= len(word) <= maximumLength)]
    #print(dictionaryData)
    wordsAmount = len(dictionaryData)
    print("{0} words available.".format(str(wordsAmount)))
    return dictionaryData, wordsAmount
    
#FilterWords(7,7)

def getIntInput(InputString: str, ErrorString: str):
    while True:
        try:
            userInput = int(input(InputString + " "))
            return userInput
        except ValueError:
            print(ErrorString)


def getLetter(InputString: str, ErrorString: str):
    # Could add a feature to only guess new letters
    while True:
        userInput = input(InputString + " ")
        if len(userInput) == 0:
            print(ErrorString)
            continue
        #print(userInput,userInput[0],str(userInput[0]))
        userLetter = userInput[0].lower()
        if userLetter in validLetters:
            return userLetter
        else:
            print(ErrorString)

def checkWord(word: str,shownletters: str):
    obfuscatedWord = ""
    allCorrect = True
    for letter in word:
        if letter in shownletters:
            obfuscatedWord += letter
        else:
            allCorrect = False
            obfuscatedWord += "_"
    return allCorrect, obfuscatedWord



skipConfiguration = True;
playingGame = True;
try:
    while playingGame:

        # Default configuration
        minAmount = 7
        maxAmount = 7 
        if skipConfiguration:
            availableWords, availableWordsAmount = FilterWords(minAmount,maxAmount)
        lifesPerWord = 4
        wordAmount = 4

        if not skipConfiguration:
            # Start with a greeting and configuring the settings

            print("Hello and welcome to the word guesser game!")
            while True:
                minAmount = getIntInput("How many letters should the word have at minimum?",\
                            "That's not a valid number, please try again.")
                maxAmount = getIntInput("How many letters should the word have at maximum?",\
                            "That's not a valid number, please try again.")
                _, availableWordsAmount = FilterWords(minAmount,maxAmount)
                if availableWordsAmount > 0:
                    break
                else:
                    print("There are 0 words left, please change the minimum/maximum.")

            lifesPerWord = 4
            
            while True:
                wordAmount = getIntInput("Please input how many words you'd like to guess! 1-{0}".format(availableWordsAmount),\
                            "That's not a valid number, please try again.")
                if 0 < wordAmount <= availableWordsAmount:
                    break
                else:
                    print("Selected number is not within the 1-{0} range.".format(availableWordsAmount))
        

        print("Are you ready to begin?!")
        guessedWords = []
        failedWords = []

        for wordNumber in range(wordAmount):
            randomWord = random.choice(availableWords)
            guessedLetters = ""
            correct = False
            print("Word {0}/{1}! Correct: {2}/{3}".format(wordNumber+1,wordAmount,len(guessedWords),(len(guessedWords)+len(failedWords))))
            print("DEBUG: Word is {0}".format(randomWord))
            lifesLeft = lifesPerWord
            while lifesLeft > 0 and not correct:
                print("Life {0}/{1} Letters guessed: {2}".format(lifesLeft,lifesPerWord,guessedLetters))
                letter = getLetter("Pick a letter a-z",\
                        "That's not one of the letters {0}".format(validLetters))
                guessedLetters += letter

                if letter not in randomWord:
                    lifesLeft -= 1

                correct, obfuscatedWord = checkWord(randomWord,guessedLetters)
                if not correct:
                    print(obfuscatedWord)
                    
            
            if correct:
                print("Guessed the correct word '{0}'!".format(randomWord))
                guessedWords.append(randomWord)
            else:
                print("Ran out of lifes! Word was '{0}'.".format(randomWord))
                failedWords.append(randomWord)

        print("The game is over!")
        print("Results: {0}/{1}".format(len(guessedWords),(len(guessedWords) + len(failedWords))))
              
        continuePlayingInput = input("Would you like to keep playing? y/N")
        if not (len(continuePlayingInput) > 0 and continuePlayingInput[0].lower() == "y"):
            print("Thanks for playing!")
            break
        # Victory stuff

        # Readd the words to the potential word list.

        






except KeyboardInterrupt:
    print("\nExited game.")
    print("But we haven't even finished the game yet!")