#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import sqlite3


# In[ ]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root"
  passwd="enzo&luvi2/?123*-",
  database="mydata"
)

mycursor = mydb.cursor()

sql = "INSERT INTO mydata(brands,prices) VALUES (%s, %s)"
val = ("tomato", 12)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# In[ ]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="enzo&luvi2/?123*-",
  database="sakila"
)

mycursor = mydb.cursor()

sql = "INSERT INTO mydata(items,brands,prices,barcode,`expiry date`) VALUES (%s,%s, %s,%s,%s)"
val = ('BISCUITS',"eat some more",10,458974,'08.06.2020' )


mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# In[67]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="enzo&luvi2/?123*-",
  database="sakila"
)

mycursor = mydb.cursor()

sql = "UPDATE mydata SET items = 'healthy veggies' where brands = 'tomato'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 


# In[47]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

db= MySQLdb.connect("localhost", "root", "enzo&luvi2/?123*-", "sakila")

cursor= db.cursor()

cursor.execute("ALTER TABLE mydata ADD `expiry date` VARCHAR(100) NOT NULL")

db.close()


# In[ ]:


mycursor = mydb.cursor()

sql = "DELETE FROM mydata WHERE brands = 'tennis'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


# In[23]:


chips=pd.read_sql_query("Select * from sakila.mydata where items='Chips'",mydb)

chips


# In[68]:


cooldrink=pd.read_sql_query("Select * from sakila.mydata where items='Cooldrink'",mydb)

cooldrink


# In[69]:


chocolate=pd.read_sql_query("Select * from sakila.mydata where items='Chocolate'",mydb)

chocolate


# In[70]:


cupcakes=pd.read_sql_query("Select * from sakila.mydata where items='Cupcakes'",mydb)

cupcakes


# In[75]:


pies=pd.read_sql_query("Select * from sakila.mydata where items='pies'",mydb)

pies


# In[ ]:




