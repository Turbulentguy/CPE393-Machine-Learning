import pandas as pd
import matplotlib.pyplot as plt

def data_manipulate():

    df = pd.read_csv('retail_store_sales.csv')

    print(df.head())

    print(df.info())

    # Check of Null
    print(df.isnull().sum())

    # Check number of categories
    print(pd.crosstab(df['Category'], columns = 'N'))


    # Check outlier for numerical columns
    list = ['Price Per Unit', 'Quantity', 'Total Spent']

    # Making the for loop to check for outlier data
    for i in list:

        Q1 = df[i].quantile(0.25)

        Q3 = df[i].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - (1.5 * IQR)

        upper = Q3 + (1.5 * IQR)

        print(i)

        print(df[(df[i] < lower) | (df[i] > upper)])

    # Question 1: In the data set is there any column containing Null?
    # Answer: Yes, there are Nulls in columns "Price Per Unit", "Quantity", "Total Spent".

    # Question 2: Is there any outlier in this data set?
    # Answer: Yes, it's containing outlier data in "Total Spent" column.

    # Question 3: Why is it contain Nulls in those columns?
    # Answer: 