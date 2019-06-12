## Description:
#
#
# Modification History:
#	DD-MM-YYY 	Author			Description
#	12-06-2019	Stacey Smith	Initial Creation
#


import os
import csv

file = os.path.join("..", "Resources", "budget_data.csv")

with open(file, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csvheader = next(csvreader)
	print(f'CSV Header {csvheader}')