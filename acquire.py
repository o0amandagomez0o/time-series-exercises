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