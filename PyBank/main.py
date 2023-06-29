import csv 
#import to use the csv module

with open("C:\\Users\\hanna\\Desktop\\Python-challenge\\Starter_Code\\Starter_Code\\PyBank\\Resources\\budgetdata.csv") as csv_file: 
#"r" represents the read mode
    reader = csv.reader(csv_file) 
    
    #this is the reader object

    for item in reader:
    # you have to loop through the document to get each data
        print(item)


#Set path
