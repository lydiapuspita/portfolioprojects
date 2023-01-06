#!/usr/bin/env python
# coding: utf-8

# ## Glassnode API | Python

# In[1]:


import json
import requests
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot


# insert your API key here
API_KEY = '2It9FiAZB1mHp7VcjmmI9XzjPp4'

"""
make API request to get all endpoints
"""
res = requests.get(
    'https://api.glassnode.com/v2/metrics/endpoints',
    params={'api_key': API_KEY}
)

# convert to pandas dataframe
endpointData = pd.read_json(res.text)

# review endpoint data
print(endpointData.columns)


# In[2]:


# view all endpoint URLs
print(endpointData.path)


# In[3]:


# view specific endpoint
print(endpointData.path[0])


# In[4]:


# view specific endpoint tier
print(endpointData.tier[0])


# In[5]:


# all endpoints for specific tier 
print(endpointData.path[endpointData.tier == 1])


# In[6]:


# all endpoints for specific tier AND lower
print(endpointData.path[endpointData.tier <= 2])


# In[7]:


# find index/row number of endpoint by path
endpointRow = endpointData[
                endpointData.path == '/v1/metrics/market/price_usd_ohlc']
print(endpointRow)


# In[8]:


# supported assets by endpoint // in a DataFrame
print(pd.DataFrame(endpointData.assets[endpointRow.index[0]]))


# In[9]:


# view data resolution, granularity
print(endpointData.resolutions[endpointRow.index[0]])


# ### APE Coin

# In[10]:


"""
make API request to get candlestick data
"""
res = requests.get(
    'https://api.glassnode.com/v1/metrics/market/price_usd_ohlc',
    params={'a': 'APE', 'api_key': API_KEY, 'i': '24h'}
)


# In[11]:


# convert to pandas dataframe
candleData = pd.read_json(res.text, convert_dates=['t'])


# In[12]:


pd.set_option('display.max_rows', None)


# In[13]:


# rename columns
candleData = candleData.rename(columns={'t': 'Date', 'o': 'Candles'})

candleData


# In[14]:


# set index to date
candleData = candleData.set_index('Date')

candleData


# In[15]:


# turn candle dictionaries into individual series
candleData = candleData.Candles.apply(pd.Series)


# In[16]:


# rename columns
candleData = candleData.rename(columns={'c': 'Close', 'h': 'High', 
                                        'l': 'Low', 'o': 'Open'})


# In[17]:


candleData


# In[18]:


# generate plotly figure
fig = go.Figure(data=[go.Candlestick(x=candleData.index,
                open=candleData['Open'],
                high=candleData['High'],
                low=candleData['Low'],
                close=candleData['Close'])])

# open figure in browser
plot(fig, auto_open=True)


# In[22]:


"""
make request to get total addresses // APE
"""
res = requests.get(
    'https://api.glassnode.com/v1/metrics/addresses/count',
    params={'a': 'APE', 'api_key': API_KEY}
)


# In[23]:


# convert to pandas dataframe
addressData = pd.read_json(res.text, convert_dates=['t'])


# In[24]:


# rename columns
addressData = addressData.rename(columns={'t': 'Date', 'v': 'numAddresses'})


# In[25]:


# set index to date
addressData = addressData.set_index('Date')


# In[26]:


addressData


# In[27]:


# plot address data
addressData.plot()


# In[28]:


"""
make a request to get % Circulating Supply // APE
"""

res2 = requests.get(
    'https://api.glassnode.com/v1/metrics/supply/current',
    params={'a': 'APE', 'api_key': API_KEY}
)


# In[29]:


# convert to pandas dataframe
supplyData = pd.read_json(res2.text, convert_dates=['t'])


# In[30]:


# rename columns
supplyData = supplyData.rename(columns={'t': 'Date', 'v': 'LongTermSupply'})


# In[31]:


supplyData.info()


# In[32]:


# set index to date
supplyData = supplyData.set_index('Date')


# In[33]:


# plot supply data
supplyData.plot()


# ### MANA (Decentraland)

# In[34]:


"""
make API request to get candlestick data
"""
res3 = requests.get(
    'https://api.glassnode.com/v1/metrics/market/price_usd_ohlc',
    params={'a': 'MANA', 'api_key': API_KEY, 'i': '24h'}
)


# In[35]:


# convert to pandas dataframe
candleData = pd.read_json(res3.text, convert_dates=['t'])


# In[36]:


