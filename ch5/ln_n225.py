import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as pdr

end = '2016/9/30'
n225 = pdr.DataReader('NIKKEI225', 'fred', '1949/5/16', end).NIKKEI225
struct_break = [('1949/5/16', 'recv'), ('1954/12/1', 'growth'), ('1972/1/1', 'stable'), ('1986/12/1', 'bubble'), ('1993/11/1', 'reform')]

fig = plt.figure()
g = fig.add_subplot(1,1,1)
ln_n225 = np.log(n225)
ln_n225.plot(ax=g, style='y-', linewidth=0.5)

for date, label in struct_break:
    g.annotate(label, xy = (date, n225.asof(date)),
               xytext = (date, ln_n225.asof(date)-0.75),
               horizontalalignment = 'left', verticalalignment = 'top')
    g.set_xlim(['1947/1/1', '2019/4/25'])

plt.ylabel('log(N225 Index)')
plt.title("Log Nikkei 225 and structural change")
plt.show()
