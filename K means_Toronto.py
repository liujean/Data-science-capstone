# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 00:44:01 2019

@author: jean2
"""
# =============================================================================
# K Means: segmenting neighborhoods in Toronto
# =============================================================================
from bs4 import BeautifulSoup
import requests
import pandas as pd


# assign the link of the website to scrape the data
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text

soup = BeautifulSoup (website_url,'lxml')
print(soup.prettify())

# all table contents are under class "wikitable sortable"
My_table = soup.find('table',{'class':'wikitable sortable'})
table_rows = My_table.findAll('tr')

data = []
for row in table_rows:
    data.append([t.text.strip() for t in row.find_all('td')])
    
df = pd.DataFrame(data, columns = ['PostalCode','Borough','Neighborhood'])

df.head()
df.info()
df.shape()

# ignore cells where Borough is "not assigned"
df.drop(df[df['Borough']=="Not assigned"].index,axis=0, inplace=True)

df1 = df.reset_index()
df1.head()
df1.info()

df2 = df1.groupby('PostalCode').agg(lambda x: ','.join(x))
df2.head()
df2.info()

df3 = df2.reset_index()
df3['Borough']= 
    df3['Borough'].str.replace('nan|[{}\s]','').str.split(',').apply(set).str.join(',').str.strip(',').str.replace(",{2,}",",")
df3 = df2.reset_index()
df3.head()

df3.shape()



