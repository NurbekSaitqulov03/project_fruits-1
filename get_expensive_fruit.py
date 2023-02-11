import csv
def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    # your code here
    data = csv.reader(data, delimiter=',')
    a = []
    for i in data:
        if not i[1].isalpha():
            a.append(float(i[1]))
    mx = a[0]
    for i in a[1:]:
        if i>mx:
            mx = i
    return mx


f = open('fruits.csv', 'r')
print(get_expensive_fruit(f))