# rename columns
candleData = candleData.rename(columns={'t': 'Date', 'o': 'Candles'})

candleData


# In[37]:


# set index to date
candleData = candleData.set_index('Date')

candleData


# In[38]:


# turn candle dictionaries into individual series
candleData = candleData.Candles.apply(pd.Series)


# In[39]:


# rename columns
candleData = candleData.rename(columns={'c': 'Close', 'h': 'High', 
                                        'l': 'Low', 'o': 'Open'})


# In[40]:


candleData


# In[41]:


# generate plotly figure
fig = go.Figure(data=[go.Candlestick(x=candleData.index,
                open=candleData['Open'],
                high=candleData['High'],
                low=candleData['Low'],
                close=candleData['Close'])])

# open figure in browser
plot(fig, auto_open=True)


# In[42]:


# make request to get total addresses // MANA
res4 = requests.get(
    'https://api.glassnode.com/v1/metrics/addresses/count',
    params={'a': 'MANA', 'api_key': API_KEY}
)


# In[43]:


# convert to pandas dataframe
addressData2 = pd.read_json(res4.text, convert_dates=['t'])


# In[44]:


# rename columns
addressData2 = addressData2.rename(columns={'t': 'Date', 'v': 'numAddresses'})


# In[45]:


# set index to date
addressData2 = addressData2.set_index('Date')


# In[46]:


addressData2


# In[47]:


# plot address data
addressData2.plot()


# In[51]:


"""
make a request to get % Circulating Supply // MANA
"""

res5 = requests.get(
    'https://api.glassnode.com/v1/metrics/supply/current',
    params={'a': 'MANA', 'api_key': API_KEY}
)


# In[52]:


# convert to pandas dataframe
supplyData = pd.read_json(res5.text, convert_dates=['t'])


# In[53]:


# rename columns
supplyData = supplyData.rename(columns={'t': 'Date', 'v': 'LongTermSupply'})


# In[54]:


# set index to date
supplyData = supplyData.set_index('Date')


# In[55]:


# plot address data
supplyData.plot()


# ### Pi Cycle Top Indicator - APE Coin

# In[62]:


"""
make a request to Pi Cycle Top Indicator
"""

res6 = requests.get(
    'https://api.glassnode.com/v1/metrics/indicators/pi_cycle_top',
    params={'a': 'APE', 'api_key': API_KEY}
)


# In[63]:


# convert to pandas dataframe
piCycleTop = pd.read_json(res6.text, convert_dates=['t'])


# In[64]:


# rename columns
piCycleTop = piCycleTop.rename(columns={'t': 'Date', 'o': 'movAvgData'})


# In[65]:


# set index to date
piCycleTop = piCycleTop.set_index('Date')


# In[66]:


# turn dictionaries into individual series
piCycleTop = piCycleTop.movAvgData.apply(pd.Series)


# In[67]:


# plot address data
piCycleTop.plot()


# ### Pi Cycle Top
# 
# The Pi Cycle Top was also created by Philip Swift, and works by comparing the momentum of two moving average indicators. It compares the 111 SMA (blue) and 2 * 350 SMA (purple) of Bitcoin’s Price. These two moving averages were selected as 350 / 111 = 3.153; An approximation of the Pi number.
# 
# 1. When the 111 SMA (blue) meets the 2 * 350 SMA (purple), it is an indication of an overheated market. The mid timeframe momentum reference crosses above the long timeframe momentum reference.
# 2. When the 111 SMA (blue) falls beneath the 2 * 350 SMA (purple), it is an indication of a deflating market that is cooling of after a period of overheating.

# ### Pi Cycle Top Indicator - MANA Coin

# In[68]:


"""
make a request to Pi Cycle Top Indicator
"""

res7 = requests.get(
    'https://api.glassnode.com/v1/metrics/indicators/pi_cycle_top',
    params={'a': 'MANA', 'api_key': API_KEY}
)


# In[69]:


# convert to pandas dataframe
piCycleTop_2 = pd.read_json(res7.text, convert_dates=['t'])


# In[70]:


# rename columns
piCycleTop_2 = piCycleTop_2.rename(columns={'t': 'Date', 'o': 'movAvgData'})


# In[71]:


# set index to date
piCycleTop_2 = piCycleTop_2.set_index('Date')


# In[72]:


# turn dictionaries into individual series
piCycleTop_2 = piCycleTop_2.movAvgData.apply(pd.Series)


# In[73]:


# plot address data
piCycleTop_2.plot()


# In[ ]:




