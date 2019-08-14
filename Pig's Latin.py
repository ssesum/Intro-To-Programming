print("Welcome to the Pig Latin Translator!")
pyg = "ay"
word = ("Enter a word: ")


if len(word) > 1 and word.isalpha():
        word_lower = word.lower()
        first_letter = word_lower[0]
        new_word = word_lower + first_letter + pyg
        new_word = new_word[1:len(new_word)]
        print (new_word)
else:
        print ("Try again!")
