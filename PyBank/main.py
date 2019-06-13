## Description:
#
#
# Modification History:
#	DD-MM-YYY 	Author			Description
#	12-06-2019	Stacey Smith	Initial Creation
#


import os
import csv

#print(os.getcwd())
file = os.path.join('Resources', 'budget_data.csv')


with open(file, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csvheader = next(csvreader)
	print(f'CSV Header {csvheader}')

	months=[]
	#netTotal[]

	for row in csvfile:
		months.append(row[0])

	print(f'''Financial Analysis \n 
		 -------------------------------- \n
		Total Months: {len(months)} \n  
		Total:   \n 
		Average Change: \n 
		Greatest Increase in Profits: \n  
		Greatest Decrease in Profits:  ''')

