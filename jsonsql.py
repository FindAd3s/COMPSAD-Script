from sqlalchemy import MetaData, Table, Column, Integer, String, bindparam, update, create_engine
import pandas as pd

print ("hello")
engine = create_engine("mysql+pymysql://root@localhost/testTable")
con = engine.connect()


