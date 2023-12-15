import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   f = open('data.csv')
   data = csv.reader(f)
   
   return list(data)[0]

# Read the csv file
print(get_first_row('data.csv'))