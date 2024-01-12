import os
import csv

def write_csv(filename, students):
    """ takes the original filename and a list of students and 
        creates a new csv file of all students who should be 
        contacted concerning grades. Names will also be 
        formatted to be capitalized properly
    """
    with open(os.getcwd() + '\\' + filename + '.csv', 'w', newline='') as file:
        fwrite = csv.writer(file, quotechar='|')
        for record in students:
            # formats both name fields to be properly capitalized
            record[0], record[1] = record[0].capitalize(), record[1].capitalize()
            fwrite.writerow(record)
    print("* csv written successfully! *")
    print()