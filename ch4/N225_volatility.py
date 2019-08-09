import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as pdr

price = pdr.DataReader("^N225", 'yahoo',"1984/1/4", "2019/8/8")

volatility = pd.Series.rolling(np.log(price.Close).diff().dropna(), window=250).std()*np.sqrt(250)
volatility.plot()
plt.ylabel('STD 250days N225')
plt.show()
