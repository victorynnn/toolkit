""" yf_example3.py
Example of a function to download stock price data for Qantas for a given year and save the information in a CSV file.
"""
import os
import toolkit_config as cfg
import yf_example2
import yfinance as yf
def qan_prc_to_csv(year):#Download Qantas stock prices for a given year into a CSV file
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    tics = 'QAN.AX'
    paths = fr"qan_prc_{year}.csv"
    pths = os.path.join(cfg.DATADIR, paths)
    yf_example2.yf_prc_to_csv(tic=tics,pth = pths, start=start_date, end=end_date)
if __name__ == "__main__":
    qan_prc_to_csv(2020)



