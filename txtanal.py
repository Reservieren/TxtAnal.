import re

def txt_anal(txt):
    # txt cleaner (remove special characters)
    if not txt:
        return 'No text provided...'
    
    txt = re.sub(r'[^\w\s]', '', txt.lower())

    #words counter
    words = txt.split()
    word_count = len(words)

    #phrases counter
    phrases = len(re.split(r'[.!?]', txt)) - 1

    #characters counter
    char_count = len(txt)

    #word frequency
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

#vowels and consonants counter

    vowels = re.findall(r'[aeiou]', txt)
    vowels_count = len(vowels)
    
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyz]', txt)
    consonants_count = len(consonants)

    return {
        'characters':char_count,
        'words': word_count,
        'phrases': phrases,
        'word_frequency': word_freq,
        'vowels': vowels_count,
        'consonants': consonants_count
    }

txt = input('Input a text: ')
result = txt_anal(txt)
print(result)
# 