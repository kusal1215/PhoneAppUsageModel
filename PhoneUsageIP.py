# -*- coding: utf-8 -*-
"""
Created on Fri May  7 23:53:01 2021

@author: kusal
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class PhoneUsageIP(BaseModel):
    Age: float 
    Gender: float 
    No_Of_Social_Media_Apps: float 
    Social_Media_App_Usage: float
    Gaming_App_usage: float
    Night_Time_Use: float
