## Description:
#
#
# Modification History:
#	DD-MM-YYY 	Author			Description
#	12-06-2019	Stacey Smith	Initial Creation
#


import os
import csv

curdir = os.getcwd()
file = os.path.join(curdir, 'Resources', 'budget_data.csv')

with open(file, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csvheader = next(csvreader)
	#print(f'CSV Header {csvheader}')
	#next(csvreader) #skips header so it's not added to the list

	months=[]
	netTotal=[]
	diffs=[]
	
	firstval = 0
	maxval = 0
	minval = 9999999

	for row in csvreader:

		months.append(row[0])
		netTotal.append(int(row[1]))

		diffval = int(row[1])-firstval
		firstval = int(row[1])
		diffs.append(diffval)
		if diffval > maxval:
			maxval = diffval
			maxdate = row[0]
		if diffval < minval:
			minval = diffval
			mindate = row[0]


	#print(diffs[1:])

	#zipdiffs = zip(months, diffs)
	#print(set(zipdiffs))
	#for x in zipdiffs:

	#print(min(zipdiffs))
		

		
#Print Financial Analysis to the terminal
	print('Financial Analysis \n') 
	print('-------------------------------- \n')	 

#The total number of months included in the dataset
	print(f' Total Months: {len(months)} \n ')

#The net total amount of "Profit/Losses" over the entire period
	#print('Net Total: $' + sum(float(x) for x in netTotal) + ' \n')
	print(f'Net Total: {sum(netTotal)} \n')

#The average of the changes in "Profit/Losses" over the entire period
	print(f' Average Change:  {sum(diffs[1:])/len(diffs[1:])} \n')	
	
#The greatest increase in profits (date and amount) over the entire period
	print(f' Greatest Increase in Profits: {maxdate, maxval} \n ')


#The greatest decrease in losses (date and amount) over the entire period	
	print(f' Greatest Decrease in Losses: {mindate, minval} \n ')
	
#Export the Financial Analysis to a text file
	
	
	
	
	
	
	
	
	#print(f' Net Total: {}')

	#print(lastval)
	
	




	
	







