import pandas as pd
import requests
from io import StringIO





def get_items():
    """
    creates empty list
    - requests a data structure from "https://python.zach.lol/api/v1/items"
    - reads the `n` number of pages of items.
    - loops through to retrieve data dictionaries from each page and append to empty list.
    returns: appended list as a DataFrame
    """
    
    items_list = []
    url = "https://python.zach.lol/api/v1/items"
    
    response = requests.get(url)
    data = response.json()
    
    n = data['payload']['max_page']
    
    for i in range(1, n+1):
        new_url = url+'?page='+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_items = data['payload']['items']
        items_list += page_items
        
    items = pd.DataFrame(items_list)
        
    return items






def get_stores():
    """
    creates empty list
    - requests a data structure from "https://python.zach.lol/api/v1/stores"
    - reads the `n` number of pages of items.
    - loops through to retrieve data dictionaries from each page and append to empty list.
    returns: appended list as a DataFrame
    """
    
    stores_list = []
    url1 = "https://python.zach.lol/api/v1/stores"
    
    response = requests.get(url1)
    data = response.json()
    
    n = data['payload']['max_page']
    
    for i in range(1, n+1):
        new_url = url1+'?page='+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_stores = data['payload']['stores']
        stores_list += page_stores
            
        stores = pd.DataFrame(stores_list)
        
    return stores







def get_sales():
    """
    creates empty list
    - requests a data structure from "https://python.zach.lol/api/v1/sales"
    - reads the `n` number of pages of items.
    - loops through to retrieve data dictionaries from each page and append to empty list.
    returns: appended list as a DataFrame
    """
    
    sales_list = []
    url2 = "https://python.zach.lol/api/v1/sales"
    
    response = requests.get(url2)
    data = response.json()
    
    n = data['payload']['max_page']
    
    for i in range(1, n+1):
        new_url = url2+'?page='+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_sales = data['payload']['sales']
        sales_list += page_sales
        
    sales = pd.DataFrame(sales_list)
        
    return sales





def merge_zachlol():
    """
    creates df1 dataframe from: 
    - merged `items` df with `sales` df on `item` key
    merges df1 with `stores` df on `store` key
    - drops repeated columns
    
    returns: df
    """
    
    # create the three dfs
    items = get_items()
    stores = get_stores()
    sales = get_sales()
    
    # merges the three dfs
    df1 = items.merge(sales, left_on="item_id", right_on="item", how= 'outer')
    
    df = df1.merge(stores, left_on="store", right_on="store_id", how= 'outer')
    
    df = df.drop(columns=["item", "store"])
    
    return df





def get_opsd():
    """
    
    """
    
    url = "https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv"

    s = requests.get(url).content
    opsd_df = pd.read_csv(StringIO(s.decode('utf-8')))
    
    return opsd_df





def get_df(url, ):
    """
    
    """
    
    if cached == False:
        stores_list = []
        url = "https://python.zach.lol/api/v1/stores"
        response = requests.get(url)
        data = response.json()
        n = data['payload']['max_page']
        
        
        for i in range(1, n+1):
            new_url = url + '?page=' + str(i)
            response = requests.get(new_url)
            data = response.json()
            page_stores = data['payload']['stores']
            stores_list += page_stores
        stores = pd.DataFrame(stores_list)
        stores.to_csv('stores.csv')
    else:
        stores = pd.read_csv('stores.csv', index_col=0)
    return stores