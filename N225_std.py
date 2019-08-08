import numpy as np
import pandas_datareader.data as pdr

price = pdr.DataReader("^N225", 'yahoo',"1984/1/4", "2019/8/8")

dp = np.log(price.Close).diff() # 終値の対数の差を計算
vol = dp.std()*np.sqrt(250) # 終値の対数の差の標準偏差を取理、250のルートをか取ることで年率換算
print(vol, len(price))
