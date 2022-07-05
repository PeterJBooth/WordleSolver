import numpy as np
import pandas as pd


class BestGuessFinder:

    def __init__(self):

        self.remaining_words_count = 12_972
        self.best_guess_dataframe = self.create_best_guess_dataframe()
        self.word_removed_count = [0] * 12_972

    @staticmethod
    def create_best_guess_dataframe():
        result_dataframe = pd.DataFrame(data={'Best Guesses': [''] * 10,
                                              ' % of Words Removed': [''] * 10,
                                              '     Possible Answers': [''] * 10,
                                              '% of Words Removed': [''] * 10},
                                        index=([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        return result_dataframe

    def get_best_guesses(self, matching_words_array, word_dataframe):

        self.get_number_of_remaining_words(matching_words_array)

        self.get_ten_best_guesses(matching_words_array, word_dataframe)
        self.get_ten_best_possible_answers(matching_words_array, word_dataframe)

        return self.best_guess_dataframe

    def get_ten_best_guesses(self, matching_words_array, word_dataframe):

        for i in range(len(word_dataframe)):
            self.word_removed_count[i] = self.get_expected_number_of_words_removed(matching_words_array[i])

        self.add_best_guesses_and_their_scores_to_best_guess_df(word_dataframe)

    def get_number_of_remaining_words(self, matching_words_array):

        self.remaining_words_count = matching_words_array.shape[1] - 244

    def add_best_guesses_and_their_scores_to_best_guess_df(self, word_dataframe):

        for position in range(1, 11):

            best_guess_index = self.word_removed_count.index(max(self.word_removed_count))

            self.add_guess_to_best_guess_df(best_guess_index, word_dataframe, position)
            self.add_guess_score_to_best_guess_df(best_guess_index, position)

            self.word_removed_count[best_guess_index] = 0

    def add_guess_to_best_guess_df(self, best_guess_index, word_dataframe, position):

        word = word_dataframe.loc[best_guess_index, 'words']
        self.best_guess_dataframe.loc[position, 'Best Guesses'] = word

    def add_guess_score_to_best_guess_df(self, best_guess_index, position):

        words_removed_percentage = \
            self.word_removed_count[best_guess_index] / self.remaining_words_count * 100
        self.best_guess_dataframe.loc[position, ' % of Words Removed'] = words_removed_percentage

    def get_expected_number_of_words_removed(self, row):

        word_count_for_each_result = self.get_word_count_for_each_result(row)

        expected_number_of_words_removed = \
            self.calculate_expected_number_of_words_removed(word_count_for_each_result)

        return expected_number_of_words_removed

    def get_word_count_for_each_result(self, row):

        minus_positions = self.get_indexes_of_minus_ones(row)
        word_count_for_each_result = self.calculate_word_count_for_each_result(minus_positions)

        return word_count_for_each_result

    @staticmethod
    def get_indexes_of_minus_ones(row):

        minus_positions = np.where(row == -1)[0]
        return minus_positions

    @staticmethod
    def calculate_word_count_for_each_result(minus_positions):

        # Get number of word indexes between each -1 indexes
        # This gives you for each result, the number of words matching that result

        word_count_for_each_result = np.subtract(minus_positions[1:], (minus_positions[:-1] + 1))
        return word_count_for_each_result

    def calculate_expected_number_of_words_removed(self, word_count_for_each_result):

        total_number_of_words = self.remaining_words_count

        # The equation used to calculate expected number of words removed is:
        # total_number_of_words - sum(word_count[0]^2 + word_count[1]^2 +...+ word_count[n]^2 +) / total_number_of_words

        # Derived from: expected number of words removed = p_1*n_1 + p_2*n_2 + ... + p_n * n_n
        # Where:
        # p = probability of getting word result
        # n = number of words removed if result occurred

        word_counts_squared = np.square(word_count_for_each_result)
        expected_number_of_words_removed = total_number_of_words - sum(word_counts_squared) / total_number_of_words
        return expected_number_of_words_removed

    def get_ten_best_possible_answers(self, matching_words_array, word_dataframe):

        self.get_number_of_words_removed_for_all_possible_answers(matching_words_array, word_dataframe)
        self.add_best_possible_answer_and_their_scores_to_best_guess_df(word_dataframe)

    def get_number_of_words_removed_for_all_possible_answers(self, matching_words_array, word_dataframe):

        for i in range(len(word_dataframe)):

            is_possible_answer = matching_words_array[i][-2] != -1  # if -1 for that word there is no GGGGG result
            if is_possible_answer:
                self.word_removed_count[i] = self.get_expected_number_of_words_removed(matching_words_array[i])
            else:
                self.word_removed_count[i] = 0

    def add_best_possible_answer_and_their_scores_to_best_guess_df(self, word_dataframe):

        for position in range(1, 11):

            best_guess_index = self.word_removed_count.index(max(self.word_removed_count))

            self.add_possible_answer_to_best_guess_df(best_guess_index, word_dataframe, position)
            self.add_possible_answer_score_to_best_guess_df(best_guess_index, position)

            self.word_removed_count[best_guess_index] = 0

    def add_possible_answer_to_best_guess_df(self, best_guess_index, word_dataframe, position):

        word = word_dataframe.loc[best_guess_index, 'words']
        self.best_guess_dataframe.loc[position, '     Possible Answers'] = word

    def add_possible_answer_score_to_best_guess_df(self, best_guess_index, position):

        words_removed_percentage = \
            self.word_removed_count[best_guess_index] / self.remaining_words_count * 100
        self.best_guess_dataframe.loc[position, '% of Words Removed'] = words_removed_percentage

    def get_answer_if_solved(self, matching_words_array, word_dataframe):

        self.get_number_of_remaining_words(matching_words_array)
        answer, is_solved = self.if_one_word_remains_get_word(matching_words_array, word_dataframe)

        return answer, is_solved

    def if_one_word_remains_get_word(self, matching_words_array, word_dataframe):

        if self.remaining_words_count == 1:

            is_solved = True

            answer_index = matching_words_array[matching_words_array != -1][0]
            answer = word_dataframe.loc[answer_index, 'words']

        else:

            is_solved = False
            answer = '_____'

        return answer, is_solved
