import os
import csv

#set path for file
csvpath = os.path.join('C:\\Users\\hanna\\Desktop\\Python-challenge\\PyBank\\Resources\\budgetdata.csv')

#set the output of the txt file
#text_path = "output.txt"

#Set variables
#total_months = 0
#total_revenue = 0
#revenue = []
#previous_revenue = 0
#month_of_change = []
#revenue_change = 0
#greatest_decrease = ["", 9999999]
#greatest_increase = ["", 0]
#revenue_change_list = []
#revenue_average = 0


#open the csv file
with open(csvpath,encoding= 'utf') as csvfile:
#inializing reader to read csvfile
    csvreader = csv.reader(csvfile, delimiter = ',')
    #Skipping the header(first row
    next(csvreader)
    #Excluding first month from the loop
    budget_data = [next(csvreader)]
    #Initializing net amt with first profit or loss
    net_amount = int(budget_data[0][1])
    changes = []
    #Will be used to calculate change instide for loop
    previous_profit_loss = net_amount

    for line in csvreader:
        #Total months included in dataset
        budget_data.append(line)


        #net total amount of Profit/Losses over entire period
        net_amount = net_amount + int(line[1])

        #Changes in profit/loss over entire period
        changes.append(int(line[1])-previous_profit_loss)

        #Average canges of profit/loss
        previous_profit_loss = int(line[1])


    # Greatest increase in profit (date and amount)
    index_max_change = changes.index(max(changes))
    # print(budget_data[index_max_change+1])


    #Greatest decrease in profit (date and amount)
    index_max_loss = changes.index(min(changes))
    # print(budget_data[index_max_loss+1])

    #Export result to text file and print analysis in terminal
    output = f'''  Financial Analysis:
            -------------------------------
    Total Months: {len(budget_data)}
    Total: ${net_amount}
  Greatest Increase in Profits: {budget_data[index_max_change+1][0]} (${max(changes)})
  Greatest Decrease in Profits: {budget_data[index_max_loss+1][0]} (${min(changes)})

    '''
print(output)
csvpath = os.path.join('Analysis','Financial_Analysis.txt')
with open(csvpath,'w') as textfile:
    textfile.write(output)