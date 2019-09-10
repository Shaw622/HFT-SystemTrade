import numpy as np
import pandas_datareader.data as pdr

states = ['recover', 'growth', 'stable', 'bubble', 'reform', 'now']
dates = ['1949/5/16', '1954/12/1', '1972/1/1', '1986/12/1', '1993/11/1', '2016/9/30']

end = '2016/9/30'
n225 = pdr.DataReader('NIKKEI225', 'fred', '1949/5/16', end).NIKKEI225

for i in range(len(dates)-1):
    vol = np.log(n225[dates[i]:dates[i+1]]).diff().std()
    print(states[i], ': %2.4f ;' %vol)

