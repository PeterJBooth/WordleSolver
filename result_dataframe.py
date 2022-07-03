import pandas as pd


class ResultDataframe:

    def __init__(self):

        self.result_dataframe = self.create_result_dataframe()

    @staticmethod
    def create_result_dataframe():

        result_dataframe = pd.DataFrame(data={'letters': [''] * 5,
                                              'letter_result': [''] * 5,
                                              'letter_count': [0] * 5})

        return result_dataframe

    def add_word_to_result_dataframe(self, word):

        for i in range(5):
            self.result_dataframe.loc[i, 'letters'] = word[i]

    def add_result_and_letter_count_to_result_dataframe(self, result):

        self.add_result_to_result_dataframe(result)
        self.count_number_of_observed_occurrences_of_all_letters_in_answer()


    def add_result_to_result_dataframe(self, result):

        for i in range(5):
            self.result_dataframe.loc[i, 'letter_result'] = result[i]

    def count_number_of_observed_occurrences_of_all_letters_in_answer(self):

        self.set_all_letter_counts_to_0()

        unique_letters = self.get_unique_letters_from_word()

        for letter in unique_letters:
            number_of_green_and_orange_results = self.count_number_of_green_and_orange_results(letter)
            self.add_number_to_letter_count_column(number_of_green_and_orange_results, letter)

    def set_all_letter_counts_to_0(self):

        self.result_dataframe = self.result_dataframe.assign(letter_count=0)

    def get_unique_letters_from_word(self):

        unique_letters = self.result_dataframe[~self.result_dataframe.duplicated('letters', keep='first')]['letters']

        return unique_letters

    def count_number_of_green_and_orange_results(self, letter):

        number_of_green_and_orange_results = len(self.result_dataframe[(self.result_dataframe['letters'] == letter) &
                                                                ((self.result_dataframe['letter_result'] == 'O') |
                                                                 (self.result_dataframe['letter_result'] == 'G'))])

        return number_of_green_and_orange_results

    def add_number_to_letter_count_column(self, number_of_green_and_orange_results, letter):

        self.result_dataframe.loc[self.result_dataframe['letters'] == letter, 'letter_count'] = number_of_green_and_orange_results

    def create_dataframe_with_result_and_letter_counts(self, word, result):

        self.result_dataframe = self.create_result_dataframe()
        self.add_word_to_result_dataframe(word)
        self.add_result_and_letter_count_to_result_dataframe(result)

        return self.result_dataframe