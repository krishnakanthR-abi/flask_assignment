#Represent a small bilingual lexicon as a Python dictionary in the followingfashion{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt","year":"år"}anduseittotranslateyourChristmascardsfromEnglishintoSwedish.Thatis, write a function translate() that takes a list of English words and returns a list of Swedish words.

def translate(english_word_list, lexicon):
    # finding lexicon word from english word list
    swedish_word_list = [lexicon[word] for word in english_word_list]

    return swedish_word_list

lexicon = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "newmer":"nytt","year":"år"}
english_word_list = input().strip().split()

#printing lexicon words
print(' '.join( translate(english_word_list, lexicon) ) )