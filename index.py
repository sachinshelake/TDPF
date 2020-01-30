print("Welcome to Test Data Pattern Finder")

import pandas as pd
import datetime
from utility.common import skycake, week_of_month

skycake()

try:
    testData = pd.read_excel('Hack-Data-For-Pattern-Finder.xlsx')
    testData.columns = [c.lower().replace(' ', '_').replace('/','_') for c in testData.columns]
    # print(testData)
    print('Total Rows and Columns:',testData.shape)
    #print(testData.head(4))
except:
    print("Error while importing test data.")
loopForInput= True
while loopForInput:
    try:
        userid=input("Please enter user id : ")
        inputDate = input("Pleas enter date(mm/dd/yyyy) : ")
        # /date_time_str = '2018-06-29 08:15:27.243860'
        date_time_obj = datetime.datetime.strptime(inputDate, '%m/%d/%Y')
        inputClass=userid.lower()+'_'+str(week_of_month(date_time_obj))+'_'+str(date_time_obj.weekday())
    except :
        print("Please enter valid input")
    else:
        try:
            testData["class"]=testData.apply(lambda row: str(row.user_id).lower()+'_'+str(week_of_month(row.date))+'_'+str(row.date.weekday()), axis=1)
            filteredData=testData[testData["class"]==inputClass]
            uniqueDataFrame=filteredData.drop_duplicates("workflow_query_test_data_request")
            #uniqueDataFrame=uniqueDataFrame.sort_values('sequence_no')
            uniqueDataFrame=uniqueDataFrame[["sequence_no", "user_id", "ait", "workflow_query_test_data_request"]]
        except:
            print("Error while processing data")
        else:    
            if uniqueDataFrame.empty!=True:
                print("Data you would be interested in:")
                print(uniqueDataFrame)
                try:
                    uniqueDataFrame.to_excel(inputClass+"_output.xlsx")
                    print("output is written at "+inputClass+"_output.xlsx")
                except:
                    print("Error while writing output to excel.")
            else:
                print("No data found")
                
        wantsToContinue=input("Do you want to exit? Please press 'Y'. To continue press any other key : ")
        if wantsToContinue.lower()=="y":
            loopForInput=False
        #show(uniqueDataFrame)