# EDA
from numpy import floor 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def EDA(df):
    # first
    total = floor(df.groupby(['month','year'])['customer_id'].count().groupby('month').mean())
    total.name = 'floored average number of customers per month for all year'
    total.sort_values(ascending=False, inplace=True)
    total.to_csv('eda-in-1.txt', sep='\t', index=True)

    # second
    df2 = df[['categorized_price','payment_method']]
    eda2 = df2[df2.categorized_price == 2].value_counts()
    eda2.name = 'counts of payment methods for products in the fourth quartile'
    eda2.to_csv('eda-in-2.txt', sep='\t', index=True)

    # third
    sales_df = df[['shopping_mall','price','quantity']]
    sales_df['total_sales'] = sales_df['price'] * sales_df['quantity']
    sales_df = sales_df.groupby('shopping_mall')['total_sales'].sum()
    sales_df.name = 'total sales for each shopping mall'
    sales_df.sort_values(ascending=False, inplace=True)
    sales_df.to_csv('eda-in-3.txt', sep='\t', index=True)