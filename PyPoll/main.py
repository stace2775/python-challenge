## Description:
#	PYPOLL homework assignment.  This script pulls data from election_data.csv and returns
#	a summary to the terminal and to a PyPoll_Summary.csv file.  
#
# Modification History:
#	DD-MM-YYY 	Author			Description
#	17-06-2019	Stacey Smith	Initial Creation
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

	votes=[]
	candidates=[]

	for row in csvreader:

		votes.append(row[0])
		candidates.append(row[2])


votecount = len(votes)

Votes_Dict = dict(zip(votes, candidates))
#print(Votes_Dict)




#Print Election Results to the terminal
print('Election Results \n') 
print('-------------------------------- \n')	 


#The total number of votes cast
print(f' Total Votes: {votecount} \n ')
print('-------------------------------- \n')

#A complete list of candidates who received votes
	#print(f' Candidates: {print(x) for x in Votes_Dict} \n ')
print('-------------------------------- \n')

#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.

