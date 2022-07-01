from sqlalchemy import create_engine
import pandas as pd

print ("hello") #Hello
engine = create_engine("mysql+pymysql://root@localhost/fies") #Connection address to the SQL server
conn = engine.connect() #Actual connection to the SQL Server
excelData = pd.read_excel('2018-2012_FIES_excel_data.xlsx', sheet_name='2018 FIES data') #Reads data on the excel file

try:
    referencedata = pd.read_sql_table("fies_2018_2012", con = engine) #Reads data from SQL

except ValueError:
    frame = excelData.to_sql("fies_2018_2012", conn, if_exists = 'replace', index = False) #Uploads excel data to the SQL Server
    print("data uploaded to sql server")

else:
    # Uncomment print statement below to print excel data for reference
    # print(excelData) 

    concatenateData = pd.concat([excelData, referencedata], axis = 0) #Merges Excel data to SQL data. Excel Data is always on top 
    concatenateData = concatenateData.drop_duplicates(subset=['Region'], keep = 'first', ignore_index= True) #Drops duplicates based on Region. Newest data is kept

    frame = concatenateData.to_sql("fies_2018_2012", conn, if_exists = 'replace', index = False) #Uploads excel data to the SQL Server
    print("sql server data updated")