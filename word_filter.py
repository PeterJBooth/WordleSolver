import numpy as np


class WordFilter:

    def get_indexes_of_words_that_meet_result_condition(self, word_dataframe, result_dataframe):

        check_if_word_meet_result_conditions = self.create_function_that_makes_conditional_from_result(result_dataframe)

        result_filter = word_dataframe['words'].apply(lambda word: check_if_word_meet_result_conditions(word))

        filtered_word_indexes = word_dataframe[result_filter].index.to_numpy()

        return filtered_word_indexes

    def create_function_that_makes_conditional_from_result(self, result_dataframe):

        function_dictionary = self.create_function_dictionary()

        for letter_position in range(5):

            function_dictionary[letter_position] = \
                self.get_B_O_or_G_conditional_function_based_on_letter_result(result_dataframe, letter_position)

        def check_if_word_meet_conditions_of_chosen_word_result(dataframe_word):

            conditional = function_dictionary[0](dataframe_word)
            if not conditional:
                return conditional

            conditional = function_dictionary[1](dataframe_word)
            if not conditional:
                return conditional

            conditional = function_dictionary[2](dataframe_word)
            if not conditional:
                return conditional

            conditional = function_dictionary[3](dataframe_word)
            if not conditional:
                return conditional

            conditional = function_dictionary[4](dataframe_word)
            return conditional

        return check_if_word_meet_conditions_of_chosen_word_result

    @staticmethod
    def create_function_dictionary():

        function_dictionary = {0: None, 1: None, 2: None, 3: None, 4: None}
        return function_dictionary

    @staticmethod
    def get_letter_and_letter_result_and_letter_count(result_dataframe, letter_position):

        letter = result_dataframe.loc[letter_position, 'letters']
        letter_result = result_dataframe.loc[letter_position, 'letter_result']
        letter_count = result_dataframe.loc[letter_position, 'letter_count']
        return letter, letter_result, letter_count

    def get_B_O_or_G_conditional_function_based_on_letter_result(self, result_dataframe, letter_position):

        letter, letter_result, letter_count = self.get_letter_and_letter_result_and_letter_count(result_dataframe,
                                                                                                 letter_position)

        if letter_result == 'B':

            function_for_checking_if_word_meets_B_condition = \
                self.create_function_for_checking_if_word_meets_B_condition(letter, letter_count, letter_position)

            return function_for_checking_if_word_meets_B_condition

        elif letter_result == 'O':

            function_for_checking_if_word_meets_O_condition = \
                self.create_function_for_checking_if_word_meets_O_condition(letter, letter_count, letter_position)

            return function_for_checking_if_word_meets_O_condition

        elif letter_result == 'G':

            function_for_checking_if_word_meets_G_condition = \
                self.create_function_for_checking_if_word_meets_G_condition(letter, letter_position)

            return function_for_checking_if_word_meets_G_condition

    @staticmethod
    def create_function_for_checking_if_word_meets_B_condition(letter, letter_count, letter_position):

        if letter_count == 0:

            def check_if_word_meets_B_condition(word):

                black_conditional = word.count(letter) == 0
                return black_conditional

            return check_if_word_meets_B_condition

        elif letter_count > 0:

            def check_if_word_meets_B_with_letter_count_more_than_1_condition(word):

                # True if amount of that letter is equal to amount in answer and letter is not in described position
                black_conditional = (word.count(letter) == letter_count) & (word[letter_position].count(letter) == 0)
                return black_conditional

            return check_if_word_meets_B_with_letter_count_more_than_1_condition

    @staticmethod
    def create_function_for_checking_if_word_meets_O_condition(letter, letter_count, letter_position):

        def check_if_word_meets_O_condition(word):
            # True if number of letter is equal or more than letter count and letter is not in described position
            orange_conditional = (word.count(letter) >= letter_count) & (word[letter_position].count(letter) == 0)
            return orange_conditional

        return check_if_word_meets_O_condition

    @staticmethod
    def create_function_for_checking_if_word_meets_G_condition(letter, letter_position):

        def check_if_word_meets_G_condition(word):
            green_conditional = word[letter_position].count(letter) == 1
            return green_conditional

        return check_if_word_meets_G_condition

    def remove_words_from_array_not_meeting_condition(self, word_dataframe, result_dataframe, matching_words_array):

        word_indexes_not_meeting_condition = self.get_indexes_of_words_not_meeting_condition_of_result(word_dataframe,
                                                                                                       result_dataframe)

        matching_words_array = self.remove_word_indexes_from_array(matching_words_array,
                                                                   word_indexes_not_meeting_condition)

        return matching_words_array

    def get_indexes_of_words_not_meeting_condition_of_result(self, word_dataframe, result_dataframe):

        check_if_word_meet_result_conditions = self.create_function_that_makes_conditional_from_result(result_dataframe)

        result_filter = word_dataframe['words'].apply(lambda word: check_if_word_meet_result_conditions(word))

        not_filtered_word_indexes = word_dataframe[~ result_filter].index.to_numpy()

        return not_filtered_word_indexes

    @staticmethod
    def remove_word_indexes_from_array(matching_words_array, word_indexes):

        contains_word_index_mask = np.isin(matching_words_array, word_indexes)
        matching_words_array = matching_words_array[~contains_word_index_mask]
        matching_words_array = matching_words_array.reshape((12_972, -1))

        return matching_words_array
