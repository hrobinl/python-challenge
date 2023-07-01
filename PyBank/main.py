import csv 
#import to use the csv module

with open("C:\\Users\\hanna\\Desktop\\Python-challenge\\Starter_Code\\Starter_Code\\PyBank\\Resources\\budgetdata.csv") as csv_file: 
#"r" represents the read mode
    reader = csv.reader(csv_file) 
    
    total_months = 0
    total_revenue = 0
    revenue = []
    month_of_change = []
    revenue_change = 0
    greatest_decrease = ["", 9999999]
    greatest_increase = ["", 0]
    revenue_change_list = []
    revenue_average = 0

        #loop through to find total months
        for row in reader:
            total_months += 1


    #this is the reader object

    for item in reader:
    # you have to loop through the document to get each data
        print(item)

    #text_path = "output.txt"

#Set path
    total_months += 1
