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

y = lnn225.loc['1990/1/1':'1992/8/31'].dropna()
x = range(len(y))
x = sm.add_constant(x)
model = sm.OLS(y, x)
results = model.fit()

results.resid.hist(bins=10, color='seagreen')
plt.xlabel('residual')
plt.ylabel('frequency')
plt.show()
