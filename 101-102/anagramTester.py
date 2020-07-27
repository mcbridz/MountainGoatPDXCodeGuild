from anagramChecker import anagramCheck, split

word1 = "dormitory"
word2 = "dirtyroom"

if anagramCheck(word1, word2):
    print(f"{word1} and {word2} are anagrams of each other.")
else:
    print(f"{word1} and {word2} are not anagrams of each other.")