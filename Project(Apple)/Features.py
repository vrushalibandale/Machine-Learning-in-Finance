#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 23:30:58 2019

@author: nirmaljay
"""

import pandas as pd

aapl = pd.read_excel('AAPL.xlsx')

#MOM

Mom = pd.Series([])
for i in range(0,len(aapl['Close '])):
    price_today = aapl.iat[i,1]
    price_5Days = aapl.iat[i-5,1]
    if(i < 5):
        mom[i] = 0
    else:
        momentum =(price_today/price_5Days)*100
        Mom[i] = momentum
aapl['Momentum'] = Mom.to_frame()


#RSI
def rsi_fn(n):
    temp = aapl['Close '].diff()
    temp = temp[1:]
    up, down = temp.copy(), temp.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up = up.rolling(n).mean()
    roll_down = down.rolling(n).mean().abs()
    rs = roll_up / roll_down
    rsi= 100.0 - (100.0 / (1.0 + rs))
    return rsi


aapl['RSI'] = rsi_fn(2)

aapl = aapl.set_index(['Date'])
aapl_feature = aapl.iloc[:,6:]
aapl_feature = aapl_feature.dropna()
