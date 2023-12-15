#Define function,Get coloumn names from a csv file
import csv
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    f = open('data.csv')
    data = csv.reader(f)

    names = []
    for row in data:
        names.append(row[1])

    return names
    
# Read the csv file