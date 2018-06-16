import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(100,4), columns=['one','two','three','four'])
print(df)

df.to_excel('C:/python source/Section4/result_s2.xlsx',index=None)
