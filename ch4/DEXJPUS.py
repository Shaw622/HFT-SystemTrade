import pandas as pd
import pandas_datareader.data as pdr
import matplotlib.pyplot as plt

start = "1949/5/16"
end = "2016/9/30"

price = pdr.DataReader("^N225", 'yahoo',"1984/1/4", end)
price.head(1)

fx = pdr.DataReader('DEXJPUS', "fred", start, end)
port = pd.concat([price.Close, fx], axis=1).dropna()
n = port.Close.pct_change().dropna()
f = port.DEXJPUS.pct_change().dropna()
f.rolling(window = 20).corr(n).plot(color="yellow")
plt.ylabel('correlation')
plt.show()
