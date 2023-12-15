import csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    f = open('data.csv')
    data = csv.reader(f)

    number_of_rows = []
    n = 0
    for row in list(data):
        number_of_rows.append(row[0])
        n += 1

    return n

# Read the csv file