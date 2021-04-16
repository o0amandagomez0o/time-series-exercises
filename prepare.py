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






def prep_opsd(opsd):
    """
    prep_opsd 
    - sets index to datetime typed `Date`
    - adds month & year columns
    - fills na's with 0 
    """
    
    #change dtype to datetime
    opsd.Date = pd.to_datetime(opsd.Date)
    
    #set date to index
    opsd = opsd.set_index('Date').sort_index()
    
    #add month/year columns
    opsd['month'] = opsd.index.month
    opsd['year'] = opsd.index.year
    
    #fill nan's
    opsd = opsd.fillna(0)
    
    return opsd