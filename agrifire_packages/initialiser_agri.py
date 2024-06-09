#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 08:55:29 2023

@author: moorthymnair
"""

from datetime import datetime as dt

def header():
    print("-*-" * 28)
    print()
    print("Automated Agriculture Fire Detector".center(70))
    print("Fetches agriculture fire points from satellite images".center(70))
    print()
    print(f"Date & Time of Run:     {dt.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("Contact:                morthymnair@yahoo.in")
    print("Acknolwedgement:        NASA-FIRMS (https://firms.modaps.eosdis.nasa.gov/)")                   
    print()
    print("-*-" * 28)
    print()
    print("Fetching details........")