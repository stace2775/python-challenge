## Description:
#	PYBANK homework assignment.  This script pulls data from budget_data.csv and returns
#	a summary to the terminal and to a financial_analysis.txt file.  
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

#create lists for the months, the profit/loss, and to hold the difference in p/l from month-to-month
	months=[]
	netTotal=[]
	diffs=[]
	
#initializing values
	firstval = 0
	maxval = 0
	minval = 9999999

#looping through the file to build the lists and calculate the difference and the max/min p/l values with corresponding dates
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


		
#Print Financial Analysis to the terminal
	print('Financial Analysis \n') 
	print('-------------------------------- \n')	 

#The total number of months included in the dataset
	print(f'Total Months: {len(months)} \n ')

#The net total amount of "Profit/Losses" over the entire period
	#print('Net Total: $' + sum(float(x) for x in netTotal) + ' \n')
	print(f'Net Total: {sum(netTotal)} \n')

#The average of the changes in "Profit/Losses" over the entire period
	print(f'Average Change:  {round(sum(diffs[1:])/len(diffs[1:]))} \n')	
	
#The greatest increase in profits (date and amount) over the entire period
	print(f'Greatest Increase in Profits: {maxdate, maxval} \n ')

#The greatest decrease in losses (date and amount) over the entire period	
	print(f'Greatest Decrease in Losses: {mindate, minval} \n ')
	
#Export the Financial Analysis to a text file
curdir = os.getcwd()
file = os.path.join(curdir, 'Resources', 'financial_analysis.txt')
with open(file, 'w') as txtfile:	
	txtfile.write('Financial Analysis \n') 
	txtfile.write('-------------------------------- \n')	 
	txtfile.write(f'Total Months: {len(months)} \n ')
	#print('Net Total: $' + sum(float(x) for x in netTotal) + ' \n')
	txtfile.write(f'Net Total: {sum(netTotal)} \n')
	txtfile.write(f'Average Change:  {round(sum(diffs[1:])/len(diffs[1:]))} \n')	
	txtfile.write(f'Greatest Increase in Profits: {maxdate, maxval} \n ')
	txtfile.write(f'Greatest Decrease in Losses: {mindate, minval} \n ')

txtfile.close()
	
	
	
	
	
	
	




	
	







