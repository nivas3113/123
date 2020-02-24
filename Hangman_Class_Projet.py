secret = ""
letter = ""
def test():
    if (letter in secret):
        pos = secret.find(letter)
        updatedWord[pos] = letter
        print updatedWord.join()
        ifWon()
    else:
        getLetter()