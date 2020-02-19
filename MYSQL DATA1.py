#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import sqlite3


# In[1]:


#Read from file
df=pd.read_csv('MYDATA.csv', sep="\t")
# Create table
c.execute('''CREATE TABLE WHOLE
           #  (ITEMS text, BRANDS text, SIZES text,QUANTITY real, price real,STOCK PRICES real)''')
# Insert a row of data
conn = sqlite3.connect(":memory:")# database is in the ram

df.to_sql("whole", con=conn, index=False, if_exists='replace')
_q = 'SELECT * FROM whole'
_d = pd.read_sql(_q, conn)
_d


# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
df.plot(x ='BRANDS', y='STOCK PRICE', kind = 'bar')
plt.ylabel('STOCK PRICE')


# In[4]:


import numpy as np
fig = plt.figure(figsize= (20,5))
plt.xticks(rotation=45)
plt.title('BRANDS AND PRICES')
plt.xlabel('BRANDS')
plt.ylabel('STOCK PRICES')
plt.plot(_d["BRANDS"], _d["STOCK PRICE"])
plt.show()
 


# In[41]:



SIZES= [250,250,250,250]
x = ["simba","niknaks","cheetos","doritos"]

fig = plt.figure(figsize=(10, 5))
plt.plot(x,SIZES, color='purple')
# Customizing the axes
plt.xticks(rotation=45, color='teal', size=12)
plt.yticks(rotation=45, color='teal', size=12)
plt.title('SIZES OF CHIPS')
# Setting axes labels
plt.xlabel('BRANDS', {'color': 'orange', 'fontsize':15})
plt.ylabel('SIZES', {'color': 'orange', 'fontsize':15})
plt.show()


# In[27]:


color = np.random.rand(5)
size = np.random.randint(50, 100, 10)
y = [16,18,17,16,13]
x = ["stoney","coke","score","sprite","fanta"]
# Creating a scatter plot
plt.scatter(x, y, c=color, s=size)
plt.title('QUANTITY OF COOLDRINKS')
# Labeling the plot and showing it
plt.xlabel('COOLDRINKS')
plt.ylabel('QUANTITY')
plt.show()


# In[40]:


y = [12,16,20,16,20]
x = ["apple","banana","mango","orange","grapes"]

plt.plot(x,y ,'g' )
plt.plot(x,y ,'r*' )
plt.title('FRUITS PRICES')
plt.xlabel('FRUITS')
plt.ylabel('PRICES')
plt.show()


# In[50]:


data = [250,300,150,100,120]
register =0 ,1,2,3,4
cupcakes=["vanilla","chocolate","redvelvet","caramel","blueberry"]
plt.figure(figsize=(8, 4))
b = plt.barh(register,data,height =.8,color =("m","r","b","g"))
plt.title("CUPCAKES QUANTITY", fontsize = 20)
plt.yticks(register,cupcakes)
plt.legend(b,cupcakes)
plt.show()



# In[ ]:




