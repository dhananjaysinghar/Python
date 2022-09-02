# pip install xlrd
# pip install pandas
# pip install openpyxl
# import pandas lib as pd  
import pandas as pd

# read by default 1st sheet of an excel file
#df1 = pd.read_csv('employees.xlsx', skiprows = 1)
df1 = pd.read_excel('employees.xlsx', skiprows = 1)
df2 = pd.read_excel('employees.xlsx')

print(df1)
print("====================================")
print(df2)
