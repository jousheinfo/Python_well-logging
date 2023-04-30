# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:10:08 2022

@author: User
"""


#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

word_start = '~Ascii'

#Opening .txt file
with open("X_well_log.las","r") as infile:
    
    #Reading line by line
    for idx,line in enumerate(infile):

        content = infile.readlines()

        #Knowing total number of lines
        print("Number of lines is {}".format(len(content)))
        #print(content)
        
        data = content[30:]
        
        #Knowing total number of lines
        print("Number of lines is {}".format(len(data)))
        
    with open("well_log_data.txt", 'w') as outfile:
        for new_content in (data):
            #print(new_content)
            outfile.write(new_content)
                
#Reading data
data_df = pd.read_csv('well_log_data.txt', header=None, skiprows=(1), delim_whitespace=True)
data_df.columns = ['Depth', 'Permeability', 'Gamma', 'Porosity', 'Fluvial_facies', 'NetGros']

#Physical data
depth = data_df['Depth'][4:len(data_df['Depth'])-4]
permeability = data_df['Permeability'][4:len(data_df['Permeability'])-4]
gamma = data_df['Gamma'][4:len(data_df['Gamma'])-4]
porosity = data_df['Porosity'][4:len(data_df['Porosity'])-4]

fig, (ax1,ax2,ax3) = plt.subplots(1,3)

ax1.plot(permeability, depth, color='blue')
ax1.set_xlabel('Permeability', fontweight ='bold')
ax1.set_ylabel('Depth', fontweight ='bold')
ax1.xaxis.set_label_position('top')
ax1.xaxis.tick_top()
ax1.invert_yaxis()

ax2.plot(gamma, depth, color='yellow')
ax2.set_xlabel('Gamma', fontweight ='bold')
ax2.set_ylabel('Depth', fontweight ='bold')
ax2.xaxis.set_label_position('top')
ax2.xaxis.tick_top()
ax2.invert_yaxis()

ax3.plot(porosity, depth, color='brown')
ax3.set_xlabel('Porosity', fontweight ='bold')
ax3.set_ylabel('Depth', fontweight ='bold')
ax3.xaxis.set_label_position('top')
ax3.xaxis.tick_top()
ax3.invert_yaxis()