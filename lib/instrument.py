import scipy as sp
import numpy as np
import urllib2
import datetime 
import matplotlib.pyplot as plt
import matplotlib
import doctest

class stock(object):

    def get_web_data(self):
        """
        Go to Yahoo! Finance a grab the data
        """
                
        (begin_d,begin_m,begin_y) = self.begin_date.split('/')
        (end_d,end_m,end_y) = self.end_date.split('/')
        b_day = "&a={}&b={}&c={}".format(begin_d,begin_m,begin_y)
        e_day = "&d={}&e={}&f={}".format(end_d,end_m,end_y)
        ticker = "http://ichart.finance.yahoo.com/table.csv?s={}{}&g=d{}&ignore=.csv".format(self.name,b_day,e_day)
        f = urllib2.urlopen(ticker)
        stocktitles = f.readline().split(',')
        stock_data = f.read(f).replace('\n',',').split(',') 
        dates = stock_data[::len(stocktitles)]
        dates.pop()
        close_price = stock_data[4::len(stocktitles)]
        f.close()
        return dates, close_price
    
    def plot_date_price(self, dates, close_price):
        new_dates = []
        for i in dates:
            new_dates.append(matplotlib.dates.date2num(datetime.datetime.strptime(i, '%Y-%m-%d')))
                                                
        plt.plot_date(new_dates,close_price,'bo-', label="stock Prices")
        plt.legend(loc = 'upper left')
        #plt.plot()
        plt.savefig(self.name, dpi=150, format='pdf')
        plt.show()
        
    def __init__(self,name='MSFT',begin_date='1/1/2013',end_date='10/1/2013'):
        self.name = name
        self.begin_date = begin_date
        self.end_date = end_date
        
    