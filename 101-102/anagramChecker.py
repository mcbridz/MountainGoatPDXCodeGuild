#filename: anagramChecker.py
#author: Zachary McBride

def split(word):
    return [char for char in word]
def anagramCheck(arg1, arg2):
    word1 = split(arg1).sort()
    word2 = split(arg2).sort()
    if word1 == word2:
        return True
    else:
        return False