#!/usr/bin/env python
# coding: utf-8
# In[58]:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patches as mpatches


# First Data Set


x_0 = [7,7.75,8.5,9.25,10,10.75,11.5,12.25]
x_1 = [17,17.75,18.5,19.25,20,20.75,21.5,22.25]
x_2 = [27,27.75,28.5,29.25,30,30.75,31.5,32.25]
x_3 = [37,37.75,38.5,39.25,40,40.75,41.5,42.25]
y_0 = [1846,1771,1777,1860,1869,1874,1818,1749]
y_1 = [1428,1589,1417,1522,1467,1525,1499,1537]
y_2 = [1523,1493,1498,1462,1466,1553,1454,1447]
y_3 = [960,958,925,960,1048,1099,921,975]

#create legend

A_1 = mpatches.Patch(color='blue', label='A-1')
D_2 = mpatches.Patch(color='red', label='D-2')
E_1 = mpatches.Patch(color='cadetblue', label='E-1')
F_2 = mpatches.Patch(color='green', label='F-2')
G_2 = mpatches.Patch(color='brown', label='G-2')
G_4 = mpatches.Patch(color='midnightblue', label='G-4')
G_5 = mpatches.Patch(color='gray', label='G-5')
G_6 = mpatches.Patch(color='black', label='G-6')
plt.legend(handles=[A_1,D_2,E_1,F_2,G_2,G_4,G_5,G_6], fontsize = 18)


#Plot Graph 1

plt.xlabel('Item Measured', fontsize=22)
plt.title('Max Temperatures on Various Shops', fontsize=36)
plt.ylabel('Temperature (F)', fontsize=22)
plt.bar(x_0,y_0, color=['blue','red','cadetblue','green','brown','midnightblue','gray','black'])
plt.bar(x_1,y_1, color=['blue','red','cadetblue','green','brown','midnightblue','gray','black'])
plt.bar(x_2,y_2, color=['blue','red','cadetblue','green','brown','midnightblue','gray','black'])
plt.bar(x_3,y_3, color=['blue','red','cadetblue','green','brown','midnightblue','gray','black'])
plt.xticks([10,20,30,40],['Gob','Blank Mold\n w/ Gob','Parison','Empty\n Blank Mold'], fontsize=16)
plt.yticks([0,250,500,750,1000,1250,1500,1750,2000], fontsize= 16)


#set graph size

fig = plt.gcf()
fig.set_size_inches(18.5, 12)
fig.set_size_inches(18.5,12, forward=True)

#next data set

x_4 = [7,7.75,8.5,9.25,10,10.75,11.5,12.25]
x_5 = [17,17.75,18.5,19.25,20,20.75,21.5,22.25]
x_6 = [27,27.75,28.5,29.25,30,30.75,31.5,32.25]

y_4 = [118,139,141,198,207,176,173,176]
y_5 = [156,132,126,142,145,141,188,151]
y_6 = [751,714,643,671,649,675,811,569]

#create legend

A_1 = mpatches.Patch(color='blue', label='A-1')
D_2 = mpatches.Patch(color='red', label='D-2')
E_1 = mpatches.Patch(color='cadetblue', label='E-1')
F_2 = mpatches.Patch(color='green', label='F-2')
G_2 = mpatches.Patch(color='brown', label='G-2')
G_4 = mpatches.Patch(color='midnightblue', label='G-4')
G_5 = mpatches.Patch(color='gray', label='G-5')
G_6 = mpatches.Patch(color='black', label='G-6')

# plot graph 2
plt.bar(x_4,y_3, color=['blue','red','cadetblue','green','brown','midnightblue','gray','black'])
plt.bar(x_5,y_4, color=['blue','red','cadetblue','green','brown','midnightblue','gray','black'])
plt.bar(x_6,y_5, color=['blue','red','cadetblue','green','brown','midnightblue','gray','black'])
plt.xticks([10,20,30],['Plunger','Finish Mold:\n Open','Finish Mold:\n Closed'], fontsize=16)
plt.yticks([100,200,300,400,500,600,700,800], fontsize=16)
plt.legend(handles=[A_1,D_2,E_1,F_2,G_2,G_4,G_5,G_6], fontsize = 22)
plt.title('Max Temperatures on Various Shops', fontsize=36)
plt.xlabel('Item Measured', fontsize=22)
plt.ylabel('Temperature (F)',fontsize=22)

#set graph size

fig = plt.gcf()
fig.set_size_inches(18.5, 12)
fig.set_size_inches(18.5,12, forward=True)
