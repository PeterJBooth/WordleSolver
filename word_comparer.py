import pandas as pd


class WordComparer:

    def __init__(self):

        self.chosen_word = ''
        self.result = None

    def compare_chosen_word_with_answer(self, chosen_word, answer):

        self.chosen_word = chosen_word
        self.setup_result_dataframe()

        self.categorise_letter_into_black_orange_or_green(answer)
        self.count_number_of_observed_occurrences_of_all_letters_in_answer()

        is_solved = self.check_if_solved(answer)

        return self.result, is_solved

    def setup_result_dataframe(self):

        self.result = pd.DataFrame(data={'letters': [letter for letter in self.chosen_word],
                                         'letter_result': [''] * len(self.chosen_word),
                                         'letter_count': [0] * len(self.chosen_word)}, )

    def categorise_letter_into_black_orange_or_green(self, answer):

        for i, letter in enumerate(self.chosen_word):

            if answer.count(letter) == 0:

                self.result.loc[i, 'letter_result'] = 'B'

            elif letter != answer[i]:

                self.result.loc[i, 'letter_result'] = 'O'

            elif letter == answer[i]:

                self.result.loc[i, 'letter_result'] = 'G'

            else:
                print("Error: Failed to compare chosen word with answer")

        self.undo_letters_being_counted_multiple_times_for_one_letter(answer)

    def undo_letters_being_counted_multiple_times_for_one_letter(self, answer):

        unique_letters = self.get_unique_letters_from_word()
        for letter in unique_letters:
            self.if_excess_orange_letters_remove_excess(letter, answer)

    def get_unique_letters_from_word(self):

        unique_letters = self.result[~self.result.duplicated('letters', keep='first')]['letters']

        return unique_letters

    def if_excess_orange_letters_remove_excess(self, letter, answer):

        if answer.count(letter) > 0:

            number_of_excess_orange_letters = self.chosen_word.count(letter) - answer.count(letter)
            if number_of_excess_orange_letters > 0:
                self.remove_excess_orange_letters(letter, number_of_excess_orange_letters)

    def remove_excess_orange_letters(self, letter, number_of_excess_orange_letters):

        results_for_letter = self.result.loc[self.result['letters'].str.contains(letter), 'letter_result']
        indexes_of_orange_letter = results_for_letter[results_for_letter.str.contains('O')].index

        # Turn the last Orange indexes into Black
        indexes_of_excess_orange_letters = [indexes_of_orange_letter[-i]
                                            for i in range(1, number_of_excess_orange_letters + 1)]

        self.result.loc[indexes_of_excess_orange_letters, 'letter_result'] = 'B'

    def count_number_of_observed_occurrences_of_all_letters_in_answer(self):

        unique_letters = self.get_unique_letters_from_word()

        for letter in unique_letters:

            number_of_green_and_orange_results = self.count_number_of_green_and_orange_results(letter)
            self.add_number_to_letter_count_column(number_of_green_and_orange_results, letter)

    def count_number_of_green_and_orange_results(self, letter):

        number_of_green_and_orange_results = len(self.result[(self.result['letters'] == letter) &
                                                 ((self.result['letter_result'] == 'O') |
                                                 (self.result['letter_result'] == 'G'))])

        return number_of_green_and_orange_results

    def add_number_to_letter_count_column(self, number_of_green_and_orange_results, letter):

        self.result.loc[self.result['letters'] == letter, 'letter_count'] = number_of_green_and_orange_results

    def check_if_solved(self, answer):

        return self.chosen_word == answer

