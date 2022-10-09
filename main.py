from src.words import Words

w = Words()

word = w.getRandAnswer()
print(word)

idx = 0
win = False
print("Start guessing!")
while idx < 6:
    guess = input(f"Guess #{idx+1}: ")
    if w.isValidGuess(guess):
        result = w.checkGuess(word,guess)
        idx += 1
    else:
        print("Invalid guess")
if win:
    print(f"You won in {idx+1} guesses!")
else:
    print(f"You lost, the word was {word}")