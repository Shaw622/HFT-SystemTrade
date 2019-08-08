import pandas_datareader.data as pdr

price = pdr.DataReader("^N225", 'yahoo',"1984/1/4", "2019/8/1")
price.head(1)
print(price.tail(1))
