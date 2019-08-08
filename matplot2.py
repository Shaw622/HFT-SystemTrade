import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import datetime as dt
 
def displayN225():
    yesterday = dt.datetime.today() - dt.timedelta(days=1)
    N225 = pdr.DataReader('NIKKEI225', 'fred', '1949/5/16', yesterday.strftime("%Y/%m/%d"))
    N225.plot(color='red')
    plt.ylabel('NIKKEI225')
    plt.xlabel('DATE')
    plt.show()
 
displayN225()
