import pandas as pd
from sqlalchemy import create_engine

mysql_engine = create_engine('mysql+pymysql://root:Adwika%4027@localhost:3306/etlqalab')
connection = mysql_engine.connect()
mysql_df = pd.read_sql("SELECT * FROM Customers_Order", connection)
print(mysql_df)
connection.close()