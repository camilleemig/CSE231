###########################################################
    #  Computer Project #9
    #
    #  Algorithm
    #   Call a function to control the flow of the program
    #       Call a function to open the file
    #       Call a function to strip the words from a file and add them to 
    #           a dictionary
    #       Call a function to find the completions of a prefix from a dictionary
    ###########################################################

def open_file():
    """
        Prompts for a file name until one opens properly
        Returns:  The object of the open file
    """
    while True:
        try:
            file_name = input("Enter a file name: ")
            fp = open(file_name, 'r')
            break
        except FileNotFoundError:
            print("Error. Please try again")
    return fp

def fill_completions(fd):
    """
    Makes a dictionary of words based on the place of letters in words
    fd: file pointer to get words from 
    returns: a dictionary of place of letter and letter as a tuple as a key
             and a set of words with that letter in that place as the value
    """
    dict = {}  
    for line in fd:
        #splits the line into words
        for word in line.split():
            #makes sure the word is only letters
            formatted_word = word.strip()
            formatted_word = formatted_word.strip("'.?!(),;:")
            formatted_word = word.lower()
            
            #Adds the word to the sets associated with the place/letter tuples
            #in the dictionary
            if formatted_word.isalpha() and (not len(formatted_word) <= 1):
                for place,letter in enumerate(formatted_word):
                    try:
                        dict[(place, letter.lower())].add(formatted_word)
                    except KeyError:
                        dict[(place, letter.lower())] = {formatted_word}
    return dict
    
def find_completions(prefix, c_dict):
    """
    Finds completions of a prefix from a dictionary
    prefix: a stripped 
    c_dict: dictionary of tuples as the key and sets as the value 
    returns: a set of word completions
    """
    words_set = set()
    for place, character in enumerate(prefix):
        #If there are no completions in the set
        if words_set == set():
            #sets the set to the set associated with the place and character
            #tuple of the current place/character in the word
            words_set = c_dict[(place, character)]
        #Makes a set of the words that were completions of previous letters
        #and are completions of the current letter
        else:
            words_set = c_dict[(place, character)] & words_set
    return words_set

def main():
    """
    Opens file, makes a dictionary of character locations in words,
    repeatedly prompts for a prefix and prints completions found
    Returns: None
    """
    fp = open_file()
    dictionary = fill_completions(fp)
    while True:
        prefix = input("Enter a prefix or '#' to quit: ")
        if prefix == '#':
            return 0
        else:
            prefix = prefix.strip()
            prefix = prefix.lower()
            completions = find_completions(prefix, dictionary)
            if completions.__len__() == 0:
                print("No completions found")
            else:
                print("Completions of",prefix + ":", end = ' ')
                for word in completions:
                    print(word, end = ' ')
                print()

#Calls main to start the program    
main()