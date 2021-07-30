#!/usr/bin/env python
# coding: utf-8

# In[56]:


import csv
import matplotlib.pyplot as plt
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
print(matplotlib.get_cachedir())


# In[57]:


data = csv.reader(open('data/seoul.csv', encoding='utf-8'))


# In[58]:


next(data)


# In[59]:


data = list(data)


# In[60]:


# [print(i) for i in data]


# In[61]:


# [print(i[-1]) for i in data] # show_highest_temperature


# In[62]:


highest_temperatures = []
[highest_temperatures.append(float(i[-1])) for i in data if i[-1] != '']
print(f'총 개수 : {len(highest_temperatures)}개')


# In[63]:


plt.plot(highest_temperatures, 'lightpink')
plt.plot(figsize=(20, 2))
plt.show()


# In[64]:


high = []
low = []
for i in data:
    if i[-1] != '' and i[-2] != '':
        if 1983 <= int(i[0].split('-')[0]):
            if i[0].split('-')[1] == '03' and i[0].split('-')[2] == '05':
                high.append(float(i[-1]))
                low.append(float(i[-2]))


# In[65]:


plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False
plt.title('ChangedTemperaturesOnMyBirthday')
plt.plot(high, 'pink', label='high')
plt.plot(low, 'skyblue', label='low')
plt.legend()
plt.show()

