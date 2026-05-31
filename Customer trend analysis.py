#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd


# In[29]:


df = pd.read_csv(r'C:\Users\Biju\Desktop\Data Science Project\customer_shopping_behavior.csv')


# In[31]:


df.head()


# In[32]:


df.info()


# In[33]:


df.describe()


# In[34]:


df.describe(include='all')


# In[35]:


df.isnull().sum()


# In[36]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


# In[37]:


df.isnull().sum()


# In[38]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')


# In[39]:


df.columns


# In[40]:


df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[41]:


df.columns


# In[42]:


#create a new column as age_group to categorise different age people
labels = ['Young Adult','Adult','Middle Aged','Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)


# In[43]:


df[['age','age_group']].head(10)


# In[44]:


#create a new column called purchase_frequency_days


# In[45]:


frequency_mapping = {
   'Fortnightly' : 14,
   'Weekly' : 7,
   'Monthly' : 30,
   'Quarterly' : 90,
   'Bi-Weekly' :14,
   'Annually' :365,
   'Every 3 months' : 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[46]:


df[['purchase_frequency_days','frequency_of_purchases']].head(50)


# In[47]:


#df[['purchase_frequency_days']].head(50)


# In[48]:


df[['discount_applied','promo_code_used']].head(10)


# In[49]:


#to check the above 2 columns are really required or reduntant


# In[50]:


(df['discount_applied'] == df['promo_code_used']).all()


# In[51]:


df = df.drop('promo_code_used', axis=1)


# In[52]:


df.columns


# In[53]:


pip install psycopg2-binary sqlalchemy


# In[54]:


#step1: connect to postgreSQL
#Replace placeholder with your actual details
from sqlalchemy import create_engine
username = "postgres" #default user
password = "123456" #password set during installation
host = "localhost" #if running locally
port = "5432"  #default postgrSQL port
database = "customer_behaviour" #the data base you created in pgAdmin

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

#step 2 : Load Dataframe into postgresql
table_name = "customer" #choose any tble name
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")


# In[55]:


df.head(50)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




