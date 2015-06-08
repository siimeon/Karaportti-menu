from json_lib import obj_to_json, json_to_obj
from date_modifcator import modify_dates
import urllib2

salad = "LOUNASSALAATTI"

def get_menus(obj):
    menus = obj["MenusForDays"]
    weeks_menu = {}
    for menu in menus:
        menu["Date"] = modify_dates(date_transformation(menu["Date"]))
        if len(menu["SetMenus"]) != 0:
            menu_obj = make_menu_list_obj(menu["Date"], menu["SetMenus"])
            weeks_menu[menu["Date"]] = menu_obj
    return weeks_menu

def date_transformation(date):
    date = date.split("T")[0]
    date_array = date.split("-")
    return date_array[2] + "." + date_array[1] + "." + date_array[0]

def price_modification(price_str):
    # Price': u'Nokia 6,20 \u20ac/6,65 \u20ac Ext 8,90 \u20ac/9,20 \u20ac
    result = {"Nokia Price": None, "Price": None}
    str_array = price_str.split(" ")
    if len(str_array) == 6:
        result["Nokia Price"] = str_array[1] + u" \u20AC/kg"
        result["Price"] = str_array[4] + u" \u20AC/kg"
    elif len(str_array) == 8:
        result["Nokia Price"] = str_array[1] + u" \u20AC"
        result["Price"] = str_array[5] + u" \u20AC"
    return result

def make_menu_list_obj(date, menu_obj):
    obj = {"date": date,
           "list": []}
    for i in menu_obj:
        result = {"Allergies": None,
                  "Name": None,
                  "Nokia Price": None,
                  "Price": None}
        if i["Name"] == salad:
            result["Name"] = "Salaatti: " + ", ".join(i["Components"])
            price = price_modification(i["Price"])
            result["Nokia Price"] = price["Nokia Price"]
            result["Price"] = price["Price"]
        else:
            result["Name"] = ", ".join(i["Components"])
            price = price_modification(i["Price"])
            result["Nokia Price"] = price["Nokia Price"]
            result["Price"] = price["Price"]
        obj["list"].append(result)
    return obj

def amica_to_json():
    url = "http://www.amica.fi/modules/json/json/Index?costNumber=3205&language=fi"
    # Next line is for demo and testing while development
    # url = "http://www.amica.fi/modules/json/json/Index?costNumber=3205&language=fi&firstDay=2015-6-1"
    url_data = urllib2.urlopen(url).read()
    obj = json_to_obj(url_data)
    obj = get_menus(obj)
    json_obj = obj_to_json(obj)
    return json_obj

def main():
    json_obj = amica_to_json()
    print(json_obj)


if __name__ == "__main__":
    main()
