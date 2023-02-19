#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

NEW_COLUMNS = ['index', 'customer', 'state', 'customer_lifetime_value',
              'response', 'coverage', 'education', 'effective_to_date',
              'employment_status', 'gender', 'income', 'location_code',
              'marital_status', 'monthly_premium_auto', 'months_since_last_claim',
              'months_since_policy_inception', 'number_of_open_complaints',
              'number_of_policies', 'policy_type', 'policy', 'renew_offer_type',
              'sales_channel', 'total_claim_amount', 'vehicle_class', 'vehicle_size',
              'vehicle_type']

CSV_FILE ="marketing_customer_analysis.csv"

def read_csv(csv_file):
       df = pd.read_csv(csv_file)
       return df

df = read_csv(CSV_FILE)

#1.Show the dataframe shape.
def show_shape(df):
       return df.shape

print(show_shape(df))

#2.Standardize header names

def rename_columns(new_columns):
       df.columns = new_columns
       return df

#3.Which columns are numerical?

def get_numeric(df):
       numeric_df = df._get_numeric_data()
       return numeric_df


#4. Which columns are categorical?

def get_categorical(df):
       categorical_df = df.select_dtypes('object')
       return categorical_df


#5.Check and deal with NaN values.
# Percentage of NaN values in each column

def percentage_nan(df):
       null_df = pd.DataFrame(df.isna().sum()/len(df)*100)
       return null_df

# Drop "vehicle_type" column due to high number of NaN values (>50%).

# df = df.drop(['vehicle_type'], axis=1)


# Only take rows where 'state', 'months_since_last_claim' and 'vehicle_class' are not NaN.
# df = df[df.state.notna()]
# df = df[df.months_since_last_claim.notna()]
# df = df[df.vehicle_class.notna()]

# Confirm that we do not have NaN values in the dataframe.
# null_df = pd.DataFrame(df.isna().sum()/len(df)*100)
# null_df


#6. Datetime format - Extract the months from the dataset and store in a separate column. 
# Convert the 'effective_to_date' column to DateTime format

# df['effective_to_date'] = pd.to_datetime(df['effective_to_date'], errors='coerce')


# df.dtypes


# Extract the months from the dataset and store in a separate column.
# df['month'] = pd.DatetimeIndex(df['effective_to_date']).month


# df.head()


#Filter the data to show only the information for the first quarter , ie. January, February and March. 
#Hint: If data from March does not exist, consider only January and February.
# df_first_quarter = df[(df.month == 1) | (df.month == 2) | (df.month == 3)]


# df_first_quarter


# df.to_csv("processed_marketing_customer_analysis.csv")
