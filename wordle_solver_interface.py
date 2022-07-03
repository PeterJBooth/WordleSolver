import pandas as pd


class WordleSolverInterface:

    @staticmethod
    def display_program_title_and_instructions():

        title_and_instructions = """
########################################################################################################################
                                                    WORDLE SOLVER
########################################################################################################################

Black  (B) - The letter isn't in the word
Orange (O) - The letter is in the word but in the wrong place
Green  (G) - The letter is in the word and in the right place
"""

        print(title_and_instructions)

    @staticmethod
    def display_top_10_best_guesses(guess_df):

        print(" The top ten guesses are the following")
        pd.set_option('display.max_columns', None)
        print(guess_df[::-1])


    @staticmethod
    def display_best_guess(word):
        print(f'The best guess is: {word}')

    def get_chosen_word_from_user(self, word_dataframe):

        chosen_word = input("Type in word you choose to guess: ")
        chosen_word = chosen_word.lower()

        if not word_dataframe['words'].str.contains(chosen_word).any():

            print('Oops that word is not in the list of allowable guesses, try again! ')
            chosen_word = self.get_chosen_word_from_user(word_dataframe)

        return chosen_word

    def get_word_result_from_user(self):

        string_result = input("Type in results (e.g. BGBBO): ")
        string_result = string_result.upper()

        for letter_result in string_result:

            if letter_result not in ['B', 'O', 'G']:
                print('Oops you seemed to have made a mistake, try again! ')
                string_result = self.get_word_result_from_user()
                break

        return string_result

    @staticmethod
    def display_answer(answer):

        answer = answer.upper()
        l0 = answer[0]
        l1 = answer[1]
        l2 = answer[2]
        l3 = answer[3]
        l4 = answer[4]

        print(f"""The answer is:
                                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                          %%%%%% {l0}    {l1}    {l2}    {l3}    {l4} %%%%%%
                                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
              """)
