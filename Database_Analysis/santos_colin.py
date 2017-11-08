
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:

df = pd.read_csv("ratings.csv")
dff = df.iloc[:, 2:]


# In[3]:

rvars = np.var(dff)
np.mean(rvars)


# In[4]:

rounded = rvars.round(1)[~np.isnan(rvars)]


# In[5]:

plt.hist(rounded)
plt.title("Frequency of variances")
plt.xlabel("Variance")
plt.ylabel("Frequency (rounded)")
plt.show()


# In[ ]:



