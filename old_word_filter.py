class OldWordFilter:

    def __init__(self, word_dataframe):

        self.word_dataframe = word_dataframe

    def filter_out_words_based_on_result(self, word, result):

        for letter_position in range(len(word)):

            letter = word[letter_position]
            self.check_if_letter_is_black_orange_or_green(letter, result, letter_position)

        return self.word_dataframe

    def check_if_letter_is_black_orange_or_green(self, letter, result, letter_position):

        letter_result = result.loc[letter_position, 'letter result']

        if letter_result == 'B':
            self.make_letter_black(letter, letter_position, result)

        if letter_result == 'O':
            self.make_letter_orange(letter, letter_position, result)

        if letter_result == 'G':
            self.make_letter_green(letter, letter_position)

    def make_letter_black(self, letter, letter_position, result):

        letter_count = self.get_number_of_observed_occurrences_of_letter_in_answer(result, letter_position)
        is_in_answer = self.check_if_letter_is_in_answer(letter_count)

        if is_in_answer:

            self.remove_words_containing_letter_over_letter_count_amount(letter, letter_count)
            self.remove_words_containing_letter_in_incorrect_position(letter, letter_position)
            return

        self.remove_words_containing_letter(letter)

    @staticmethod
    def get_number_of_observed_occurrences_of_letter_in_answer(result, letter_position):

        letter_count = result.loc[letter_position, 'letter count']
        return letter_count

    @staticmethod
    def check_if_letter_is_in_answer(letter_count):

        is_in_answer = letter_count > 0
        return is_in_answer

    def remove_words_containing_letter_over_letter_count_amount(self, letter, letter_count):

        letter_filter = self.word_dataframe['words'].apply(
            lambda word: True if word.count(letter) > letter_count else False)

        self.word_dataframe = self.word_dataframe.drop(self.word_dataframe[letter_filter].index)

    def remove_words_containing_letter_in_incorrect_position(self, letter, position):

        letter_filter = self.word_dataframe['words'].apply(
            lambda word: True if word[position].count(letter) == 1 else False)

        self.word_dataframe = self.word_dataframe.drop(self.word_dataframe[letter_filter].index)

    def remove_words_containing_letter(self, letter):

        letter_filter = self.word_dataframe['words'].apply(lambda word: True if word.count(letter) > 0 else False)

        # print(self.word_dataframe)
        self.word_dataframe = self.word_dataframe.drop(self.word_dataframe[letter_filter].index)

    def make_letter_orange(self, letter, position, result):

        letter_count = self.get_number_of_observed_occurrences_of_letter_in_answer(result, position)
        self.remove_words_containing_letter_under_letter_count_amount(letter, letter_count)
        self.remove_words_containing_letter_in_incorrect_position(letter, position)

    def remove_words_containing_letter_under_letter_count_amount(self, letter, letter_count):

        letter_filter = self.word_dataframe['words'].apply(
            lambda word: True if word.count(letter) < letter_count else False)

        self.word_dataframe = self.word_dataframe.drop(self.word_dataframe[letter_filter].index)

    def make_letter_green(self, letter, position):

        self.remove_words_not_containing_letter_in_correct_position(letter, position)

    def remove_words_not_containing_letter_in_correct_position(self, letter, position):

        letter_filter = self.word_dataframe['words'].apply(
            lambda word: True if word[position].count(letter) == 0 else False)

        self.word_dataframe = self.word_dataframe.drop(self.word_dataframe[letter_filter].index)

# Check orange filter is ok
