import matplotlib.pyplot as plt
import numpy as np
from retrieve_user_json import get_json

def probs_to_arr(a_list: list) -> np.ndarray:
    '''Appends the probabilities to a numpy array'''

    arr = np.array([])

    for i in a_list:
        arr = np.append(arr, i["weight"])

    return arr

def plot_probs(arr: np.ndarray) -> plt.figure:
    '''Plots the number of titles (x-axis) vs. the probabilities (y-axis)'''

    title_num = np.arange(arr.shape[0])

    plt.figure()
    plt.title(r'Title Probabilities vs. Number of Titles')
    plt.xlabel(r'Title No.')
    plt.ylabel(r'Probabilities')
    plt.plot(title_num, arr, ls='', marker='o', ms=0.6)
    plt.show()

if __name__ == "__main__":
    prob_dict_list = get_json("ed05c06f79baa07b")
    probabilities = probs_to_arr(prob_dict_list)
    plot_probs(probabilities)
