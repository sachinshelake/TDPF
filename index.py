print("Welcome to Test Data Pattern Finder")

import pandas as pd
import matplotlib.pyplot as plt
import datetime
from math import ceil
from utility.common import skycake, week_of_month

skycake()

excel_file = 'Hack-Data-For-Pattern-Finder.xlsx'
testData = pd.read_excel(excel_file)
testData.columns = [c.lower().replace(' ', '_').replace('/','_') for c in testData.columns]
# print(testData)
print('Total Rows and Columns:',testData.shape)
testData["class"]=testData.apply(lambda row: str(row.user_id).lower()+'_'+str(week_of_month(row.date))+'_'+str(row.date.weekday()), axis=1)
print(testData.head(4))
userid=input("Please enter user id : ")
inputDate = input("Pleas enter date(yyyy-mm-dd) : ")
# /date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.datetime.strptime(inputDate, '%Y-%m-%d')
inputClass=userid.lower()+'_'+str(week_of_month(date_time_obj))+'_'+str(date_time_obj.weekday())
#print(inputClass)
filteredData=testData[testData["class"]==inputClass]
print("Data you are interested in:")
print(filteredData.sort_values('sequence_no'))
