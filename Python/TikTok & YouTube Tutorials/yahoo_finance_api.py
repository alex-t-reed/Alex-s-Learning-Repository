"""
Written by Alex Reed Aparicio

LinkedIn: https://linkedin.com/in/alextreed
YouTube: https://www.youtube.com/@alex_t_reed
LeetCode: https://leetcode.com/u/alex-t-reed/
Medium: https://medium.com/@ar.codes
GitHub: https://github.com/alex-t-reed
TikTok: https://tiktok.com/@ar.codes
"""

"""
https://ranaroussi.github.io/yfinance/index.html

Install the yfinance package using pip:
pip install yfinance
"""

# Importing the yfinance library to fetch financial data

# Get the ticker for Apple (AAPL)
import yfinance as yf
dat = yf.Ticker('AAPL')

# Print out all the information available for the AAPL stock
print(dat.info)

# Function to get the current stock price for a given stock ticker


def get_stock_price(stockTicker: str):
    if yf.Ticker(stockTicker).info:
        # Return the regular market price if available
        return yf.Ticker(stockTicker).info["regularMarketPrice"] or None
    else:
        # Return None if information is not available
        return None


# Print the stock price for NVIDIA (NVDA)
print(get_stock_price('NVDA'))

# Get detailed information for AAPL
AAPL_info = dat.info

# Extract the keys (attributes) from the AAPL stock information
AAPL_info_keys = AAPL_info.keys()

# Loop through each key and print its value for AAPL stock
for key in AAPL_info_keys:
    print(f'{key}: {AAPL_info[key]}')
