from src.state import state
from random import randint

class Words:
    def __init__(self) -> None:
        self.words = []
        self.answers = []
        self.black_letters = []
        self.yellow_letters = []
        self.yellow_letters_positions = []
        self.green_letters = ['','','','','']
        with open('data/words.txt', 'r') as f:
            line = f.readline().replace("\n","")
            while line:
                self.words.append(line)
                line = f.readline().replace("\n","")
        with open('data/answers.txt', 'r') as f:
            line = f.readline().replace("\n","")
            while line:
                self.answers.append(line)
                line = f.readline().replace("\n","")
    
    def getRandWord(self):
        return self.words[randint(0,(len(self.words)-1))]

    def getRandAnswer(self):
        return self.answers[randint(0,(len(self.answers)-1))]

    def checkGuess(self,word,guess):
        dupLetters = self.__getDuplicates(guess)
        gs = []
        idx = 0 
        while idx < 5:
            if word[idx] == guess[idx]:
                gs.append([guess[idx], state.Green])
            elif self.__containsLetter(word,guess[idx]):
                gs.append([guess[idx], state.Yellow])
            else:
                gs.append([guess[idx], state.Black])
            idx += 1
        for l in dupLetters:
            idcs = self.__getIndexOfDuplicates(guess,l)
            # Needs to be updated to work with three letter duplicates
            if len(idcs) == 2:
                if gs[idcs[0]][1] == state.Green and gs[idcs[1]][1] == state.Yellow:
                    print("Green-Yellow")
                    gs[idcs[1]][1] = state.Black
                elif gs[idcs[0]][1] == state.Yellow and gs[idcs[1]][1] == state.Green:
                    print("Yellow-Green")
                    gs[idcs[0]][1] = state.Black
                elif gs[idcs[0]][1] == state.Yellow and gs[idcs[1]][1] == state.Yellow:
                    print("Yellow-Yellow")
                    gs[idcs[1]][1] = state.Black
        self.__colorCode(gs)

    def isValidGuess(self,guess) -> bool:
        # Return True for testing
        return True
        # return self.words.__contains__(guess)

    def __getDuplicates(self,guess):
        x=[]
        for i in guess:
            if i not in x and guess.count(i)>1:
                x.append(i)
        return(x)

    def __getIndexOfDuplicates(self,seq,item):
        start_at = -1
        locs = []
        while True:
            try:
                loc = seq.index(item,start_at+1)
            except ValueError:
                break
            else:
                locs.append(loc)
                start_at = loc
        return locs
    
    def __containsLetter(self, word, guess_letter) -> bool:
        for l in word:
            if guess_letter == l:
                return True
        return False

    def __colorCode(self,tup):
        word = []
        green = "\033[1;32m"
        yellow = "\033[1;33m"
        black = "\033[1;30m"
        for s in tup:
            if s[1] == state.Green:
                word.append(green + s[0])
            elif s[1] == state.Yellow:
                word.append(yellow + s[0])
            else:
                word.append(black + s[0])
        self.__printWord(word)

    def __printWord(self,word):
        for w in word:
            print(w, end="")
        print("\033[1;97;0m")