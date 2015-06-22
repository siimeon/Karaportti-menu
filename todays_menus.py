from amica import amica_to_json
from iss import iss_to_json
from date_modifcator import modify_dates
from json_lib import json_to_obj, obj_to_json
import time


def get_today_str():
    date = time.strftime("%d.%m.%Y")
    return modify_dates(date)


def load_menus():
    amica_menu = json_to_obj(amica_to_json())
    #iss_menu = json_to_obj(iss_to_json())
    today = get_today_str()
    amica_today = amica_menu[today]
    #iss_today = iss_menu[today]
    return {"amica": amica_today, "iss": None}

def print_menus(today_obj):
    amica = today_obj["amica"]
    #iss = today_obj["iss"]
    for dish in amica["list"]:
        if dish["Nokia Price"] is not None:
            print(dish["Name"] + " " + dish["Nokia Price"])
        else:
            print(dish["Name"])
    """
    for dish in iss["list"]:
        if dish["Nokia Price"] is not None:
            print(dish["Name"] + " " + dish["Nokia Price"])
        else:
            print(dish["Name"])
    """

def main():
    print(obj_to_json(load_menus()))

if __name__ == "__main__":
    main()
