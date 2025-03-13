import pandas as pd

def data_manipulate():

    import os
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    csv_path = os.path.join(BASE_DIR, "retail_store_sales.csv")

    df = pd.read_csv(csv_path)

    print(df.head())

    print(df.info())

    # Check of Null
    print(df.isnull().sum())

    # Check number of categories
    print(pd.crosstab(df['Category'], columns = 'N'))


    # Check outlier for numerical columns
    Col = ['Price Per Unit', 'Quantity', 'Total Spent']

    # Making the for loop to check for outlier data
    for i in Col:

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
    # The dataset contains null values in several columns, which can be attributed to various reasons:
    # 1. **Price Per Unit**: Null values in this column could indicate that the price information was not available or not applicable for certain transactions.
    # 2. **Quantity**: Similar to the price per unit, the quantity might not have been recorded for some transactions, leading to null values.
    # 3. **Total Spent**: If either the price per unit or quantity is missing, the total spent cannot be calculated, resulting in null values in this column.
    # These null values can arise due to data entry errors, missing information at the time of transaction, or specific business rules that do not require certain fields to be filled for some transactions.