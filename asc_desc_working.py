#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 01:41:09 2023

@author: jakobdietz
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calculate_and_plot(file_path_radiation_asc, file_path_radiation_desc):
    # Function to load and process data


    # Process first dataset (ascend) 
    # wird unten aufgerufen
    radiation_avg1, humidity_avg1, mid_points1, start_date_asc, end_date_asc = process_data(file_path_radiation_asc)
    # Process second dataset (descend)
    radiation_avg2, humidity_avg2, mid_points2, start_date_desc, end_date_desc = process_data(file_path_radiation_desc)

    # Visualization
    plt.figure(figsize=(20, 12))

    # Fnet - Ascend plot
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(radiation_avg1['Net Irradiance [W/m**2]'].values, mid_points1, label='Fnet', linestyle='-', linewidth=0.7,color='black')
    ax1.set_xlabel('Net Irradiance [W/m**2]')
    ax1.set_ylabel('Height [m]')
    ax1.set_title(f'Fnet - Ascend ({start_date_asc} to {end_date_asc})')
    ax1.legend()
    ax1.grid(True)
    ax1.set_xlim(-100, 10)  # Set x-axis limits for Fnet plot

    # Fnet - Descend plot
    ax2 = plt.subplot(2, 2, 2)
    ax2.plot(radiation_avg2['Net Irradiance [W/m**2]'].values, mid_points2, label='Fnet', linestyle='-', linewidth=0.7, color='black')
    ax2.set_xlabel('Net Irradiance [W/m**2]')
    ax2.set_title(f'Fnet - Descend ({start_date_desc} to {end_date_desc})')
    ax2.legend()
    ax2.grid(True)
    ax2.set_xlim(-100, 10)  # Set x-axis limits for Fnet plot

    # Temperature and Humidity - Ascend plot
    ax3 = plt.subplot(2, 2, 3)
    ax3.plot(humidity_avg1['TTT grad [K]'].values, mid_points1, label='Temp. Grad.', linestyle='-', linewidth=0.7, color='firebrick')
    ax3.set_xlabel('Average Temperature Gradient [K]')
    ax3.set_ylabel('Height [m]')
   # ax3.set_title('Temperature and Humidity - Ascend')
    ax3.legend(loc='lower right')
    ax3.grid(True)
    ax3.set_xlim(260, 280)

    # Create a second x-axis for RH - Ascend
    ax4 = ax3.twiny()
    ax4.plot(humidity_avg1['RH [%]'].values, mid_points1, label='RH', linestyle='-', linewidth=0.7, color='steelblue')
    ax4.set_xlabel('Average Humidity [%]')
    ax4.legend(loc='upper right')
    ax4.set_xlim(50, 100)
                
    # Temperature and Humidity - Descend plot
    ax5 = plt.subplot(2, 2, 4)
    ax5.plot(humidity_avg2['TTT grad [K]'].values, mid_points2, label='Temp. Grad', linestyle='-', linewidth=0.7, color='firebrick')
    ax5.set_xlabel('Average Temperature Gradient [K]')
   # ax5.set_title('Temperature and Humidity - Descend')
    ax5.legend(loc='lower right')
    ax5.grid(True)
    ax5.set_xlim(260, 280)
    
    # Create a second x-axis for RH - Descend
    ax6 = ax5.twiny()
    ax6.plot(humidity_avg2['RH [%]'].values, mid_points2, label='RH', linestyle='-', linewidth=0.7, color='steelblue')
    ax6.set_xlabel('Average Humidity [%]')
    ax6.legend(loc='upper right')
    ax6.set_xlim(50, 100)

    plt.suptitle('Ascend and Descend Dataset 6', fontsize=16)
    plt.show()
    
def process_data(file_path_radiation):
    data = pd.read_csv(file_path_radiation)
    columns_radiation = ['LWD [W/m**2] (corrected)', 'SWD [W/m**2] (corrected)', 
                         'LWU [W/m**2] (corrected)', 'SWU [W/m**2] (corrected)']
    radiation_data = data[columns_radiation + ['Height [m]']]
    
   
    humidity_data = data[['RH [%]', 'TTT grad [K]', 'Height [m]']]
    
    height_intervals = pd.interval_range(start=0, end=max(data['Height [m]'].max(), data['Height [m]'].max()), freq=10)
    radiation_avg = radiation_data.groupby(pd.cut(radiation_data['Height [m]'], height_intervals)).mean()
    humidity_avg = humidity_data.groupby(pd.cut(humidity_data['Height [m]'], height_intervals)).mean()
    
   
    radiation_avg['Net Irradiance [W/m**2]'] = (radiation_avg['LWD [W/m**2] (corrected)'] - radiation_avg['LWU [W/m**2] (corrected)'])#(radiation_avg['LWD [W/m**2] (corrected)'] - radiation_avg['LWU [W/m**2] (corrected)']) #+ \
                                              # (radiation_avg['SWD [W/m**2] (corrected)'] - radiation_avg['SWU [W/m**2] (corrected)'])                                 
    mid_points = np.array([(interval.left + interval.right) / 2 for interval in height_intervals])
    return radiation_avg, humidity_avg, mid_points, data['Date/Time'].iloc[0], data['Date/Time'].iloc[-1]
