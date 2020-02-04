import csv


with open('TEMPLATES_COMMADN.csv', newline='') as csv_records:
     spamreader = csv.reader(csv_records, delimiter=',')
     for row in spamreader:
         print(','.join(row))