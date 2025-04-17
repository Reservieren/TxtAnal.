#final version, probably

import re
from collections import Counter

def txt_anal(txt):
    # Check if the text is empty or only contains whitespace
    if not txt or not txt.strip():
        return 'No text provided...'

    # Phrase counter (done before cleaning)
    phrases = len(re.findall(r'[^.!?]*[.!?]', txt))

    # Original character count (before cleaning)
    original_char_count = len(txt)

    # Clean the text: remove punctuation and convert to lowercase
    cleaned_txt = re.sub(r'[^\w\s]', '', txt.lower())

    # Word counter
    words = cleaned_txt.split()
    word_count = len(words)

    # Cleaned character count
    cleaned_char_count = len(cleaned_txt)

    # Word frequency using Counter
    word_freq = dict(Counter(words))

    # Vowel and consonant counters
    vowels_count = len(re.findall(r'[aeiou]', cleaned_txt))
    consonants_count = len(re.findall(r'[bcdfghjklmnpqrstvwxyz]', cleaned_txt))

    # Most frequent word
    most_frequent_word = max(word_freq, key=word_freq.get) if word_freq else None

    # Average words per phrase
    avg_words_per_phrase = word_count / phrases if phrases else 0

    return {
        'original_characters': original_char_count,
        'cleaned_characters': cleaned_char_count,
        'words': word_count,
        'phrases': phrases,
        'avg_words_per_phrase': round(avg_words_per_phrase, 2),
        'most_frequent_word': most_frequent_word,
        'word_frequency': word_freq,
        'vowels': vowels_count,
        'consonants': consonants_count
    }

# Execution
txt = input('Input a text: ')
result = txt_anal(txt)
print(result)
