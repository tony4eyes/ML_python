#import Numpy as np
import pandas as pd
import quandl as ql

df = ql.get('WIKI/GOOGL')
print(df) 

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT','PCT_change','Adj. Volume']]

dict = {1:'tom', 2:'jerry'}