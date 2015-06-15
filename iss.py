from bs4 import BeautifulSoup
from json_lib import obj_to_json
import re
import urllib2

lines_to_be_removed = ["Diet",
                       "Hinta",
                       "Nokia",
                       "Maanantai / Monday",
                       "Tiistai / Tuesday",
                       "Keskiviikko / Wednesday",
                       "Torstai / Thursday",
                       "Perjantai / Friday",
                       u"G=Glutein free, M=Milk free, VL=Low lactose, L=Lactose free / G=Gluteeniton, M=Maidoton, "
                       u"VL=V\u00E4h\u00E4laktoosinen, L=Laktoositon",
                       u"K\u00E4yk\u00E4\u00E4 p\u00F6yt\u00E4\u00E4n!",
                       "Bon apetit!"]
themes = ["Home cooking",
          "Energy -boost",
          "Vegetarian",
          "Salad",
          "Soup",
          "Theme",
          "Bistro",
          "Dessert"]
lines_to_be_removed += themes

def prettify_html(html_string):
    return BeautifulSoup(html_string).prettify()


def get_tag_content(tag, source):
    inside_tag = False
    data = []
    source_list = source.split("\n")
    for line in source_list:
        if inside_tag:
            data.append(line)
        if tag in line:
            if inside_tag:
                inside_tag = False
                data.pop()
            else:
                inside_tag = True
    return "\n".join(data)


def filter_out_tags(source):
    source_lines = source.split("\n")
    data = []
    for line in source_lines:
        if "<" not in line:
            data.append(line.strip().lstrip())
    return "\n".join(data)


def is_date(line):
    date_expression1 = "\d\d*.\d\d*.\d\d\d\d"
    if re.match(date_expression1, line) is not None:
        return True
    return False


def group_data(array):
    data = []
    temp = []
    for line in array:
        if is_date(line):
            data.append(temp)
            temp = [line]
        else:
            temp.append(line)
    data.append(temp)
    return data


def organize(week_array):
    data = {"Maanantai / Monday": {},
            "Tiistai / Tuesday": {},
            "Keskiviikko / Wednesday": {},
            "Torstai / Thursday": {},
            "Perjantai / Friday": {}}
    for day_array in week_array:
        if len(day_array) > 5:
            first = False
            date_boolean = True
            weekday_boolean = False
            date = None
            weekday = None
            master_tmp = []
            tmp = []
            for line in day_array:
                if date_boolean:
                    date = line
                    date_boolean = False
                    weekday_boolean = True
                elif weekday_boolean:
                    weekday = line
                    weekday_boolean = False
                if line not in lines_to_be_removed:
                    if not is_date(line):
                        tmp.append(line)
                # \u20AC is euro sign
                if u"\u20AC" in line:
                    if first:
                        first = False
                        master_tmp.append(tmp)
                        tmp = []
                    else:
                        first = True
            master_tmp.append(tmp)
            data[weekday] = {"date": date, "data": master_tmp}
    return data

def next_organize(data):
    master_list = {}
    for day in data:
        #print(data[day]["date"])
        aa = {"date": data[day]["date"], "list": None}
        list = []
        a = data[day]["data"]
        for i in a:
            dish = {"Name": None,
                    "Allergies": None,
                    "Price": None,
                    "Nokia Price": None}
            if len(i) == 3:
                dish["Name"] = "Salaatti:" + i[0].split("/")[0]
            else:
                dish["Name"] = i[0].split("/")[0]
            if len(i) != 2 and len(i) > 2:
                dish["Nokia Price"] = i.pop()
                dish["Price"] = i.pop()
            if len(i) == 2 or len(i) == 4:
                dish["Allergies"] = i[1]
            list.append(dish)
        aa["list"] = list
        master_list[aa["date"]] = aa
    return master_list


def iss_to_json():
    url = "http://www.fi.issworld.com/fi-FI/palvelumme-service/ruokailupalvelut/ravintolat/midpoint-ruokalistasivu"
    html_data = urllib2.urlopen(url).read()
    html_data = prettify_html(html_data)
    tbody_data = get_tag_content("tbody", html_data)
    menu_data = filter_out_tags(tbody_data)
    menu_data = group_data(menu_data.split("\n"))
    menu_data = organize(menu_data)
    menu_data = next_organize(menu_data)
    menu_json = obj_to_json(menu_data)
    return menu_json


def main():
    menu_json = iss_to_json()
    print(menu_json)


if __name__ == "__main__":
    main()
