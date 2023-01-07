#!/usr/bin/env python
# coding: utf-8

# In[323]:


import pandas as pd
import numpy as np
from statistics import mean
import math
from matplotlib import pyplot as plt


# In[324]:


data  = pd.read_csv(r"C:\Users\User\Desktop\data5.csv")


# In[325]:


data


# In[331]:


emisssions_sorted = data.sort_values(by=['CO2_emissions_metric_tons_per_capita'])
# print(emissions_sorted)


# In[328]:


emissions = data['CO2_emissions_metric_tons_per_capita']
emissions_list = list(map(float, emissions))
emissions_average = math.fsum(emissions_list)/len(emissions_list)
print(emissions_average)


# In[329]:


plt.legend (["Year is x , CO2 emissions (metric tons per capita) is y"])
plt.xlabel("Year")
plt.ylabel("CO2 emissions (metric tons per capita)")
plt.plot(data.Year, data.CO2_emissions_metric_tons_per_capita)
for x in range(0, 3): 
    plt.plot(data[data.eq(emissions_sorted[x]).any(1)].Year, emissions_sorted[x], 'go')
for x in range(len(emissions_sorted)-3, len(emissions_sorted)):
    plt.plot(data[data.eq(emissions_sorted[x]).any(1)].Year, emissions_sorted[x], 'bo')
plt.plot(data[data.eq(emissions_sorted[round(len(emissions_sorted)/2)]).any(1)].Year, emissions_sorted[round(len(emissions_sorted)/2)], 'ro')
plt.show()

