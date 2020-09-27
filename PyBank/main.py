#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing pandas and defining the dataframe

import pandas as pd
df = pd.read_csv("budget_data.csv")
df2 = pd.read_csv("budget_data.csv")


# In[2]:


#checking prior command
#print(df)


# In[3]:


monthly_pnl = df['Profit/Losses'].sum()
monthly_pnl
net_profits = monthly_pnl
print(net_profits)


# In[4]:


#calculating number of periods in dataset
num_months = (df.shape[0])


# In[5]:


#print(num_months)


# In[6]:


# calculating net profits for all periods


# In[ ]:





# In[7]:


#importing numpy library

import numpy as np

df.dtypes


# In[8]:


#checking datatypes and selecting what needs to be included in below calculation
pnl_int = df.select_dtypes(include = ['int64'])


# In[9]:


#calculating difference in profit and loss between prior and next period for data set
pnl_difference = pnl_int.diff()
#print(pnl_difference)


# In[10]:


#calculating the average of the change in Profit/Loss over the entire dataset

pnl_change = pnl_difference.sum() // num_months
#print(pnl_change)


# In[11]:


# identifying the greatest increase in profits 
#max_increase = pnl_difference.max()
max_increase = pnl_difference["Profit/Losses"].max()
#print(max_increase)


# In[12]:


#identifying the greatest drop

max_decrease = pnl_difference.min()
print(max_decrease)


# In[13]:


# checking lenght for merge
len_df2 = (df2.shape[0])
print(len_df2)


# In[14]:


#checking length for merge
len_pnl_difference = (pnl_difference.shape[0])
#print(len_pnl_difference)


# In[15]:


# creating new dict by merging dfs Profit/Losses-y is the monthly changes in pnl

delta_df = pd.merge(df2, pnl_difference, right_index= True, left_index = True)
#print(delta_df)


# In[16]:


#setting up new dataframe with appened monthly pnl change
df3 = pd.DataFrame(delta_df)
#print(df3)


# In[17]:


#renaming columns for readability
df3.columns =['Date', 'Profit/Losses', 'MoMVariance']
#print(df3)


# In[18]:


df3['MoMVariance'].astype(str)
df3.set_index('MoMVariance')


# In[19]:


#locating the month with the greatest increse in profits
 
max_month = df3.loc[df3['MoMVariance']== 1926159.0]
#print(max_month)


# In[20]:


#here i am using the monthly change column as an index to return the dates values associated with them
max_date = max_month.get(["Date"])

max_amount = max_month.get(["MoMVariance"])

maxfinal_date = max_date.to_csv(header = None, index = False)
maxfinal_amount = max_amount.to_csv(header = None, index = False)
#print(maxfinal_date)
#print(maxfinal_amount)


# In[21]:


#locating the month with the greatest decrease in profits
min_month = df3.loc[df3['MoMVariance']== -2196167.0]
print(min_month)


# In[ ]:





# In[22]:


## formatting max and min values for text printing
min_date = min_month.get(["Date"])
minfinal_date = min_date.to_csv(header = None, index = False)

min_amount = min_month.get(["MoMVariance"])
minfinal_amount = min_amount.to_csv(header = None, index = False)


#print(minfinal_date)
#print(minfinal_amount)


# In[23]:


total_months =num_months
total_profits = net_profits
average_change = pnl_change.loc['Profit/Losses']
greatest_increase_month = maxfinal_date
greatest_increase_amount = maxfinal_amount
greatest_decrease_month = minfinal_date
greatest_decrease_amount = minfinal_amount


# In[24]:



 
print("Financial Analysis", )
print("------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits}")
print(f"AverageChange: ${average_change}")
print(f"The Greatest Increase in Profits:{greatest_increase_month}(${greatest_increase_amount})") 
print(f"The Greatest Decrease in Profits:{greatest_decrease_month}($ {greatest_decrease_amount})")
        


# In[25]:



with open("Output.txt", "a") as f: 
    print("Financial Analysis", file = f)
    print("------------------------------------------------", file = f)
    print(f"Total Months: {total_months}", file = f)
    print(f"Total: ${total_profits}", file = f)
    print(f"AverageChange: ${average_change}", file = f)
    print(f"The Greatest Increase in Profits:{greatest_increase_month}(${greatest_increase_amount})", file = f) 
    print(f"The Greatest Decrease in Profits:{greatest_decrease_month}($ {greatest_decrease_amount})", file = f)
        


# In[ ]:





# In[ ]:




