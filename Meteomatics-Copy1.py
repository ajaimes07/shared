#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Retrieves weather data from the last 2 days from meteomatics


# In[26]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding:=utf-8
#Meteomatics
import argparse
import datetime as dt
import sys
import meteomatics.api as api
import pandas as pd
from pathlib import Path


# In[27]:


###Credentials:
username = 'engie_jaimes' 
password = 't8MjJ7sHe0WyG'


# In[49]:


#import pymongo
#import sys
#import json
#from flask_pymongo import PyMongo


# In[52]:


#MONGODB_URI = "mongodb://Aline1:aline1@ds061355.mlab.com:61355/heroku_njkl5bj0"
#mongo= PyMongo
#db = client.get_database("time_record")
#time_record = db.time_record


# In[53]:


#Datetime. Get the last day
now = dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
startdate_ts = now
enddate_ts = startdate_ts + dt.timedelta(days=1)
#interval_ts = dt.timedelta(hours=1)
interval_ts = dt.timedelta(hours=24)


# In[54]:


#From where 
input_coordinates_frame = pd.read_csv('locations.csv')
coordinates_ts = [(lat, lon) for lat, lon in input_coordinates_frame.loc[:, ['lat', 'lon']].values]


# In[55]:


# What parameters
parameters_station_ts = ['absolute_humidity_2m:gm3', 'clear_sky_rad:W','dew_point_2m:C', 'diffuse_rad:W',
                         'diffuse_rad_1h:Ws', 'direct_rad:W', 'direct_rad_1h:Ws',
                         'dust_0p03um_0p55um:ugm3', 'dust_0p55um_0p9um:ugm3', 'dust_0p9um_20um:ugm3',
                         'effective_cloud_cover:p', 'fresh_snow_1h:cm', 'frost_depth:cm',
                         'global_rad:W', 'global_rad_1h:Ws', 'high_cloud_cover:p',
                         'is_fog_1h:idx', 'is_rain_1h:idx', 'is_sleet_1h:idx', 'is_snow_1h:idx',
                         'low_cloud_cover:p', 'medium_cloud_cover:p', 'neff:p', 'pm1:ugm3',
                         'pm10:ugm3', 'pm2p5:ugm3', 'precip_1h:mm', 'prob_precip_1h:p',
                         'relative_humidity_2m:p', 'sfc_pressure_mean_1h:hPa', 'snowdepth:cm',
                         'snow_melt_1h:mm', 'sunrise:sql', 'sunset:sql', 'sunshine_duration_1h:min',
                         't_0m:C', 't_2m:C', 't_max_0m_1h:C', 't_mean_0m_1h:C', 't_min_0m_1h:C',
                         'total_cloud_cover:p', 'wet_bulb_t_2m:C', 'wind_dir_10m:d',
                         'wind_dir_mean_10m_1h:d', 'wind_gusts_10m:ms', 'wind_speed_10m:ms',
                         'wind_speed_mean_10m_1h:ms', 'wind_speed_u_10m:ms', 'wind_speed_v_10m:ms']


# In[56]:


print("time series:")
try:
    df_ts = api.query_time_series(coordinates_ts, startdate_ts, enddate_ts, interval_ts,
                                  parameters_station_ts, username, password)
    print (df_ts.head())
except Exception as e:
    print("Failed, the exception is {}".format(e))


# In[57]:


df_ts.head()


# In[58]:


df_ts.to_csv('Meteomatics.csv',index=False)


# In[37]:





# In[ ]:




