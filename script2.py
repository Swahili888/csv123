import csv

with open('spreadsheet.csv', 'w') as csv_data:
	csvwriter = csv.writer(csv-data)
	csvwriter.writerow(['forename', 'surname', 'email'])
	csvwriter.writerow(['chidi', 'mansa', 'chidi@chef.co'])
