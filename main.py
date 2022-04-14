# Wordle Amogus Finding Tool by Orhu

def main():
    print("====== Wordle Amogus Finder Tool ======\n")
    print("Welcome to the Amogus Finder Tool for the hit New York Times game \"Wordle\"")
    print("Please enter a five-letter word: ", end='')
    wotd = input()
    print("\n")
    WordleAmogusFinder(wotd)


def WordleAmogusFinder(wotd, mode=0, rarityMode=""):
    """
    Computes Among Us Crewmate patterns that can be created with a given wordle word
    :param wotd: Wordle word of the day.
    :param mode: Integer corresponding to output mode (by default is set to single mode)
    0 = Single Mode, returns a single word set that creates the highest rarity amogus for that day.
    1 = Data Mode, returns the 10 highest rarity amogi, plus a total number of amogi of each (non-failure) rarity
    possible with the wotd. TO BE ADDED LATER
    2 = Rarity Mode, returns a word of a specified rarity. TO BE ADDED LATER
    :param rarityMode: For use in Rarity Mode only. Specify desired rarity using the following format.
    L = Legendary, E = Epic, U = Uncommon, C = Common
    :return: All possible word sets that create wordle amogus
    """

    wotd = wotd.strip().lower()

    wordList = wordListRead() # Why do this in another function but not the dictionaries...

    patternDict = {"GGGBB":{"priority":[0,4],"words":[],"level":0},
                   "YYGGB":{"priority":[0,10],"words":[],"level":1},
                   "GGGGB":{"priority":[0,2,4,6],"words":[],"level":2},
                   "GBGBB":{"priority":[0,4],"words":[],"level":4},
                   "BGGGB":{"priority":[1,2,5,6],"words":[],"level":0},
                   "BYYGG":{"priority":[1,11],"words":[],"level":1},
                   "BGGGG":{"priority":[1,3,5,7],"words":[],"level":2},
                   "BGBGB":{"priority":[1,2,5,6],"words":[],"level":4},
                   "GGYYB":{"priority":[2,8],"words":[],"level":1},
                   "BBGGG":{"priority":[3,7],"words":[],"level":0},
                   "BGGYY":{"priority":[3,9],"words":[],"level":1},
                   "BBGBG":{"priority":[3,7],"words":[],"level":4},
                   "BBGGB":{"priority":[4],"words":[],"level":1},
                   "BBBGG":{"priority":[5],"words":[],"level":1},
                   "GGBBB":{"priority":[6],"words":[],"level":1},
                   "BGGBB":{"priority":[7],"words":[],"level":1},
                   "YYYBB":{"priority":[8,12],"words":[],"level":0},
                   "YYYYB":{"priority":[8,10,12,14],"words":[],"level":2},
                   "YBYBB":{"priority":[8,12],"words":[],"level":4},
                   "BYYYB":{"priority":[9,10,13,14],"words":[],"level":0},
                   "BYYYY":{"priority":[9,11,13,15],"words":[],"level":2},
                   "BYBYB":{"priority":[9,10,13,14],"words":[],"level":4},
                   "BBYYY":{"priority":[11,15],"words":[],"level":0},
                   "BBYBY":{"priority":[11,15],"words":[],"level":4},
                   "BBYYB":{"priority":[12],"words":[],"level":1},
                   "BBBYY":{"priority":[13],"words":[],"level":1},
                   "YYBBB":{"priority":[14],"words":[],"level":1},
                   "BYYBB":{"priority":[15],"words":[],"level":1},
                   "BBBBB":{"priority":[16],"words":[],"level":5}}

    rarityDict = {0:"Legendary Quality Type-A",
                1:"Legendary Quality Type-B",
                2:"Legendary Quality Type-C",
                3:"Legendary Quality Type-D",
                4:"Epic Quality Type-A",
                5:"Epic Quality Type-B",
                6:"Epic Quality Type-C",
                7:"Epic Quality Type-D",
                8:"Rare Quality Type-A",
                9:"Rare Quality Type-B",
                10:"Rare Quality Type-C",
                11:"Rare Quality Type-D",
                12:"Common Quality Type-A",
                13:"Common Quality Type-B",
                14:"Common Quality Type-C",
                15:"Common Quality Type-D",
                16:"Failure Quality"}
    # Yes I know this is terrible. I don't care.

    # Sort words into their pattern lists.
    for word in wordList:
        pattern = wordCheck(word,wotd) # Is it even necessary to make a list? Can't you just read in the file here?
        if pattern in patternDict:
            # noinspection PyTypeChecker
            patternDict[pattern]["words"].append(word)

    # Amogus Finding Time (AFT for short)
    amogusWordList = ["","","","","",wotd]
    endPriority = -1

    for i in range(16):
        for pattern in patternDict:
            if i in patternDict[pattern]["priority"]:
                if not patternDict[pattern]["words"]:
                    for j in range(5):
                        amogusWordList[j] = ""
                    break
                else:
                    index = patternDict[pattern]["level"]
                    if index == 5:
                        for j in range(5):
                            amogusWordList[j] = patternDict[pattern]["words"][0]
                    elif index == 2:
                        amogusWordList[2] = patternDict[pattern]["words"][0]
                        amogusWordList[3] = patternDict[pattern]["words"][0]
                    else:
                        amogusWordList[index] = patternDict[pattern]["words"][0]
        if "" not in amogusWordList:
            endPriority = i
            break

    # Output
    rarity = rarityDict[endPriority]

    print("Amogus Rarity for word \"" + wotd + "\":", rarity)
    if endPriority < 4:
        print("Congratulations! A Legendary-Grade Amogus is quite a rare find!\n")
    elif endPriority < 8:
        print("An Epic-Quality Amogus?! That's amazing!\n")
    elif endPriority < 12:
        print("A Rare Amogus is a lot less exciting than it sounds...\n")
    elif endPriority < 16:
        print("Only a Common-Grade Amogus could be found today. Better luck next time! \n")
    else:
        print("\"Failure Quality\"? What does that even mean??\n")

    print("Word List:")
    for i in amogusWordList:
        print(i)
    return


def wordCheck(word, checkWord):
    """
    Generates hint response for word based on checkWord.
    :param word: Word to generate hints for.
    :param checkWord: The word being checked against.
    :return: A five character hint string
    """
    hintString = []
    word = list(word)
    checkWord = list(checkWord)
    # need to account for multi-letter
    for i in range(len(word)):
        if word[i] == checkWord[i]:
            hintString.append('G')
            checkWord[i] = ''
        elif word[i] in checkWord:
            for j in range(len(checkWord)):
                if word[i] == checkWord[j]:
                    hintString.append('Y')
                    checkWord[j] = ''
                    break
        else:
            hintString.append('B')
    return ''.join(hintString)


def wordListRead():
    """
    Helper function for reading in our word list
    :return: Word list as a list
    """

    file = open("wordlist.txt","r")

    wordList = []

    for line in file:
        wordList.append(line.strip())

    file.close()

    return wordList

main()
