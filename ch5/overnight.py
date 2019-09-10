import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as pdr

plt.figure(figsize = (8, 4))
analysis = pdr.DataReader("^N225", 'yahoo',"1986/9/3", '2019/7/30')
analysis['intraday'] = 0
analysis['overnight'] = 0
c0 = analysis.Close.iloc[0]

for i in range (1, len(analysis)):
    o = analysis.iloc[i, 0]
    c = analysis.iloc[i, 3]
    analysis.iloc[i, 6] = c - o
    analysis.iloc[i, 7] = o - c0
    c0 = c

analysis.Close.plot(label='Close', linewidth=1)
analysis.intraday.cumsum().plot(label='intraday', linestyle = ':')
analysis.overnight.cumsum().plot(label='overnight', linestyle = '--', linewidth=1)

plt.legend()
plt.ylabel('PL or N225 index')
plt.legend(loc='lower left')
plt.show()
