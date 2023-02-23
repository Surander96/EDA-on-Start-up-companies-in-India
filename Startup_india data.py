#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as pd
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# In[33]:


raw_data=pd.read_csv('C:/Users/HP/Documents/backups/big_startup_secsees_dataset.csv')


# In[34]:


raw_data.head()


# In[35]:


raw_data.info()


# In[36]:


raw_data.describe(include='all')


# In[37]:


raw_data.isna().sum()


# In[38]:


raw_data=raw_data.dropna(subset=['category_list'],axis=0)
raw_data=raw_data.dropna(subset=['region'],axis=0)
raw_data=raw_data.dropna(subset=['country_code'],axis=0)


# In[39]:


raw_data.isna().sum()


# In[40]:


company_status = raw_data[['status', 'permalink']].groupby('status').count().reset_index()
plt.bar(company_status.status, company_status.permalink)


# In[41]:


world_data=raw_data.loc[raw_data.status.isin(['ipo','acquired','operating','closed'])][['country_code', 'status', 'permalink']].groupby(['country_code']).count().reset_index().sort_values('permalink', ascending=False)
world_data


# In[42]:


india_startup=raw_data[raw_data['country_code']=='IND'].reset_index()
india_startup


# In[43]:


fig_pie=go.Figure(go.Pie(title='India startup chart',labels=india_startup['status'],hole=0.5))
fig_pie.update_layout(
                      autosize=False,
                      width=400,
                      height=400)
fig_pie.update_traces(textposition='outside')
fig_pie.show()


# In[44]:


fig_bar=px.histogram(title='Startup status with respect to state',x=india_startup['region'],color=india_startup['status'])
fig_bar.show()


# In[45]:


indian_operating_statup=india_startup[india_startup['status']=='operating']


# In[46]:


indian_operating_statup


# In[47]:


fig_hist=px.histogram(title='start up opearting in various sectors',x=indian_operating_statup['category_list'],color=indian_operating_statup['status'])
fig_hist.update_layout(
                       autosize=False,
                       width=1200,
                       height=1200)
fig_hist.show()


# In[48]:


Closed_category_data=india_startup[india_startup['status']=='closed']
Closed_category_data


# In[49]:


fig_closed=go.Figure(go.Pie(title='Catogory wise closed',labels=Closed_category_data['category_list'],hole=0.5))
fig_closed.update_traces(textposition='outside')
fig_closed.show()


# In[50]:


avg_fundingstat=india_startup


# In[51]:


avg_fundingstat=avg_fundingstat.dropna(subset=['founded_at','first_funding_at'],axis=0,how='any')


# In[52]:


avg_fundingstat.isna().sum()


# In[53]:


avg_fundingstat['founded_at']=pd.to_datetime(avg_fundingstat['founded_at'],errors='coerce')
avg_fundingstat['founded_at']=pd.to_datetime(avg_fundingstat['founded_at'])


# In[54]:


avg_fundingstat['founded_year']=avg_fundingstat['founded_at'].dt.year  #to seperate year from date


# In[55]:


avg_fundingstat


# In[56]:


avg_fundingstat['first_funding_at']=pd.to_datetime(avg_fundingstat['first_funding_at'],errors='coerce')
avg_fundingstat['first_funding_at']=pd.to_datetime(avg_fundingstat['first_funding_at'])
avg_fundingstat['first_funding_year']=avg_fundingstat['first_funding_at'].dt.year


# In[57]:


avg_fundingstat['founded_year'].value_counts().head(5)    #more statup found at year 2012


# In[58]:


avg_waiting_period=avg_fundingstat['first_funding_year']-avg_fundingstat['founded_year']


# In[59]:


avg_fundingstat['avg_waiting_period']=avg_waiting_period


# In[60]:


avg_fundingstat['avg_waiting_period'].mean()


# In[61]:


fig=px.scatter(avg_fundingstat,x='category_list',y=avg_waiting_period,color='region',animation_frame='region',width=800,height=1200)
fig.show()


# In[ ]:




