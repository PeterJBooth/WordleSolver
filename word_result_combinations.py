import pandas as pd


class WordResultCombinations:

    def __init__(self):

        self.result_combinations = self.create_word_result_combinations()

    @staticmethod
    def create_word_result_combinations():

        results_combinations_list = []

        for letter_0 in ['B', 'O', 'G']:
            for letter_1 in ['B', 'O', 'G']:
                for letter_2 in ['B', 'O', 'G']:
                    for letter_3 in ['B', 'O', 'G']:
                        for letter_4 in ['B', 'O', 'G']:
                            result = letter_0 + letter_1 + letter_2 + letter_3 + letter_4
                            results_combinations_list.append(result)

        results_combinations = pd.DataFrame(data={'result': results_combinations_list, 'validity': [True] * 243})

        return results_combinations

    def check_for_invalid_word_results(self, result_df):

        self.set_all_result_combinations_to_valid()

        non_unique_letters = self.get_non_unique_letters_from_word(result_df)

        for letter in non_unique_letters:

            self.check_for_invalid_result_for_letter(letter, result_df)

    def set_all_result_combinations_to_valid(self):

        self.result_combinations = self.result_combinations.assign(validity='true')

    @staticmethod
    def get_non_unique_letters_from_word(result_df):

        duplicated_letters = result_df[result_df.duplicated('letters', keep='first')]['letters'].unique()
        return duplicated_letters

    def check_for_invalid_result_for_letter(self, letter, result_df):

        letter_indexes = result_df.loc[result_df['letters'] == letter].index

        for row in self.result_combinations.index:

            self.check_if_result_is_valid(row, letter_indexes)

    def check_if_result_is_valid(self, row, letter_indexes):

        letter_results = self.get_results_of_letter(row, letter_indexes)

        if (letter_results.count('O') == 0) or (letter_results.count('B') == 0):
            return

        first_B_index = self.get_index_of_first_B_in_list_of_letter_results(letter_results)
        last_O_index = self.get_index_of_last_O_in_list_of_letter_results(letter_results)

        if last_O_index > first_B_index:

            self.result_combinations.loc[row, 'validity'] = False

    def get_results_of_letter(self, row, letter_indexes):

        result = self.result_combinations.loc[row, 'result']

        letter_result = [result[letter_index] for letter_index in letter_indexes]

        return letter_result

    @staticmethod
    def get_index_of_first_B_in_list_of_letter_results(letter_results):

        return letter_results.index('B')

    @staticmethod
    def get_index_of_last_O_in_list_of_letter_results(letter_results):

        last_O_index = len(letter_results) - letter_results[::-1].index('O') - 1
        return last_O_index