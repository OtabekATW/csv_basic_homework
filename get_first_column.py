import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f = open('data.csv')
    data = csv.reader(f)

    first_column = []
    for row in data:
        first_column.append(row[0])
    
    return first_column
    
# Read the csv file