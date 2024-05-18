import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("HistDataAppl.csv")


df.plot(x='Date', y='Volume', kind='line', rot=30, legend=None, 
        title='histori data Apple (volume)', ylabel='Volume', figsize=(12,5));


plt.show() 