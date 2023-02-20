#!/usr/bin/env python
# coding: utf-8

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
PERCENTAGE_VALUE = 50

def read_csv(csv_file):
       print('Reading csv file...')
       df = pd.read_csv(csv_file)
       print("CSV file imported into a DataFrame")
       print(df.head())
       return df

df = read_csv(CSV_FILE)

#Show the dataframe shape.
def show_shape(df):
       return "The shape of the input DataFrame is:", df.shape

print(show_shape(df))

#Standardize header names

def rename_columns(new_columns):
       df.columns = new_columns
       return df

#Return numeric columns

def get_numeric(df):
       numeric_df = df._get_numeric_data()
       return "The numeric columns are: ", numeric_df


#Return categorical columns

def get_categorical(df):
       categorical_df = df.select_dtypes('object')
       return "The categorical columns are: ", categorical_df


#Check NaN values
# Percentage of NaN values in each column

def percentage_nan(df):
       null_df = df.isna().sum()/len(df)*100
       return "The percentage of missing values is:", null_df

print(percentage_nan(df))

# Drop columns with high number of NaN values (>50%).

def drop_columns_nan(df, null_df, percentage_value):
       for item in null_df.index:
              print(item)
              # if null_df.loc[item] > percentage_value:
                     # print(item)
                     # df.drop([item], inplace=True, axis=1)
       # return "Dropping column: ", item, "due to percentage of NaN values greater than:", percentage_value
       # return df
print(drop_columns_nan(df, percentage_nan(df), PERCENTAGE_VALUE))


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
