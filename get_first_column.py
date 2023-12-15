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
    for i in data:
        temp = (', '.join(i)).split(',')
        first_column.append(temp[0])
    
    return first_column
    
# Read the csv file