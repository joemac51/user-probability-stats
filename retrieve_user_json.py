import requests
import json
import sys

FILE_PATH = "/Users/daniel/Documents/AREA 22/user-prob-stats/prob_json"
MY_USER_ID = "ed05c06f79baa07b"

def get_json(user_id: str) -> list:
    '''Returns a list of dicts containing TMSID and their corresponding probabilities
    for the user's top 1000 of titles'''

    try:
        r = requests.get(f"https://optik-prod-node-lb.area22.info/getlistforusernormnew/{user_id}")

        return r.json()
    except:
        print("User not present")
        
        return []

def save_json_to_file(user_json: list, file_no: int) -> None:
    '''Serializes user_json list to file number file_no'''

    with open(f"{FILE_PATH}/{str(file_no)}.json", "w") as write_file:
        json.dump(user_json, write_file)

if __name__ == "__main__":
    my_json = get_json(MY_USER_ID)
    save_json_to_file(my_json, sys.argv[1])
