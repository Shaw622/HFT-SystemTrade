import numpy as np
import pandas_datareader.data as pdr
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

end = '2016/9/30'
n225 = pdr.DataReader('NIKKEI225', 'fred', '1949/5/16', end).dropna()
lnn225 = np.log(n225.dropna())
lnn225.columns = ['Close']

y = lnn225
x = range(len(lnn225))
x = sm.add_constant(x)
model = sm.OLS(y, x)
results = model.fit()

plt.plot(y, label='Close', color='darkgray')
results.fittedvalues.plot(label='prediction', style='--') # t時の予測値or期待値
plt.ylabel('log(n225 index)')
plt.legend(loc='upper left')
plt.show()
