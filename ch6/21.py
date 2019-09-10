import numpy as np
import pandas_datareader.data as pdr
import statsmodels.api as sm

end = '2016/9/30'
n225 = pdr.DataReader('NIKKEI225', 'fred', '1949/5/16', end).dropna()
lnn225 = np.log(n225.dropna())
lnn225.columns = ['Close']

y = lnn225.ix['1954/12/1':'1971/12/31'].dropna()
x = range(len(y))
x = sm.add_constant(x)
model = sm.OLS(y, x)
results = model.fit()

print(results.summary())
