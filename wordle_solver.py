import pandas as pd
from wordle_solver_interface import WordleSolverInterface
from word_filter import WordFilter
from best_guess_finder import BestGuessFinder
from word_comparer import WordComparer
from result_dataframe import ResultDataframe
from load_matching_array import load_matching_array


class WordleSolver:

    def __init__(self):

        file_path = "word_sample_files/wordle_words.txt"
        self.dictionary = pd.read_csv(file_path, sep=',    ', delimiter=None, header=None, names=['words'],
                                      index_col=None, usecols=None, engine='python', encoding='utf8')

        self.word_dataframe = pd.DataFrame(self.dictionary.copy())

        self.user_interface = WordleSolverInterface()
        self.best_guess_finder = BestGuessFinder()
        self.word_comparer = WordComparer()
        self.word_filter = WordFilter()
        self.result_dataframe = ResultDataframe()
        self.matching_word_array = load_matching_array()

    def setup_and_run_user_input_program(self):

        self.user_interface.display_program_title_and_instructions()
        self.run_user_input_program()

    def run_user_input_program(self):

        answer, is_solved = self.best_guess_finder.get_answer_if_solved(self.matching_word_array, self.word_dataframe)

        if is_solved:
            self.user_interface.display_answer(answer)
            return

        best_guesses = self.best_guess_finder.get_best_guesses(self.matching_word_array, self.word_dataframe)
        self.user_interface.display_top_10_best_guesses(best_guesses)

        chosen_word = self.user_interface.get_chosen_word_from_user(self.word_dataframe)
        result = self.user_interface.get_word_result_from_user()

        result_dataframe = self.result_dataframe.create_dataframe_with_result_and_letter_counts(chosen_word, result)

        self.matching_word_array = self.word_filter.remove_words_from_array_not_meeting_condition(
            self.word_dataframe, result_dataframe, self.matching_word_array)

        print()
        print(f'{self.matching_word_array.shape[1] - 244} Words remaining!')
        print()

        self.run_user_input_program()

    def run_automatic_program(self, answer):

        is_solved = False

        best_guess = 'talks'

        # while not is_solved:
        for i in range(1):

            result, is_solved = self.word_comparer.compare_chosen_word_with_answer(best_guess, answer)
            print(self.matching_word_array)

            string_result = input('Type Result: ')
            self.matching_word_array = self.word_filter.remove_words_from_array_not_meeting_condition(
                self.word_dataframe, result, self.matching_word_array)

            print(self.matching_word_array)

            print(self.matching_word_array.shape)
            best_guess = self.best_guess_finder.get_best_guess(self.matching_word_array, self.word_dataframe)
            print(best_guess)
            if is_solved:
                break


if __name__ == '__main__':

    wordle_solver = WordleSolver()
    wordle_solver.setup_and_run_user_input_program()
