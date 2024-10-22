# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:20:10 2024

@author: joahb
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime


def convert_to_datetime(row):
    year, month, day, hour, minute, second = row[:6]
    return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

data = np.loadtxt('fismflux20020824.dat', skiprows=1)


date_time = data[:, :6]  
euv_spectrum = data[:, 6:]  


times = [convert_to_datetime(row) for row in date_time]

euv_bin_56 = euv_spectrum[:, 55]


plt.figure(figsize=(12, 6))
plt.plot(times, euv_bin_56, label='56th bin of EUV spectrum')


plt.xlabel('Time', size=14)
plt.ylabel('EUV Irradiance (W/m^2/nm)', size=14)
plt.title('56th Bin of EUV Spectrum Vs Time', size=16)
plt.grid(True) 
plt.legend()

plt.show()