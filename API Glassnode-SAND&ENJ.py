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


# ### SAND Coin

# In[10]:


"""
make API request to get candlestick data
"""
res = requests.get(
    'https://api.glassnode.com/v1/metrics/market/price_usd_ohlc',
    params={'a': 'SAND', 'api_key': API_KEY, 'i': '24h'}
)


# In[11]:


# convert to pandas dataframe
candleData = pd.read_json(res.text, convert_dates=['t'])


# In[12]:


# rename columns
candleData = candleData.rename(columns={'t': 'Date', 'o': 'Candles'})

candleData


# In[13]:


# set index to date
candleData = candleData.set_index('Date')

candleData


# In[14]:


# turn candle dictionaries into individual series
candleData = candleData.Candles.apply(pd.Series)


# In[15]:


# rename columns
candleData = candleData.rename(columns={'c': 'Close', 'h': 'High', 
                                        'l': 'Low', 'o': 'Open'})


# In[16]:


candleData


# In[17]:


# generate plotly figure
fig = go.Figure(data=[go.Candlestick(x=candleData.index,
                open=candleData['Open'],
                high=candleData['High'],
                low=candleData['Low'],
                close=candleData['Close'])])

# open figure in browser
plot(fig, auto_open=True)


# In[18]:


"""
make request to get total addresses // SAND
"""
res2 = requests.get(
    'https://api.glassnode.com/v1/metrics/addresses/count',
    params={'a': 'SAND', 'api_key': API_KEY}
)


# In[19]:


# convert to pandas dataframe
addressData = pd.read_json(res2.text, convert_dates=['t'])


# In[20]:


# rename columns
addressData = addressData.rename(columns={'t': 'Date', 'v': 'numAddresses'})


# In[21]:


# set index to date
addressData = addressData.set_index('Date')


# In[22]:


addressData


# In[23]:


# plot address data
addressData.plot()


# In[24]:


"""
make a request to get % Circulating Supply // SAND
"""

res3 = requests.get(
    'https://api.glassnode.com/v1/metrics/supply/current',
    params={'a': 'SAND', 'api_key': API_KEY}
)


# In[25]:


# convert to pandas dataframe
supplyData = pd.read_json(res3.text, convert_dates=['t'])


# In[26]:


# rename columns
supplyData = supplyData.rename(columns={'t': 'Date', 'v': 'LongTermSupply'})


# In[27]:


supplyData.info()


# In[28]:


# set index to date
supplyData = supplyData.set_index('Date')


# In[29]:


# plot supply data
supplyData.plot()


# ### ENJ (Enjin Coin)

# In[35]:


"""
make API request to get candlestick data
"""
res4 = requests.get(
    'https://api.glassnode.com/v1/metrics/market/price_usd_ohlc',
    params={'a': 'ENJ', 'api_key': API_KEY, 'i': '24h'}
)


# In[36]:


# convert to pandas dataframe
candleData2 = pd.read_json(res4.text, convert_dates=['t'])


# In[37]:


# rename columns
candleData2 = candleData2.rename(columns={'t': 'Date', 'o': 'Candles'})

candleData2


# In[38]:


# set index to date
candleData2 = candleData2.set_index('Date')

candleData2


# In[39]:


# turn candle dictionaries into individual series
candleData2 = candleData2.Candles.apply(pd.Series)


# In[40]:


# rename columns
candleData2 = candleData2.rename(columns={'c': 'Close', 'h': 'High', 
                                        'l': 'Low', 'o': 'Open'})


# In[41]:


candleData2


# In[42]:


# generate plotly figure
fig = go.Figure(data=[go.Candlestick(x=candleData2.index,
                open=candleData2['Open'],
                high=candleData2['High'],
                low=candleData2['Low'],
                close=candleData2['Close'])])

# open figure in browser
plot(fig, auto_open=True)


# In[43]:


# make request to get total addresses // MANA
res5 = requests.get(
    'https://api.glassnode.com/v1/metrics/addresses/count',
    params={'a': 'ENJ', 'api_key': API_KEY}
)


# In[44]:


# convert to pandas dataframe
addressData2 = pd.read_json(res5.text, convert_dates=['t'])


# In[45]:


# rename columns
addressData2 = addressData2.rename(columns={'t': 'Date', 'v': 'numAddresses'})


# In[46]:


# set index to date
addressData2 = addressData2.set_index('Date')


# In[47]:


addressData2


# In[48]:


# plot address data
addressData2.plot()


# In[49]:


"""
make a request to get % Circulating Supply // ENJ
"""

res6 = requests.get(
    'https://api.glassnode.com/v1/metrics/supply/current',
    params={'a': 'ENJ', 'api_key': API_KEY}
)


# In[50]:


# convert to pandas dataframe
supplyData2 = pd.read_json(res6.text, convert_dates=['t'])


# In[51]:


# rename columns
supplyData2 = supplyData2.rename(columns={'t': 'Date', 'v': 'LongTermSupply'})


# In[52]:


# set index to date
supplyData2 = supplyData2.set_index('Date')


# In[53]:


# plot address data
supplyData2.plot()


# ### Pi Cycle Top Indicator - SAND (The Sandbox)

# In[54]:


"""
make a request to Pi Cycle Top Indicator
"""

res7 = requests.get(
    'https://api.glassnode.com/v1/metrics/indicators/pi_cycle_top',
    params={'a': 'SAND', 'api_key': API_KEY}
)


# In[55]:


# convert to pandas dataframe
piCycleTop = pd.read_json(res7.text, convert_dates=['t'])


# In[56]:


# rename columns
piCycleTop = piCycleTop.rename(columns={'t': 'Date', 'o': 'movAvgData'})


# In[57]:


# set index to date
piCycleTop = piCycleTop.set_index('Date')


# In[58]:


# turn dictionaries into individual series
piCycleTop = piCycleTop.movAvgData.apply(pd.Series)


# In[59]:


# plot address data
piCycleTop.plot()


# ### Pi Cycle Top
# 
# The Pi Cycle Top was also created by Philip Swift, and works by comparing the momentum of two moving average indicators. It compares the 111 SMA (blue) and 2 * 350 SMA (purple) of Bitcoin’s Price. These two moving averages were selected as 350 / 111 = 3.153; An approximation of the Pi number.
# 
# 1. When the 111 SMA (blue) meets the 2 * 350 SMA (purple), it is an indication of an overheated market. The mid timeframe momentum reference crosses above the long timeframe momentum reference.
# 2. When the 111 SMA (blue) falls beneath the 2 * 350 SMA (purple), it is an indication of a deflating market that is cooling of after a period of overheating.

# ### Pi Cycle Top Indicator - Enjin Coin

# In[60]:


"""
make a request to Pi Cycle Top Indicator
"""

res8 = requests.get(
    'https://api.glassnode.com/v1/metrics/indicators/pi_cycle_top',
    params={'a': 'ENJ', 'api_key': API_KEY}
)


# In[61]:


# convert to pandas dataframe
piCycleTop_2 = pd.read_json(res8.text, convert_dates=['t'])


# In[62]:


# rename columns
piCycleTop_2 = piCycleTop_2.rename(columns={'t': 'Date', 'o': 'movAvgData'})


# In[63]:


# set index to date
piCycleTop_2 = piCycleTop_2.set_index('Date')


# In[64]:


# turn dictionaries into individual series
piCycleTop_2 = piCycleTop_2.movAvgData.apply(pd.Series)


# In[65]:


# plot address data
piCycleTop_2.plot()


# In[ ]:




