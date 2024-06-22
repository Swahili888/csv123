import csv

with open('spreadsheet.csv', 'r') as csv_data:
	csv_reader = csv.reader(csv_data)

	with open('newfile.csv', 'w') as new_data:
		csv_writer = csv.writer(new_data, delimiter='\t')
		for line in csv_reader:
			csv_writer.writerow(line)
