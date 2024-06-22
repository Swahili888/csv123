import csv 

with open('spreadsheet.csv', 'r') as csv_data:
	csv_reader = csv.reader(csv_data)
	print(csv_data)
