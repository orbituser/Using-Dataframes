# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:34:42 2023

@author: mozea
"""

import pandas as pd

data = {'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'], 'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'], 'Age': [30, 40, 25, 35, 45, 28], 'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'], 'Salary': [50000, 60000, 45000, 55000, 70000, 55000], 'Experience': [3, 7, 2, 5, 10, 4]}

employee_df = pd.DataFrame(data)
FirstThreeRows = employee_df.iloc[:3, :]
MarketingRow = employee_df.loc[:, "Department"]
AgeAndGender = employee_df.iloc[:4, [2,3]]
SalaryAndExperience = employee_df.loc[employee_df["Gender"] == "Male", ["Salary", "Experience"]]
