
def get_char_index(char, word):
    indices = []
    for index, letter in enumerate(word):
        if char == letter:
            indices.append(index)
    return indices


name = input("What is your name? ")
print(f"=== Hello {name}")

words = {'kiwi', 'apple', 'banana', 'orange'}


# choose random word to guess
random_word = words.pop()
guessedword  = ["-"]*len(random_word)  # [_- ---]
print(random_word)
print("-- try to guess this word : ", "".join(guessedword))

for i  in range(7):
    char = input("Guess a letter: ").lower()
    if char in random_word:
        # get index of it
        char_index = get_char_index(char, random_word)
        # print(char_index)
        # print(guessedword)
        # replace it list of guessed word
        for i in char_index:
            guessedword[i] = char
        # print guessed after adding the chars
        if "".join(guessedword) == random_word:
            print(f"the word is {random_word}, congratulations!")
            break
    print("".join(guessedword))
else:
    print('You Lose!')