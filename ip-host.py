

import pandas as pd
import numpy as np
import re
import socket

file1=pd.read_csv('aug5-wl.csv', delim_whitespace=True)


file2=(file1[['Destination']]).drop_duplicates()

file2=file2.astype(str)

file2['Results']=file2.fillna


file2=file2['Destination'].str.extract(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

file2=file2.dropna()


#df.columns = df.columns.str.strip()

file2=file2.str.rstrip()



f2=lambda x:socket.getfqdn(str(x))



file2['Results']=file2.apply(f2)