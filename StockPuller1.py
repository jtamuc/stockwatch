# Stock price puller and plotter
# Adam Hetzler and John Creasy 10/13/13
#
#

import scipy as sp
import numpy as np
import urllib2
import datetime 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib

# use raw input to ask for and take in the 4 digit stock ticker as a string
stocks = raw_input('Please type your 4 digit stock to look up ex. MSFT: ')
for stock in stocks:
    begin_day = "&a=1&b=1&c=2013"
    end_day = "&d=5&e=23&f=2013"
    ticker = "http://ichart.finance.yahoo.com/table.csv?s={}{}&g=d{}&ignore=.csv".format(stock,begin_day,end_day)
    f = urllib2.urlopen(ticker)
    stocktitles = f.readline().split(',')
    stock_data = f.read(f).replace('\n',',').split(',') 
    dates = stock_data[::len(stocktitles)]
    dates.pop()
    close_price = stock_data[4::len(stocktitles)]
    f.close()
    new_dates = []
    for i in dates:
        new_dates.append(matplotlib.dates.date2num(datetime.datetime.strptime(i, '%Y-%m-%d')))
    
    fig, ax = plt.subplots(1)                                            
    ax.plot_date(new_dates,close_price,'bo-', label=stocks)
    plt.legend(loc = 'upper left')
    #plt.plot()
    fig.autofmt_xdate()
    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    plt.savefig(stocks, dpi=150, format='pdf')
    
    plt.show()
    print stocktitles,'\n'
    print close_price,'\n'
