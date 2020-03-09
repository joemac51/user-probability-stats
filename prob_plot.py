import requests
import matplotlib.pyplot as plt
import numpy as np

def get_json(user_id: str) -> list:
    '''Returns a list of dicts containing TMSID and their corresponding probabilities
    for the user's top 1000 of titles'''

    try:
        r = requests.get(f"http://movie-demo-daniel.davidmcgettigan.com/getlistforusernormnew/{user_id}")

        return r.json()
    except:
        print("User not present")
        
        return []

prob_dict_list = get_json("ed05c06f79baa07b")

def probs_to_arr(a_list: list) -> np.ndarray:
    '''Appends the probabilities to a numpy array'''

    arr = np.array([])

    for i in a_list:
        arr = np.append(arr, i["weight"])

    return arr

probabilities = probs_to_arr(prob_dict_list)

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
    plot_probs(probabilities)
