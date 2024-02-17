#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:48:32 2023

@author: jakobdietz
"""


# import pandas as pd
# import numpy as np
# # from asc_desc_working import process_data

# def calculate_stats(file_path):
#     # Load the dataset
#     data = pd.read_csv(file_path)

#     # Exclude non-numerical columns (like 'Date/Time')
#     numerical_data = data.select_dtypes(include=[np.number])

#     # Calculate minimum, maximum, and average for each numerical column
#     min_values = numerical_data.min()
#     max_values = numerical_data.max()
#     average_values = numerical_data.mean()

#     # Creating a DataFrame to display the results
#     stats_df = pd.DataFrame({
#         'Minimum': min_values,
#         'Maximum': max_values,
#         'Average': average_values
#     })

#     # Display the results
#     print(f"Stats for {file_path.split('/')[-1]}:")
#     print(stats_df)
#     print("\n")  # Adding a newline for readability
    
#     # Print net irradiance statistics
#     # print("Net Irradiance Statistics:")
#     # print("Ascend:\n", radiation_avg1)
#     # print("Descend:\n", radiation_avg2)
#     # print("\n")
    
    
 
    
#     # Emphasize specific columns
#     emphasized_columns = ['RH [%]', 'TTT grad [K]', 'LWD [W/m**2] (corrected)', 'LWU [W/m**2] (corrected)']
#     print("Emphasized Stats:")
#     for col in emphasized_columns:
#         if col in stats_df.index:
#             print(f"{col}:\n{stats_df.loc[col]}")
#             print("-" * 20)  # Separator for readability
#     print("\n" * 2)  # Adding extra newlines for separation

# # Example usage for four datasets
# file_paths = [
#     '/Users/jakobdietz/Uni Leipzig/Bachelor Thesis/Gottschalk-Egerer_2021_AO2018/csv_split/3radiation_corr_ascend.csv',
#     #'/Users/jakobdietz/Uni Leipzig/Bachelor Thesis/Gottschalk-Egerer_2021_AO2018/csv_split/3radiation_corr_ascend.csv',
#    # '/Users/jakobdietz/Uni Leipzig/Bachelor Thesis/Gottschalk-Egerer_2021_AO2018/csv_split/3radiation_corr_descend.csv',
#     '/Users/jakobdietz/Uni Leipzig/Bachelor Thesis/Gottschalk-Egerer_2021_AO2018/csv_split/3radiation_corr_descend.csv'
# ]

# for file_path in file_paths:
#     calculate_stats(file_path)
    
    




import numpy as np
import pandas as pd

from asc_desc_working import process_data


def calculate_stats(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Exclude non-numerical columns (like 'Date/Time')
    numerical_data = data.select_dtypes(include=[np.number])

    # Process first dataset (ascend)
    radiation_avg, _, _, _, _ = process_data(file_path)

    # Calculate minimum, maximum, and average for each numerical column
    stats_df = calculate_min_max_avg(numerical_data)

    radiation_stats_df = calculate_min_max_avg(radiation_avg)
    # Display the results
    print(f"Stats for {file_path.split('/')[-1]}:")
    print(stats_df)
    print(radiation_stats_df)
    print("\n")  # Adding a newline for readability
   


    # Emphasize specific columns
    # emphasized_columns = ['RH [%]', 'TTT grad [K]', 'LWD [W/m**2] (corrected)', 'LWU [W/m**2] (corrected)']
    # print("Emphasized Stats:")
    # for col in emphasized_columns:
    #     if col in stats_df.index:
    #         print(f"{col}:\n{stats_df.loc[col]}")
    #         print("-" * 20)  # Separator for readability
    # print("\n" * 2)  # Adding extra newlines for separation


def calculate_min_max_avg(column):
    # Calculate minimum, maximum, and average for each numerical column
    min_values = column.min()
    max_values = column.max()
    average_values = column.mean()

    # Creating a DataFrame to display the results
    stats_df = pd.DataFrame({
        'Minimum': min_values,
        'Maximum': max_values,
        'Average': average_values
    })

    return stats_df

file_paths = [
    '/Users/jakobdietz/Uni Leipzig/Bachelor Thesis/Gottschalk-Egerer_2021_AO2018/csv_split/4radiation_corr_ascend.csv',
   # '/Users/jakobdietz/Uni Leipzig/Bachelor Thesis/Gottschalk-Egerer_2021_AO2018/csv_split/3radiation_corr_ascend.csv',
   # '/Users/jakobdietz/Uni Leipzig/Bachelor Thesis/Gottschalk-Egerer_2021_AO2018/csv_split/3radiation_corr_descend.csv',
    '/Users/jakobdietz/Uni Leipzig/Bachelor Thesis/Gottschalk-Egerer_2021_AO2018/csv_split/4radiation_corr_descend.csv'
]

for file_path in file_paths:
    calculate_stats(file_path)
