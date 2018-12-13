
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob


# In[2]:


#littrow mode grating equation
# for R6 grating

#order
m = 0

#wavelength (in nm)
lam = 0

#slit (in nm)
# 13.33 groves/mm
# 1mm = 1000000 microns
# find d in microns
gpmm = 13.33
gpnm = 13.333/1000000
d = 1000000/13.33

#blaze angle (in radians)
#80.7 degrees
thetab = 80.7*(np.pi/180)
print(thetab)

# incident, diffraction angle (in radians)
#9.3 degrees
#theta = 9.3*(np.pi/180)
theta = 0
print(theta)

#off plane angle (in radians)
gamma = 0


# In[3]:


def calc_blaze_peak_order_gamma(lam, gamma):

    m = (2*d*np.sin(thetab)*np.cos(theta)*np.cos(gamma))/lam
    
    print("blaze peak at")
    print(str(lam) + " nm, with off plane angle (degrees) of:")
    print(gamma*(180/np.pi))
    print("is at order:")
    print(m)
    
    return m
    #print(m)


# In[4]:


gamma=np.arctan(60/550)/2
morder = calc_blaze_peak_order_gamma(543,gamma)


# In[5]:


gamma=np.arctan(110/550)/2
morder = calc_blaze_peak_order_gamma(543,gamma)


# In[6]:


gamma=np.arctan(20/550)/2
morder = calc_blaze_peak_order_gamma(633,gamma)


# In[7]:


gamma=np.arctan(90/550)/2
morder = calc_blaze_peak_order_gamma(633,gamma)


# In[8]:


morder = calc_blaze_peak_order_gamma(1478,0)

