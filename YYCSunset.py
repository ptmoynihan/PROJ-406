# YYCSunset
# This script will output sunrise and sunset times in Calgary to a data frame
# Author: Paul Moynihan
# Date: 21 December 2021
# This script is based on a similar script found on geeksforgeeks.com
# Input might change depending on how this is called in the project

"""
Input: none
Output: Data Frame containing sunrise and sunset times
"""
# %% Module Import
import datetime as dt
import pandas as pd
from suntime import Sun
from geopy.geocoders import Nominatim

# Nominatim API
geolocator = Nominatim(user_agent='my-geo-application')

# %%Location
place = 'calgary'
location = geolocator.geocode(place)

# Latitude & Longitude
latitude = location.latitude
longitude = location.longitude
sun = Sun(latitude,longitude)

# Get local time from machine clock
time_zone = dt.date(2021, 12, 22)
sun_rise = sun.get_local_sunrise_time(time_zone)
sun_set = sun.get_local_sunset_time(time_zone)
# %%
