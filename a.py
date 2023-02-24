import matplotlib.pyplot as grafic
import numpy as np
import pandas as pd
import time

date=pd.read_csv('date.csv', index_col='Year')

x=list(date.columns)
L=len(x)
y=list(date.loc[2010][0:L])

grafic.bar(x, y, color='red', width=0.8)
grafic.xticks(np.arange(0, L, 1), rotation=90)

grafic.xlabel('Domenii de activitate')
grafic.ylabel('Milioane')
grafic.title('Număr femei angajate în anul 2010')
grafic.show()

grafic.pie(y, labels=x)
grafic.title('Număr femei angajate în anul 2010')
grafic.legend(fontsize='4', loc='lower left')
grafic.show()
