import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as pdr

price = pdr.DataReader("^N225", 'yahoo',"1984/1/4", "2019/8/8")

ma = pd.Series.rolling(price.Close, window=259).mean()
price.Close.plot(label = 'n225 Close', style = '--')
ma.plot(label = '250days ma')
plt.ylabel('n225 index')
plt.legend
plt.show()


# 移動平均 ma 以外に利用可能な斧の例
# Series.rolling().max()　移動最大値
# Series.rolling().min()　移動最小値
# Series.rolling().median()　移動中央値
# Series.rolling().std()　標準偏差
