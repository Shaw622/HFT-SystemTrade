import pandas_datareader.data as pdr
import matplotlib.pyplot as plt

start = "1949/5/16"
end = "2016/9/30"
N225 = pdr.DataReader("NIKKEI225", 'fred',start,end)

N225.plot(color='darkblue')
plt.ylabel('N225 index')
