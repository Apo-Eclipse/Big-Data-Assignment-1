# preprocessing
import sklearn
from sklearn import preprocessing
import pandas as pd
import numpy as np
from eda import EDA

def preprocessing(df):  
    # cleaning
    # remove duplicates
    df.drop_duplicates(subset=['gender', 'age', 'category', 'quantity','price', 'payment_method','shopping_mall'], keep='first', inplace=True)
    
    # cleaning 
    # not all dates are in the same format
    def r_format(arg):
        left_ind = arg.find('/')
        if left_ind == 1:
            arg = '0' + arg
            left_ind+=1
        if arg[left_ind+2] == '/':
            arg = arg[:left_ind+1] + '0' + arg[left_ind+1:]
        return arg
    
    df['invoice_date'] = df['invoice_date'].apply(r_format)
    df['invoice_date'] = pd.to_datetime(df['invoice_date'], format='%d/%m/%Y')
    
    
    def categorization(price,step1,step2):
        if price < step1:
            return 0
        elif price < step2:
            return 1
        else:
            return 2

    # discretizing 
    # for price column
    step1 = df.price.quantile(1/3)
    step2 = df.price.quantile(3/4)
    df['categorized_price'] = df['price'].apply(categorization,step1=step1,step2=step2)
    
    
    # discretizing
    # for age column
    step1 = df.age.quantile(1/3)
    step2 = df.age.quantile(3/4)
    df['categorized_ages'] = df['age'].apply(categorization,step1=step1,step2=step2)
    
    
    #Transformation
    df['month'] = pd.to_datetime(df['invoice_date']).dt.month
    df['year'] = pd.to_datetime(df['invoice_date']).dt.year
    df['day'] = pd.to_datetime(df['invoice_date']).dt.day
    df.drop(columns=['invoice_date','invoice_no'], inplace=True)

    
    # reduction
    df_out = df.copy()
    df_out.drop(columns=['price','month','year','day','customer_id'], inplace=True)
    
    
    # encoding categorical columns
    le = sklearn.preprocessing.LabelEncoder()
    categorical_columns = ['gender', 'category', 'payment_method', 'shopping_mall']
    for col in categorical_columns:
        df_out[col] = le.fit_transform(df_out[col])
    
    # Transformation
    standardize = sklearn.preprocessing.StandardScaler()
    df_stan = standardize.fit_transform(df_out)
    
    pd.DataFrame(df_stan).to_csv('res_dpre.csv', index=False)
    EDA(df)