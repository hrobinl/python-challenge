import csv
import os

# Define path to collect data from the Resources Folder
csvpath = os.path.join("C:\\Users\\hanna\\python-challenge\\PyPoll\\Resources\\election_data.csv")

with open ("C:\\Users\\hanna\\python-challenge\\PyPoll\\Resources\\election_data.csv") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    
    # Prepare variables

    # Generates a list named "voterids" for the "Ballot Id" column
    voterids=[] 
    # Generates a list named "counties" for the "County" column
    counties=[]
    # Generates a list named "candidates" for the "Candidate" column
    candidates=[]
    # Generates a list of "candidate names" for the "Candidate" column
    candidatenames=[] 
    # Generates alist for total votes for each found candidate
    totaleachcan=[] 
    # Generates a list for result printout of each found candidate
    resultprintcan=[] 
    # Generates a list for percentage of votes for each found candidate
    totaleachcanperc=[] 

    # Set of Start Conditions
    line_count=0
    winnervotes=0
    leastvotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
    # Read in each row of data after the header and write data into the assigned lists
    for row in csvreader:
        # Assign column 0 as voterid
        voterid=row[0]
        # Assign column 1 as county
        county=row[1]
        # Assign column 2 as candidate
        candidate=row[2]
        # Add next line to list voterids
        voterids.append(voterid) 
        # Add next line to list counties
        counties.append(county) 
        # Add next line to list candidates
        candidates.append(candidate) 
    
    line_count= len(voterids) #Count the total number of votes cast in the "Voter ID" column
    
    # print(line_count)

# Start Data Analysis
# Begin with first candidate name for comparison
candidatenames.append(candidates[0])

# First loop is through the list of candidates to determine candidates voted for (variable loop1 as loop index counter)
for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)

#print(n)

# Second loop variable loop2 as loop index counter
for loop2 in range (n): #Range of loop depending on how many candidates were listed
    # Count total votes of candidates and add to list total
    totaleachcan.append(candidates.count(candidatenames[loop2])) 

# print(candidatenames)
# print(totaleachcan)

#T hird loop variable loop3 as loop index counter

# Pre-load loservoters with maximum votes for < comparison
leastvotes=line_count 

# Range of (loop) depending on how many candidates were listed
for loop3 in range(n):
    # Calculate % per candidate found
    totaleachcanperc.append(f'{round((totaleachcan[loop3]/line_count*100), 4)}%') 
     # Find candidate with highest vote count
    if totaleachcan[loop3]>winnervotes: 
        winner=candidatenames[loop3]
        winnervotes=totaleachcan[loop3]
        # Find candidate with lowest vote count
    if totaleachcan[loop3]<leastvotes: 
        least=candidatenames[loop3]
        leastvotes=totaleachcan[loop3]

# Fourth loop variable loop4 as loop index counter
for loop4 in range(n):
    #Format list resultprintcan
    resultprintcan.append(f'{candidatenames[loop4]}: {totaleachcanperc[loop4]} ({totaleachcan[loop4]})') 

# Prepare new combined list of results for printout (each candidate with the result gets a new line)
resultlines='\n'.join(resultprintcan) 

# Generate new output lines
analysis=f'\
Election Results\n\
*----------------------------*\n\
Total Votes: {line_count}\n\
*----------------------------*\n\
{resultlines}\n\
*----------------------------*\n\
Winner: {winner}\n\
*----------------------------*\n'

# Output results on screen
print(analysis) 

# Write into text file named pypoll.txt

# Open or if file does not exist then create file named PyPollAnalysis.txt
file1=open("PyPollAnalysis.txt","w") 
# Write analysis into PyPollAnalysis.txt
file1.writelines(analysis) 
# Close PyPollAnalysis.tx write mode
file1.close() 
