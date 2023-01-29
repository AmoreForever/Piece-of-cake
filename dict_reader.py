import csv

def csv_to_dictList(file):
    reader = csv.DictReader(open(file, 'r'))
    dictList = [line for line in reader]
    return dictList