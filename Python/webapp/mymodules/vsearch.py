def search4vowels(phrase):
    '''Display any vowels found in an asked-for word.'''
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str) -> set:
    '''Return a set of the letters found in phrase.'''
    return set(letters).intersection(set(phrase))


