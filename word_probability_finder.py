import pandas as pd


class BasicWordProbabilityFinder:

    def __init__(self):

        self.word_dataframe = None
        alphabet = [chr(i) for i in range(97, 97 + 26)]
        self.probability_dataframe = pd.DataFrame({'in_word_probability': [0] * 26},
                                                  index=alphabet)

    def find_most_probable_word(self, word_dataframe):

        self.word_dataframe = word_dataframe

        self.for_every_letter_find_probability_of_letter_being_in_word()

        self.calculate_word_probabilities()

        self.sort_words_based_on_their_probability()

        most_probable_word = self.get_most_probable_words_from_list()

        return most_probable_word

    def find_top_10_most_probable_word(self, word_dataframe):

        self.word_dataframe = word_dataframe

        self.for_every_letter_find_probability_of_letter_being_in_word()

        self.calculate_word_probabilities()

        self.sort_words_based_on_their_probability()

        top_10_most_probable_words = self.get_top_10_most_probable_words_from_list()

        return top_10_most_probable_words

    def for_every_letter_find_probability_of_letter_being_in_word(self):

        for i in range(97, 97 + 26):
            letter = chr(i)
            probability_of_letter_in_word = self.find_probability_of_letter_being_in_word(letter)
            self.probability_dataframe.loc[letter, 'in_word_probability'] = probability_of_letter_in_word

    def find_probability_of_letter_being_in_word(self, letter):

        word_series_length = len(self.word_dataframe['words'])

        letter_in_word_filter = self.word_dataframe['words'].apply(lambda word:
                                                                   True if word.count(str(letter)) > 0 else False)
        letter_filter_length = len(self.word_dataframe[letter_in_word_filter])  # letter filter == True

        try:
            probability_of_letter_in_word = letter_filter_length / word_series_length

        except ZeroDivisionError:

            exit(print('You have run out of words that meet your conditions.'))
            return

        return probability_of_letter_in_word

    def calculate_word_probabilities(self):

        self.word_dataframe['word_likelihood'] = \
            self.word_dataframe['words'].apply(lambda word:
                                               self.probability_dataframe.loc[word[0], 'in_word_probability'] *
                                               self.probability_dataframe.loc[word[1], 'in_word_probability'] *
                                               self.probability_dataframe.loc[word[2], 'in_word_probability'] *
                                               self.probability_dataframe.loc[word[3], 'in_word_probability'] *
                                               self.probability_dataframe.loc[word[4], 'in_word_probability'] *
                                               10000)

    def sort_words_based_on_their_probability(self):

        self.word_dataframe = self.word_dataframe.sort_values(['word_likelihood'])

    def get_most_probable_words_from_list(self):

        most_probable_word = self.word_dataframe.iloc[-1, 0]

        return most_probable_word

    def get_top_10_most_probable_words_from_list(self):

        top_10_most_probable_words = ['_____'] * 10

        for i in range(min(len(self.word_dataframe['words']), 10)):
            top_10_most_probable_words[i] = self.word_dataframe.iloc[-(i + 1), 0]

        return top_10_most_probable_words
