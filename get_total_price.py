import csv
def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    data = csv.reader(data, delimiter=',')
    x = 0
    for i in data:
        if not i[1].isalpha():
            x += float(i[1])
    return x
    
f = open('fruits.csv', 'r')
print(get_total_price(f))