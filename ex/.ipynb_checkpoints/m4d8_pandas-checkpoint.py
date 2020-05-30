#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


indata = pd.read_csv("../dataset/customerdata.csv")


# In[4]:


type(indata)


# In[8]:


indata.to_csv("./test.csv")
# 파일데이터를 불러 모은 다음 내가 한 곳에다 저장 가능
indata.to_csv("./test2.csv", index=False)


# In[ ]:


def 

