import pandas_datareader.data as pdr

start = "1949/5/16"
end = "2016/9/30"
N225 = pdr.DataReader("NIKKEI225", 'fred',start,end)

print(N225.head(1))
print(N225.tail(1))
