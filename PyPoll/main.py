import csv 
#import to use the csv module

with open("C:\\Users\\hanna\\Desktop\\Python-challenge\\PyPoll\\Resources\\election_data.csv") as csv_file: 
#"r" represents the read mode

    
    #this is the reader object
    reader = csv.reader(csv_file) 
    for item in reader:
    # you have to loop through the document to get each data
        print(item)


#Set path


#The total number of votes cast
 #total_votes = 
#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote