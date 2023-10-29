#!/usr/bin/env python
# coding: utf-8

# # Q1) Create a null vector of size 10 but the fifth value which is 1.

# In[1]:


import numpy as np
x = np.zeros(10)
print(x)
print("fifth value is 1")
x[5] = 1
print(x)


# # Q2) Create a vector with values ranging from 10 to 49.

# In[4]:


import numpy as np
v = np.arange(10,49)
print("Given vector:")
print(v)
print("Resultant vector")
v[1:-1]
print(v)


# # Q3) Create a 3x3 matrix with values ranging from 0 to 8

# In[1]:


import numpy as np

matrix = np.arange(9).reshape(3, 3)

print(matrix)


# # Q4) Find indices of non-zero elements from [1,2,0,0,4,0]

# In[12]:


import numpy as np
a = np.array([1,2,0,0,4,0])
print("Given array:")
print(a)
print("Indices of non-zero elements:")
result = np.where(a != 0)[0]
print(result)


# # Q5) Create a 10x10 array with random values and find the minimum and maximum values.

# In[15]:


import numpy as np
x = np.random.random((10,10))
print("Given array:")
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)


# # Q6) Create a random vector of size 30 and find the mean value.

# In[1]:


import numpy as np
x = np.random.random(30)
print("Given array:")
print(x)
a = x.mean()
print("Mean value:")
print(a)


# In[ ]:




