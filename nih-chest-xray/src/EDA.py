#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("../data/Data_Entry_2017.csv")


# In[3]:


data.head()


# In[4]:


data.columns = ['Image_Index', 'Finding_Labels', 'Follow_Up_#', 'Patient_ID', 'Patient_Age', 'Patient_Gender',
                'View_Position', 'Original_Image_Width', 'Original_Image_Height', 
                'Original_Image_Pixel_Spacing_X', 'Original_Image_Pixel_Spacing_Y', 'Unnamed']


# In[5]:


# Check if number is in years, months, or days
data['Age_Measure'] = data['Patient_Age'].astype(str).str[3]

# Remove the character in Patient Age, and convert to integer
data['Patient_Age'] = data['Patient_Age'].map(lambda x: str(x)[:-1]).astype(int)


# In[6]:


data.drop('Unnamed', axis=1, inplace=True)


# In[7]:


data.head()


# In[8]:


data.Finding_Labels.value_counts().head(20)


# In[9]:


data[data['Patient_Age'] == 414]


# In[10]:


data.Finding_Labels.value_counts().head(20)


# In[11]:


data.drop(['Original_Image_Pixel_Spacing_X', 'Original_Image_Pixel_Spacing_Y'], axis = 1, inplace = True)


# In[12]:


data.drop(['Original_Image_Width', 'Original_Image_Height'], axis = 1, inplace = True)
data.head()


# In[14]:


total_visits = data.groupby('Patient_ID')['Image_Index'].count().reset_index()


# In[20]:


total_visits.sort_values(by="Image_Index", ascending=False).head(10)


# In[ ]:




