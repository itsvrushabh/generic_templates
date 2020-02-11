import csv


csv_record = []
with open('TEMPLATES_COMMADN.csv', newline='') as csv_records:
     spamreader = csv.reader(csv_records, delimiter=',')
     for row in spamreader:
        csv_record.append(row)
    
print(csv_record) 