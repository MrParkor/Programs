Word = input("Please enter a word and I'll give you index number for each letter: ")
Index = 0

while Index < len(Word):
    Letter = Word[Index]
    print(Index, Letter)
    Index = Index + 1
