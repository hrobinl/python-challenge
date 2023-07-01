

#Import Modules
import csv 
#import to use the csv module

with open("C:\\Users\\hanna\\Desktop\\Python-challenge\\PyBank\\Resources\\budgetdata.csv") as csv_file: 
#"r" represents the read mode

    
    #this is the reader object
    reader = csv.reader(csv_file) 
    for item in reader:
    # you have to loop through the document to get each data
        print(item)

        #Set variables
        total_months = 0
        total_revenue = 0
        revenue = []
        previous_revenue = 0
        month_of_change = []
        revenue_change = 0
        greatest_decrease = ["", 9999999]
        revenue_change_list = []
        revenue_average = 0 
        
        #loop through to find total months
        for row in reader:
            total_months += 1
        
        total_revenue = total_revenue + previous_revenue
        #previous_revenue = float(row["Profit/Losses"])
        #revenue_change_list = revenue_change_list + [revenue_change]

            #if the greatest increase in rev (date & amt) over enture year
        #if revenue_change > greatest_increase[1]:
         #  greatest_increase[1]= revenue_change
        #   greatest_decrease[0]= row['Date']
        #revenue_average = sum(revenue_change_list)/len(revenue_change_list)

