import pandas_datareader.data as pdr
import matplotlib.pyplot as plt

price = pdr.DataReader("^N225", 'yahoo',"1984/1/4", "2019/8/8")

price.resample('A').Close().plot(color='magenta')
plt.ylabel('N225 Index')
plt.show()
