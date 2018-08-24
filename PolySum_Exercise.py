
# coding: utf-8

# In[5]:


# import library 
import math


# In[ ]:


# define function polysum with two inside functions of area and perimeter
def polysum (n,s):
    def area (n,s):
        return (n*s**2)/(4*math.tan(math.pi/n))
    def per (n,s):
        return n*s
    # return sum of the area and squared perimeter
    return round (area(n,s) + per(n,s)**2, 4)


# In[6]:


# call a function
print(polysum (3,1))

