print("Welcome to Test Data Pattern Finder")

import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'data.xlsx'
testData = pd.read_excel(excel_file)
print(testData)
print('Total Rows and Columns:',testData.shape)
testData.plot(kind="barh")
plt.show()