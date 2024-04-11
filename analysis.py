import pandas as pd

data = pd.read_csv('Listings.csv', sep=',', encoding='latin1', index_col=False)



#Data Prep

data['host_since'] = pd.to_datetime(data['host_since'])
# print(data.info())

# sorted_data = data.loc[['city']== 'Paris',['host_since', 'neighbourhood', 'city', 'accommodates', 'price']]
print(data.head(15))