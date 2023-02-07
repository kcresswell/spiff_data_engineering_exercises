import json
import pandas as pd
from decimal import Decimal

def main(): 
    # Set to True if you'd like to see print statements for debugging
    print_lines = False  

    # Return JSON data from files as dataframes
    df_deals = read_json_to_df(file_path='data/deals.json', print_lines=print_lines) 
    df_products = read_json_to_df(file_path='data/products.json', print_lines=print_lines) 

    # Calculate Commissions for the entire dataframe 
    df_commissions = get_df_commissions(df_deals=df_deals, df_products=df_products, print_lines=print_lines)
    
    # Return Commission Calcuation for specific salesperson between start and end dates 
    calculate_commission(sales_rep_name='Ian', start_date='2023-04-15', end_date='2023-05-15', df_commissions=df_commissions, print_lines=True)

    return 'Commissions Calculated!'


def read_json_to_df(file_path, print_lines) -> pd.DataFrame():
    """
    """
    df = pd.read_json(file_path)

    if(print_lines): 
        print(f'Column Names: {df.columns}')
        print(df.head(10))
    
    return df 

# Function to calculate commission
def get_df_commissions(df_deals, df_products, print_lines) -> pd.DataFrame(): 
    """
    """
    # Merge the deals and products dataframes on the 'product_id' column
    # df = pd.merge(df_deals, df_products, on='product_id')
    df = df_products.merge(df_deals, left_on='id', right_on='product_id', how='inner')

    # Add a new column 'commission' to the merged dataframe, using the following formula:
    # quantity_products_sold * product_amount * commission_rate
    df['commission'] = df['quantity_products_sold'] * df['product_amount'] * df['commission_rate']

    if(print_lines): 
        print(f'Column Names: {df.columns}')
        print(df.head(10)) # TODO
 
    return df

def calculate_commission(sales_rep_name, start_date, end_date, df_commissions, print_lines):
    """
    Function/method to calculate commission for a sales rep in a given time period.

    Args:
        sales_rep_name (str): Name of the sales rep to calculate commission for.
        start_date (str): Starting date for the date range where commissions will be valid.
        end_date (str): Ending date for the date range where commissions will be valid.

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