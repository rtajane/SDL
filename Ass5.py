# -*- coding: utf-8 -*-
import pandas as pd
ds=pd.read_csv('movie_metadata.csv',encoding="ISO-8859-1")
ds.head()
ds.shape
ds.info()
ds.imdb_score.describe()
ds['movie_title']   
ds['duration'][:10]  
ds[['budget','gross']]
ds[ds['duration'] > 120] 


ds.country=ds.country.fillna('') 
ds.duration=ds.duration.fillna(ds.duration.mean())
ds.dropna()  
ds.dropna(how='all') 
ds.dropna(thresh=5) 
ds.dropna(subset=['title_year'])  



ds.dropna(axis=1, how='all') 
ds.dropna(axis=1, how='any') 

ds=pd.read_csv('movie_metadata.csv',dtype={'duration':int})
ds=pd.read_csv('movie_metadata.csv',dtype={'title_year':str})

ds1=ds.rename(columns={'movie_title':'Movie'})

ds['director_name'].str.upper()
ds['movie_title'].str.strip()

d2=ds.to_csv('clean.csv',encoding='utf-8')


