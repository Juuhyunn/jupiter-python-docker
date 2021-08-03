#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import matplotlib.pyplot as plt
import numpy


# In[2]:


data = csv.reader(open('./data/202106_202106_연령별인구현황_월간.csv', encoding='utf-8'))
next(data)
data = list(data)


# In[4]:


for i in data:
    if '방이1동' in i[0]:
        arr = numpy.array(i[3:], dtype=int) / int(i[2].replace(',', ''))


# In[5]:


plt.title('Population-01')
plt.style.use('ggplot')
plt.plot(arr)

