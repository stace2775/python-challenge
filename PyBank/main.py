## Description:
#
#
# Modification History:
#	DD-MM-YYY 	Author			Description
#	12-06-2019	Stacey Smith	Initial Creation
#


import os
import csv
#import numpy

#print(os.getcwd())
file = os.path.join('Resources', 'budget_data.csv')


with open(file, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csvheader = next(csvreader)
	#print(f'CSV Header {csvheader}')
	next(csvreader) #skips header so it's not added to the list

	months=[]
	netTotal=[]

	for row in csvfile:
		months.append(row[0])
		netTotal.append(row[1])

	netTotal = map(float, netTotal)
	#net = [float(i) for i in netTotal]

	print('Financial Analysis \n') 
	print('-------------------------------- \n')	 
	print(f' Total Months: {len(months)} \n ')	
	print(f' Total:  {sum(netTotal)} \n ')	
	print(f' Average Change: {(sum(netTotal))/netTotal} \n ')
	print(f' Greatest Increase in Profits: {max(netTotal)} \n ')
	print(f' Greatest Decrease in Profits: {min(netTotal)}')

