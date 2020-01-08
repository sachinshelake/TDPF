print("Welcome to Test Data Pattern Finder")

import pandas as pd
import matplotlib.pyplot as plt
import datetime
from math import ceil
from utility.common import skycake, week_of_month

skycake()

excel_file = 'data.xlsx'
testData = pd.read_excel(excel_file)
# print(testData)
print('Total Rows and Columns:',testData.shape)

testData["class"]=testData.apply(lambda row: str(row.UserId)+'_'+str(week_of_month(row.Date)), axis=1)
print(testData)
userid=input("Please enter user id =>")
inputDate = input("Pleas enter date =>")

print(userid)
print(inputDate)

inputClass=userid+'_'+str(week_of_month(inputDate))
print(inputClass)
