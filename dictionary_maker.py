import pandas as pd
import os
import numpy as np
'''
data_path = "C:/Users/Peter/OneDrive - Loughborough University/Documents/Programming/Word/"


def filter_out_non_string_values(word_series):

    string_filter = word_series.apply(lambda word: type(word) == str)
    word_series = word_series[string_filter]

    return word_series


def filter_out_non_alphabet_character(word_series):

    alphabet_character_filter = word_series.apply(
        lambda word: all([True if ord(letter) in range(97, 97 + 26) else False for letter in word.lower()]))
    word_series = word_series[alphabet_character_filter]

    return word_series


def filter_out_words_with_multiple_same_letters(word_series):

    unique_letters_filter = word_series.apply(
                        lambda word: all([True if word.count(letter) == 1 else False for letter in word]))
    word_series = word_series[unique_letters_filter]

    return word_series

def filter_out_non_five_letter_words(word_series):

    five_letter_filter = word_series.apply(lambda word: True if len(word) == 5 else False)

    word_series = word_series[five_letter_filter]

    return word_series


dictionary_series = pd.Series([], dtype=pd.StringDtype())


for i in range(65, 65 + 26):

    file_name = f'{chr(i)}word.csv'
    print(file_name)

    if i == 67:

        file_name = 'Cword1.txt'

    if i == 77:

        file_name = 'Mword1.txt'

    if i == 80:

        file_name = 'Pword1.txt'

    if i == 83:

        file_name = 'Sword1.txt'

    word_dataframe = pd.read_csv(os.path.join(data_path, file_name), sep=',    ', delimiter=None, header=None,
                                 names=None, index_col=None, usecols=None, engine='python', encoding='utf8')

    word_series = pd.Series(word_dataframe[0])
    word_series = word_series[~word_series.duplicated()]

    word_series = filter_out_non_string_values(word_series)
    word_series = filter_out_non_alphabet_character(word_series)
    word_series = filter_out_non_five_letter_words(word_series)
    word_series = filter_out_words_with_multiple_same_letters(word_series)

    dictionary_series = pd.concat([dictionary_series, word_series])

print(dictionary_series)

dictionary_series.to_csv("C:/Users/Peter/OneDrive - Loughborough University"
                         "/Documents/Programming/Word/Dictionary Of 5 Letter Words.csv", index=False, header=False)
'''
"""
guesses_file_name = "C:/Users/Peter/PycharmProjects/WordleProject/word_sample_files/wordle-allowed-guesses.txt"
answers_file_name = "C:/Users/Peter/PycharmProjects/WordleProject/word_sample_files/wordle-answers-alphabetical.txt"

guesses_dataframe = pd.read_csv(guesses_file_name, sep=',    ', delimiter=None, header=None,
                             names=None, index_col=None, usecols=None, engine='python', encoding='utf8')
answers_dataframe = pd.read_csv(answers_file_name, sep=',    ', delimiter=None, header=None,
                             names=None, index_col=None, usecols=None, engine='python', encoding='utf8')

guesses_series = guesses_dataframe[0]
answers_series = answers_dataframe[0]

words_series = pd.concat([answers_series, guesses_series])

words_series = words_series.sort_values(axis=0, ignore_index=True)
print(words_series)


words_series.to_csv("C:/Users/Peter/PycharmProjects/WordleProject/word_sample_files/wordle_words.txt"
                    , index=False, header=False)
"""

with open('word_sample_files/NYT_Wordle_words.txt') as file:

    # Converting string to list
    string_word_list = file.read()
    word_list = string_word_list.strip('][').split('","')
    word_list[0] = 'cigar'
    word_list[-1] = 'zymic'

    print(word_list)
    print(len(word_list))