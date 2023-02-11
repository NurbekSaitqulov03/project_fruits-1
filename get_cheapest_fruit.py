import csv
def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
    data = csv.reader(data, delimiter=',')
    a = []
    for i in data:
        if not i[1].isalpha():
            a.append(float(i[1]))
    mx = a[0]
    for i in a[1:]:
        if i<mx:
            mx = i
    return mx
f = open('fruits.csv', 'r')
print(get_cheapest_fruit(f))