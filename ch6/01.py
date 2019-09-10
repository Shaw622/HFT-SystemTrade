import numpy as np
import pandas_datareader.data as pdr
import statsmodels.api as sm

end = '2016/9/30'
n225 = pdr.DataReader('NIKKEI225', 'fred', '1949/5/16', end).dropna()
lnn225 = np.log(n225.dropna())
lnn225.columns = ['Close']

y = lnn225
x = range(len(lnn225))
x = sm.add_constant(x)
model = sm.OLS(y, x) # xは説明変数, y は被説明変数。ここでは x=経過時間, y=日経平均株価
results = model.fit()

print(results.summary())
