import pandas as pd
ds=pd.read_csv('Game_medal.csv',encoding='ISO-8859-1')
ds.head()
ds.tail()
ds.describe()
ds.shape
ds.info()
ds.shift
ds.plot()
ds.NOC
import matplotlib.pyplot as plt
plt.xlabel('Records')
plt.ylabel('Year of event')
plt.title('Game_Graph')
plt.plot(ds.Edition,label='Year of event',color='blue',linewidth=2.5)