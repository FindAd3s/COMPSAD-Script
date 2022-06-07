from sqlalchemy import create_engine
import pandas as pd

print ("hello") #Hello
engine = create_engine("mysql+pymysql://root@localhost/fies") #Connection address to the SQL server
conn = engine.connect() #Actual connection to the SQL Server

excelData = pd.read_excel('2018-2012_FIES_excel_data.xlsx', sheet_name='2018 FIES data') #Reads data on the excel file

frame = excelData.to_sql("fies_2018_2012", conn, if_exists = 'replace', index = False) #Uploads excel data to the SQL Server
print("data uploaded to sql server")