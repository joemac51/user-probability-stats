import matplotlib.pyplot as plt
import numpy as np
import json
import os

MY_USER_ID = "ed05c06f79baa07b"
# FILE_NUM = 1

def get_json_from_file(file_path: str) -> list:
    '''Deserializes a JSON file at file_path'''

    if os.path.exists(file_path):
        with open(file_path, "r") as read_file:
            data = json.load(read_file)

        return data
    else:
        print("File path not found")

        return []

def probs_to_arr(a_list: list) -> np.ndarray:
    '''Appends the probabilities to a numpy array'''

    arr = np.array([])

    for i in a_list:
        arr = np.append(arr, i["weight"])

    return arr

def plot_probs(arr: np.ndarray, fig_num: int) -> plt.figure:
    '''Plots the number of titles (x-axis) vs. the probabilities (y-axis)'''

    title_num = np.arange(arr.shape[0])

    plt.figure()
    plt.title(r'Title Probabilities vs. Number of Titles')
    plt.xlabel(r'Title No.')
    plt.ylabel(r'Probabilities')
    plt.plot(title_num, arr, ls=':', lw=0.4, marker='o', ms=1.1, mec='red', mfc='red')
    plt.savefig(f"/Users/daniel/Documents/AREA 22/user-prob-stats/figures/{fig_num}", dpi=300, bbox_inches='tight')

if __name__ == "__main__":
    for i in range(1, 64):
        prob_dict_list = get_json_from_file(f"/Users/daniel/Documents/AREA 22/user-prob-stats/prob_json/{i}.json")
        probabilities = probs_to_arr(prob_dict_list)
        plot_probs(probabilities, i)
    # prob_dict_list = get_json_from_file("/Users/daniel/Documents/AREA 22/user-prob-stats/prob_json/55.json")
    # probabilities = probs_to_arr(prob_dict_list)
    # plot_probs(probabilities, 1)
