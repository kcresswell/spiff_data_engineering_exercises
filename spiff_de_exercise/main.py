"""
Spiff DE Exercise 
Kayla Cresswell
Feb 08 2023
"""

import json
import pandas as pd 

def main(): 
    # Set to True if you'd like to see print statements for debugging
    print_lines:bool = False  

    # Return JSON data from files as dataframes
    df_deals:pd.DataFrame() = read_json_to_df(file_path='data/deals.json', print_lines=print_lines) 
    df_products:pd.DataFrame() = read_json_to_df(file_path='data/products.json', print_lines=print_lines) 

    # Calculate Commissions for the entire dataframe 
    df_commissions:pd.DataFrame() = get_df_commissions(df_deals=df_deals, df_products=df_products, print_lines=print_lines)
    
    # Return Commission Calcuation for specific salesperson between start and end dates 
    calculate_commission(sales_rep_name='Ian', start_date='2023-04-15', end_date='2023-05-15', df_commissions=df_commissions, print_lines=True)
    calculate_commission(sales_rep_name='David', start_date='2023-01-01', end_date='2023-02-01', df_commissions=df_commissions, print_lines=True)
    calculate_commission(sales_rep_name='Brad', start_date='2023-03-01', end_date='2023-06-30', df_commissions=df_commissions, print_lines=True)

    return 'Commissions Calculated!'


def read_json_to_df(file_path:str, print_lines:bool) -> pd.DataFrame():
    """
    Converts JSON to DataFrame 
    Parameters: 
        - file_path: path to JSON data file
        - print_lines: boolean, set to True to see print statements for debugging
    Returns: 
        - dataframe of json data 
    """
    df = pd.read_json(file_path)

    if(print_lines): 
        print(f'Column Names: {df.columns}')
        print(df.head(10))
    
    return df 

# Function to calculate commission
def get_df_commissions(df_deals:pd.DataFrame(), df_products:pd.DataFrame(), print_lines:bool) -> pd.DataFrame(): 
    """
    Merges the deals and products dataframe and calculates their commission for each row.
    Parameters: 
        - df_deals: dataframe of deals data
        - df_products: dataframe of products data
        - print_lines: boolean, set to True to see print statements for debugging
    Returns: 
        - dataframe containing new 'commission' column that is caculated for each row in the dataframe
    """
    # Merge the deals and products dataframes on the 'product_id' column
    df = df_products.merge(df_deals, left_on='id', right_on='product_id', how='inner')
    df = df.drop(columns=['id_x', 'id_y']) # drop id columns

    # Add a new column 'commission' to the merged dataframe, using the following formula:
    # quantity_products_sold * product_amount * commission_rate
    df['commission'] = df['quantity_products_sold'] * df['product_amount'] * df['commission_rate']

    if(print_lines): 
        print(f'Column Names: {df.columns}')
        print(df.head(10))
 
    return df

def calculate_commission(sales_rep_name:str, start_date:str, end_date:str, df_commissions:pd.DataFrame(), print_lines:bool) -> float:
    """
    Function/method to calculate commission for a sales rep in a given time period.

    Parameters:
        - sales_rep_name: Name of the sales rep to calculate commission for.
        - start_date: Starting date for the date range where commissions will be valid.
        - end_date: Ending date for the date range where commissions will be valid.

    Returns:
        float: A single float value for total commission amount based on the input criteria. e.g. $749.48
    """
 
    # row = df_commissions.loc[df_commissions['sales_rep_name'] == sales_rep_name]
    
    row = df_commissions.loc[(df_commissions['sales_rep_name'] == sales_rep_name) & (df_commissions['date'] >= start_date) & (df_commissions['date'] <= end_date)]
    print(row)
    df = row.copy() 
    com = df['commission']
    total_commissions = com.sum(axis=0) 

    if(print_lines):  
        print(f'Total Commissions: {sales_rep_name} made ${total_commissions} in commissions between {start_date} and {end_date}')
    
    return total_commissions

if __name__ == "__main__":
    main()