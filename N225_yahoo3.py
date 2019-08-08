import pandas_datareader.data as pdr
import matplotlib.pyplot as plt

price = pdr.DataReader("^N225", 'yahoo',"1984/1/4", "2019/8/8")

#月の初めの値を選択
print(price.resample('M').first().tail())

#月の終わりの値を選択
print(price.resample('M').last().tail())

# 1日分オフセット
print(price.resample('M', loffset='1d').last().tail())


price.resample('A').Close().plot(color='magenta')
plt.ylabel('N225 Index')
plt.show()
