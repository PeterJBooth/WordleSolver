from time import time
import pandas as pd

from word_comparer import WordComparer
from word_result_combinations import WordResultCombinations
from result_dataframe import ResultDataframe
from word_filter import WordFilter
import numpy as np


class MatchingArrayCalculator:

    def __init__(self, word_dataframe):

        self.word_dataframe = word_dataframe
        self.result_dataframe = ResultDataframe()
        self.word_comparer = WordComparer()
        self.word_result_combinations = WordResultCombinations()
        self.word_filter = WordFilter()

        self.matching_words_array = self.create_match_words_array()
        self.row = None
        self.counter = 0

    def create_match_words_array(self):

        # 1 row for each word
        # Within each row contains every word index as well as 243 + 1 spaces to separate one result combination's word
        # indexes from another

        shape = (len(self.word_dataframe), len(self.word_dataframe) + 243 + 1)
        matching_words_array = np.zeros(shape=shape).astype(np.int16)

        return matching_words_array


    def create_array_of_words_matching_to_results(self):

        for i in range(1000, 1001):

            word = self.word_dataframe.loc[i, 'words']
            print(word)

            self.create_row_of_words_matching_to_results_of_word(word)

    def create_row_of_words_matching_to_results_of_word(self, chosen_word):

        self.row = self.create_new_row()

        self.result_dataframe.add_word_to_result_dataframe(chosen_word)

        self.word_result_combinations.check_for_invalid_word_results(self.result_dataframe.result_dataframe)

        for i in range(0, 243):

            result = self.word_result_combinations.result_combinations.loc[i, 'result']
            is_valid = self.if_result_is_invalid_add_no_indexes(result)

            if not is_valid:
                continue

            self.add_word_indexes_of_words_matching_to_result(result)

        self.perform_row_length_check()

        np.save(f'word_sample_files/row_1000.npy',
                self.row)
        self.add_row_to_matching_word_array(chosen_word)

    @staticmethod
    def create_new_row():

        # Each set of word index has -1 at either end
        row = np.array([-1]).astype('int16')
        return row

    def if_result_is_invalid_add_no_indexes(self, result):

        word_result_combinations = self.word_result_combinations.result_combinations

        is_valid = word_result_combinations.loc[word_result_combinations['result'] == result, 'validity'].values[0]

        if not is_valid:

            self.add_separator_to_previous_result_word_indexes()

        return is_valid

    def add_separator_to_previous_result_word_indexes(self):

        separator = -1
        self.row = np.concatenate((self.row, separator), axis=None)

    def add_word_indexes_of_words_matching_to_result(self, result):

        self.result_dataframe.add_result_and_letter_count_to_result_dataframe(result)

        filtered_word_indexes = self.word_filter.get_indexes_of_words_that_meet_result_condition(self.word_dataframe,
                                                                                                 self.result_dataframe.
                                                                                                 result_dataframe)

        self.add_word_indexes_to_row(filtered_word_indexes)

    def get_index_of_filtered_words(self, result_filter):

        filtered_word_indexes = self.word_dataframe[result_filter].index.to_numpy()
        return filtered_word_indexes

    def add_word_indexes_to_row(self, filtered_word_indexes):

        self.row = np.concatenate((self.row, filtered_word_indexes), axis=None)
        self.add_separator_to_previous_result_word_indexes()

    def add_row_to_matching_word_array(self, chosen_word):

        row_index = self.get_word_row_index(chosen_word)

        self.matching_words_array[row_index] = self.row

    def get_word_row_index(self, chosen_word):

        row_index = self.word_dataframe.index[self.word_dataframe['words'] == chosen_word][0]

        return row_index

    def perform_row_length_check(self):

        if len(self.row) - 243 - 1 != 12_972:

            print(f'ERROR - Expected {len(self.word_dataframe)} word indexes, got {len(self.row) - 243 - 1}')
            exit()

