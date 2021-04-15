import pandas as pd
import acquire as a
import numpy as np
import datetime

def prep_zstore(df):
    """
    prep_zstore 
    - sets index to datetime typed `sale_date`
    - removes timezone from index
    - adds month, day_of_week & sales_totals columns
    """

    #converts obj to datetime
    df.sale_date = pd.to_datetime(df.sale_date)
    
    #set index to date
    df = df.set_index('sale_date').sort_index()
    
    #remove time signature
    df.index = df.index.tz_localize(None)
    
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df