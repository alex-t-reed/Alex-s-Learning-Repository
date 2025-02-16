# LinkedIn (connect with me): https://linkedin.com/in/alex-t-reed
# TikTok (follow): https://tiktok.com/@ar.codes
# GitHub (for source code): https://github.com/alex-t-reed 
# YouTube (subscribe): https://www.youtube.com/@alex_t_reed

"""
https://ranaroussi.github.io/yfinance/index.html

pip install yfinance
"""

import yfinance as yf

dat = yf.Ticker('AAPL')

# print(dat.info)

# def get_stock_price(stockTicker: str):
#     if yf.Ticker(stockTicker).info:
#         return  yf.Ticker(stockTicker).info["regularMarketPrice"] or None
#     else:
#         return None
    
# print(get_stock_price('NVDA'))

AAPL_info = dat.info

AAPL_info_keys = AAPL_info.keys()

for key in AAPL_info_keys:
    print(f'{key}: {AAPL_info[key]}')