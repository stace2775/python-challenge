## Description:
#	PYPOLL homework assignment.  This script pulls data from election_data.csv and returns
#	a summary to the terminal and to a election_results.txt file.  
#
# Modification History:
#	DD-MM-YYY 	Author			Description
#	17-06-2019	Stacey Smith	Initial Creation
#

#Dependencies
import os
import csv

#open the data file
curdir = os.getcwd()
file = os.path.join(curdir, 'Resources', 'election_data.csv')

with open(file, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csvheader = next(csvreader)
	
#iterating through the election_data.csv file and creating a separate list for each candidate.
	Khanvotes=[]
	OTooleyvotes=[]
	Livotes=[]
	Correyvotes=[]
	votes=[]
	#candidates=set()
	for row in csvreader:
		if row[2] == 'Khan':
			Khanvotes.append(row[0])
		if row[2] == "O'Tooley":
			OTooleyvotes.append(row[0])
		if row[2] == 'Li':
			Livotes.append(row[0])
		if row[2] == 'Correy':
			Correyvotes.append(row[0])
		votes.append(row[0])
		#candidates.add(row[2])

#Done with the file, close it
csvfile.close()

#counting the votes for each candidate
Khancount = len(Khanvotes)
OTooleycount = len(OTooleyvotes)
Licount = len(Livotes)
Correycount = len(Correyvotes)

#counting all the votes
votecount = len(votes)


#Print Election Results to the terminal
print('Election Results \n') 
print('-------------------------------- \n')	 

#The total number of votes cast
print(f' Total Votes: {votecount} \n ')
print('-------------------------------- \n')

#A complete list of candidates who received votes
#print(f' Candidates: {(candidates)} \n ')
#print('-------------------------------- \n')

#The percentage of votes each candidate won
print(f'Khan: {(Khancount/votecount):%} percent of the vote, with {Khancount} votes total. \n')
print(f"O'Tooley: {(OTooleycount/votecount):%} percent of the vote, with {OTooleycount} votes total. \n")
print(f'Li: {(Licount/votecount):%} percent of the vote, with {Licount} votes total. \n')
print(f'Correy: {(Correycount/votecount):%} percent of the vote, with {Correycount} votes total. \n')

#The winner of the election based on popular vote.
mostvotes=[Khancount, OTooleycount, Licount, Correycount]
winner = max(mostvotes)
if winner == Khancount:
	print("\n Winner is Khan \n")
if winner == OTooleycount:
	print("\n Winner is O'Tooley \n")
if winner == Licount:
	print("\n Winner is Li \n")
if winner == Correycount:
	print("\n Winner is Correy \n")

	
#Export the Financial Analysis to a text file

curdir = os.getcwd()
file = os.path.join(curdir, 'Resources', 'election_results.txt')
with open(file, 'w') as txtfile:

	txtfile.write('Election Results \n') 
	txtfile.write('-------------------------------- \n')	 
	txtfile.write(f' Total Votes: {votecount} \n ')
	txtfile.write('-------------------------------- \n')
	#txtfile.write(f' Candidates: {(candidates)} \n ')
	#txtfile.write('-------------------------------- \n')
	txtfile.write(f'Khan: {(Khancount/votecount):%} percent of the vote, with {Khancount} votes total. \n')
	txtfile.write(f"O'Tooley: {(OTooleycount/votecount):%} percent of the vote, with {OTooleycount} votes total. \n")
	txtfile.write(f'Li: {(Licount/votecount):%} percent of the vote, with {Licount} votes total. \n')
	txtfile.write(f'Correy: {(Correycount/votecount):%} percent of the vote, with {Correycount} votes total. \n')

	if winner == Khancount:
		txtfile.write("\n Winner is Khan \n")
	if winner == OTooleycount:
		txtfile.write("\n Winner is O'Tooley \n")
	if winner == Licount:
		txtfile.write("\n Winner is Li \n")
	if winner == Correycount:
		txtfile.write("\n Winner is Correy \n")

txtfile.close()