
def modify_dates(date):
    date_array = date.split(".")
    if date_array[0][0] == "0":
        date_array[0] = date_array[0][1]
    if date_array[1][0] == "0":
        date_array[1] = date_array[1][1]
    return ".".join(date_array)
