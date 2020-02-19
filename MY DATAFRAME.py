#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd

products = {'chips':['lays','simba','niknaks','doritos','cheetos'],
            'cooldrinks': ['sprite','coke','fanta','stoney','score'], 
            'chocolates': ['cadbury','tex','barone','ps','lunchbar'], 
            'pies':['pepper steak','chicken','steak and kidney','sousage roll','fetta and spinach'], 
            'fruits':['apples','banana','mango','orange','grapes'],
            'cupcakes':['vanilla','chocolate','redvelvet','caramel','blue berry'],
            'vegies':['potatos','cabbage','spinach','carrot','beetrot'],  
            'Price in rands': [25,16,24,21,22],
            'quantity':[20,11,12,15,10],
            'stock price':[200,300,150,200,300]
            }             
df = pd.DataFrame(products, columns= None)
df


# In[16]:


df.plot(x ='cooldrinks', y='stock price', kind = 'bar')


# In[5]:


df.filter(regex ='[aA]') 


# In[6]:


df.filter(["chips", "quantity"]) 


# In[7]:


df.loc[[0,1]]


# In[8]:


df.tail(3)


# In[83]:


df.head(0)


# In[6]:


df.mean(axis=0)


# In[17]:


df.describe()


# In[ ]:




