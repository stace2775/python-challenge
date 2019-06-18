## Description:
#	PYPOLL homework assignment.  This script pulls data from election_data.csv and returns
#	a summary to the terminal and to a PyPoll_Summary.csv file.  
#
# Modification History:
#	DD-MM-YYY 	Author			Description
#	17-06-2019	Stacey Smith	Initial Creation
#

#  Can I pull values out of a set and assign them to variables to take care of the candidate names so 
#  I don't have to explicitly name them?
#
#  How do I format the percentages to only show 2 decimals?  Round isn't working. 
#
#  How do I redirect the terminal output to a text file without having to duplicate that whole block of print business. 
#


import os
import csv

curdir = os.getcwd()
file = os.path.join(curdir, 'Resources', 'election_data.csv')

with open(file, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csvheader = next(csvreader)
	#print(f'CSV Header {csvheader}') VoterID, County, Candidate
	#next(csvreader) #skips header so it's not added to the list

	Khanvotes=[]
	OTooleyvotes=[]
	Livotes=[]
	Correyvotes=[]
	votes=[]
	candidates=set()
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
		candidates.add(row[2])

csvfile.close()

Khancount = len(Khanvotes)
OTooleycount = len(OTooleyvotes)
Licount = len(Livotes)
Correycount = len(Correyvotes)

votecount = len(votes)

#print(Khancount)
#print(OTooleycount)
#print(Licount)
#print(Correycount)




#Print Election Results to the terminal
print('Election Results \n') 
print('-------------------------------- \n')	 


#The total number of votes cast
print(f' Total Votes: {votecount} \n ')
print('-------------------------------- \n')

#A complete list of candidates who received votes
print(f' Candidates: {(candidates)} \n ')
print('-------------------------------- \n')

#The percentage of votes each candidate won
print(f'Khan: {(Khancount/votecount):2%} percent of the vote, with {Khancount} votes total.')
print(f"O'Tooley: {(OTooleycount/votecount):2%} percent of the vote, with {OTooleycount} votes total.")
print(f'Li: {(Licount/votecount):2%} percent of the vote, with {Licount} votes total.')
print(f'Correy: {(Correycount/votecount):2%} percent of the vote, with {Correycount} votes total.')
#The total number of votes each candidate won


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


output_path = os.path.join(curdir, 'Resources', 'election_results.txt')

with open(output_path, 'w') as writefile:
    #print('Filename:', "election_results.txt", file=writefile) 
	#print(writefile)
