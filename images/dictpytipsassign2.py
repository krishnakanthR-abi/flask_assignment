#Write a function char_freq() that takes a string and builds a frequency listing of thecharacters contained in it. Represent the frequency listing as a Python dictionary. Try it with something likechar_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq( input_string ):
    #fiinding unique characs from the input string
    unique_characters = set( char for char in input_string)
    #creating dictionary with characs as keys and freq as values
    python_dictionary = { char : input_string.count(char) for char in unique_characters}

    return python_dictionary

print( char_freq( input().strip()) )
