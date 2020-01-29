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
#print(testData.head(4))
userid=input("Please enter user id : ")
inputDate = input("Pleas enter date(mm/dd/yyyy) : ")
# /date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.datetime.strptime(inputDate, '%m/%d/%Y')
inputClass=userid.lower()+'_'+str(week_of_month(date_time_obj))+'_'+str(date_time_obj.weekday())
#print(inputClass)
filteredData=testData[testData["class"]==inputClass]
uniqueDataFrame=filteredData.drop_duplicates("workflow_query_test_data_request")
uniqueDataFrame=uniqueDataFrame.sort_values('sequence_no')
uniqueDataFrame=uniqueDataFrame[["sequence_no", "user_id", "ait", "workflow_query_test_data_request"]]
print("Data you would be interested in:")
print(uniqueDataFrame)
