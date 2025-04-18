# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 09:34:38 2023

@author: CLi
"""


import pandas as pd
import numpy as np
import matplotlib as mpl
#import matplotlib.pyplot as plt
#import seaborn as sns
#import joypy
mpl.rcParams["figure.dpi"] = 300



#=============================================================================
#=========== CALCULATING THE AIR QUALITY INDEX ===============================
#=============================================================================


#============ creating columns for computing the air quality index ==========================

#met_aq_data[['SO2','NOx','NH3','CO','O3']] = np.nan          #creating other pollutants columns

#==========================sub-index calculation of AQI======================================

# PM2.5 sub-index
def calc_PM25_sub_indx(x):
    if x <= 30:
        return x * 50 / 30
    elif x <= 60:
        return 50 + (x - 30) * 50 / 30
    elif x <= 90:
        return 100 + (x - 60) * 100 / 30
    elif x <= 120:
        return 200 + (x - 90) * 100 / 30
    elif x <= 250:
        return 300 + (x - 120) * 100 / 130
    elif x > 250:
        return 400 + (x - 250) * 100 / 130
    else:
        return 0

#met_aq_data["PM2.5_sub_indx"] = met_aq_data["PM2.5_CF1_ug/m3"].apply(lambda x: calc_PM25_sub_indx(x))


# PM10.0 sub-index
def calc_PM10_sub_indx(x):
    if x <= 50:
        return x
    elif x <= 100:
        return x
    elif x <= 250:
        return 100 + (x - 100) * 100 / 150
    elif x <= 350:
        return 200 + (x - 250)
    elif x <= 430:
        return 300 + (x - 350) * 100 / 80
    elif x > 430:
        return 400 + (x - 430) * 100 / 80
    else:
        return 0

#met_aq_data["PM10_sub_indx"] = met_aq_data["PM10_CF1_ug/m3"].apply(lambda x: calc_PM10_sub_indx(x))


# SO2 sub-index
def calc_SO2_sub_indx(x):
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 380:
        return 100 + (x - 80) * 100 / 300
    elif x <= 800:
        return 200 + (x - 380) * 100 / 420
    elif x <= 1600:
        return 300 + (x - 800) * 100 / 800
    elif x > 1600:
        return 400 + (x - 1600) * 100 / 800
    else:
        return 0

#met_aq_data["SO2_sub_indx"] = met_aq_data["SO2"].apply(lambda x: calc_SO2_sub_indx(x))


# NOx sub-index
def calc_NOx_sub_indx(x):
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 180:
        return 100 + (x - 80) * 100 / 100
    elif x <= 280:
        return 200 + (x - 180) * 100 / 100
    elif x <= 400:
        return 300 + (x - 280) * 100 / 120
    elif x > 400:
        return 400 + (x - 400) * 100 / 120
    else:
        return 0

#met_aq_data["NOx_sub_indx"] = met_aq_data["NOx"].apply(lambda x: calc_NOx_sub_indx(x))


#NH3 sub-index
def calc_NH3_sub_indx(x):
    if x <= 200:
        return x * 50 / 200
    elif x <= 400:
        return 50 + (x - 200) * 50 / 200
    elif x <= 800:
        return 100 + (x - 400) * 100 / 400
    elif x <= 1200:
        return 200 + (x - 800) * 100 / 400
    elif x <= 1800:
        return 300 + (x - 1200) * 100 / 600
    elif x > 1800:
        return 400 + (x - 1800) * 100 / 600
    else:
        return 0

#met_aq_data["NH3_sub_indx"] = met_aq_data["NH3"].apply(lambda x: calc_NH3_sub_indx(x))


## CO Sub-Index calculation
def calc_CO_sub_indx(x):
    if x <= 1:
        return x * 50 / 1
    elif x <= 2:
        return 50 + (x - 1) * 50 / 1
    elif x <= 10:
        return 100 + (x - 2) * 100 / 8
    elif x <= 17:
        return 200 + (x - 10) * 100 / 7
    elif x <= 34:
        return 300 + (x - 17) * 100 / 17
    elif x > 34:
        return 400 + (x - 34) * 100 / 17
    else:
        return 0

#met_aq_data["CO_sub_indx"] = met_aq_data["CO"].apply(lambda x: calc_CO_sub_indx(x))


## O3 Sub-Index calculation
def calc_O3_sub_indx(x):
    if x <= 50:
        return x * 50 / 50
    elif x <= 100:
        return 50 + (x - 50) * 50 / 50
    elif x <= 168:
        return 100 + (x - 100) * 100 / 68
    elif x <= 208:
        return 200 + (x - 168) * 100 / 40
    elif x <= 748:
        return 300 + (x - 208) * 100 / 539
    elif x > 748:
        return 400 + (x - 400) * 100 / 539
    else:
        return 0

#met_aq_data["O3_sub_indx"] = met_aq_data["O3"].apply(lambda x: calc_O3_sub_indx(x))


def sub_index_calculation(aq_data):
    aq_data["PM2.5_sub_indx"] = aq_data["pm25"].apply(lambda x: calc_PM25_sub_indx(x))
    aq_data["PM10_sub_indx"] = aq_data["pm10_0_atm"].apply(lambda x: calc_PM10_sub_indx(x))
    aq_data["SO2_sub_indx"] = aq_data["SO2"].apply(lambda x: calc_SO2_sub_indx(x))
    aq_data["NOx_sub_indx"] = aq_data["NOx"].apply(lambda x: calc_NOx_sub_indx(x))
    aq_data["NH3_sub_indx"] = aq_data["NH3"].apply(lambda x: calc_NH3_sub_indx(x))
    aq_data["CO_sub_indx"] = aq_data["CO"].apply(lambda x: calc_CO_sub_indx(x))
    aq_data["O3_sub_indx"] = aq_data["O3"].apply(lambda x: calc_O3_sub_indx(x))
    return aq_data


def apply_aq_checks(aq_data):
    aq_data['Checks'] = (aq_data["PM2.5_sub_indx"] > 0).astype(int) + \
    (aq_data["PM10_sub_indx"] > 0).astype(int) + \
    (aq_data["SO2_sub_indx"] > 0).astype(int) + \
    (aq_data["NOx_sub_indx"] > 0).astype(int) + \
    (aq_data["NH3_sub_indx"] > 0).astype(int) + \
    (aq_data["CO_sub_indx"] > 0).astype(int) + \
    (aq_data["O3_sub_indx"] > 0).astype(int)
    return aq_data



def apply_aqi_calculation(aq_data):
    aq_data['calculated_AQI'] = round(aq_data[["PM2.5_sub_indx", "PM10_sub_indx",
                   "SO2_sub_indx", "NOx_sub_indx",
                   "NH3_sub_indx", "CO_sub_indx", "O3_sub_indx"]].max(axis = 1))
    aq_data.loc[aq_data["PM2.5_sub_indx"] + aq_data["PM10_sub_indx"] <= 0, "calculated_AQI"] = np.NaN
    aq_data.loc[aq_data.Checks < 2, "calculated_AQI"] = np.NaN  #<3 indicates atleast 3 inputs else returns NaN (can be changed to suit choice)
    return aq_data
    
#changing < = 0 to < 0,calculated_AQI 



## AQI bucketing
def categorize_AQI(x):
    if x <= 50:
        return "Good"
    elif x <= 100:
        return "Moderate"
    elif x <= 150:
        return "Unhealthy for Sensitive Groups"
    elif x <= 200:
        return "Unhealthy"
    elif x <= 300:
        return "Very Unhealthy"
    elif x > 300:
        return "Hazardous"
    else:
        return np.NaN

