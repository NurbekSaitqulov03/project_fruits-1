import csv
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    data = csv.reader(data, delimiter=',')
    x = []
    for i in data:
        x.append(i[0])
    return x[1:]

f = open('fruits.csv', 'r')
print(get_frutis_name(f))