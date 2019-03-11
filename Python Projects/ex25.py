def break_words(stuff):
    """This line will break up words for us"""
    words = stuff.split()
    return words

def sort_words(words):
    """This will sort the words for us"""
    return sorted(words)

def print_first_words(words):
    """Print the first words after popping off"""
    word = words.pop(0)
    print(word)

def print_last_words(words):
    """Prints last words after popping off"""
    word = words.pop(-1)
    print(word)

def sort_sentance(sentance):
    """Takes in full sentance and then returns the sorted words"""
    words = break_words(sentance)
    return sort_words(words)

def print_first_and_last(sentance):
    """Prints the first and last words of a sentance"""
    words = break_words(sentance)
    print_first_words(words)
    print_last_words(words)

def print_first_and_last_sorted(sentance):
    """Sorts the words then prints the first and last ones"""
    words = sort_sentance(sentance)
    print_first_words(words)
    print_last_words(words)


