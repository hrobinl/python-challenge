import os
import csv

#set path for file
budgetdata_csv = os.path.join("C:\Users\hanna\Desktop\Python-challenge\PyBank\Resources\budgetdata.csv")

#set the output of the txt file
text_path = "output.txt"

#Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0


#open the csv file
with open('budgetdata.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)





