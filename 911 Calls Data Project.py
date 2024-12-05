

# # 911 Calls Capstone Project

# For this capstone project we will be analyzing some 911 call data from [Kaggle](https://www.kaggle.com/mchirico/montcoalert). The data contains the following fields:
# 
# * lat : String variable, Latitude
# * lng: String variable, Longitude
# * desc: String variable, Description of the Emergency Call
# * zip: String variable, Zipcode
# * title: String variable, Title
# * timeStamp: String variable, YYYY-MM-DD HH:MM:SS
# * twp: String variable, Township
# * addr: String variable, Address
# * e: String variable, Dummy variable (always 1)

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns



# In[3]:


df=pd.read_csv('911.csv')


# In[4]:


df.info()


# ** Check the head of df **

# In[5]:


df.head()


# ## Basic Questions

# ** What are the top 5 zipcodes for 911 calls? **

# In[6]:


df['zip'].value_counts().head()


# ** What are the top 5 townships (twp) for 911 calls? **

# In[7]:


df['twp'].value_counts().head()



# In[8]:


df['title'].nunique()     #len(df['title'].unique())


# ## Creating new features

# In[9]:


df['Reason']=df['title'].apply(lambda title: title.split(':')[0])


# In[10]:


df['Reason'].value_counts()


# In[11]:


sns.countplot(x='Reason',data=df)



# In[12]:


type(df['timeStamp'].iloc[0])


# In[13]:


df['timeStamp']=pd.to_datetime(df['timeStamp'])


# ** You can now grab specific attributes from a Datetime object by calling them. For example:**
# 
#     time = df['timeStamp'].iloc[0]
#     time.hour

# In[14]:


df['Hour']=df['timeStamp'].apply(lambda time:time.hour)
df['Month']=df['timeStamp'].apply(lambda time:time.month)
df['Day']=df['timeStamp'].apply(lambda time:time.dayofweek)


# In[15]:


df.head()


#     dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

# In[16]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[17]:


df['Day']=df['Day'].map(dmap)

# In[18]:


sns.countplot(x=df['Day'],data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05,1),loc=2)


# In[19]:


sns.countplot(x=df['Month'],data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05,1),loc=2)


# In[20]:


byMonth=df.groupby('Month').count()


# In[21]:


byMonth


# In[22]:


byMonth['lat'].plot()

# In[23]:


byMonth.reset_index()


# In[24]:


sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[25]:


df['Date']=df['timeStamp'].apply(lambda time:time.date())
df.head()



# In[26]:


df.groupby('Date').count().head()


# In[27]:


df.groupby('Date').count()['lat'].plot()
plt.tight_layout()


# In[28]:


df[df['Reason']=='Traffic'].groupby('Date').count()['lat'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[29]:


df[df['Reason']=='Fire'].groupby('Date').count()['lat'].plot()
plt.title('Fire')
plt.tight_layout()


# In[30]:


df[df['Reason']=='EMS'].groupby('Date').count()['lat'].plot()
plt.title('EMS')
plt.tight_layout()



# In[38]:


dayHour=df.groupby(by=['Day','Hour']).count()['Reason'].unstack()
dayHour


# In[36]:


sns.heatmap(dayHour,cmap='viridis')


# In[39]:


sns.clustermap(dayHour,cmap='viridis')


# In[40]:


dayMonth=df.groupby(by=['Day','Month']).count()['Reason'].unstack()
dayMonth


# In[41]:


sns.heatmap(dayMonth,cmap='viridis')


# In[42]:


sns.clustermap(dayMonth,cmap='viridis')

