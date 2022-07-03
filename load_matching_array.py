import numpy as np


def load_matching_array():

    data = np.load('word_sample_files/matching_array.npz')
    arrays = data.files

    matching_word_array = data[arrays[0]]
    return matching_word_array
