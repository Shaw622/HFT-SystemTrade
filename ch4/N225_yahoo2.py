import pandas_datareader.data as pdr
import matplotlib.pyplot as plt

price = pdr.DataReader("^N225", 'yahoo',"1984/1/4", "2019/8/8")
price1 = price.loc["1990/1/1":]
price1.Close.plot(color="green")
plt.show()

#price2 = price.loc["2015", 0:2]
#price2.tail(1)
#plt.ylabel('N225 index')
