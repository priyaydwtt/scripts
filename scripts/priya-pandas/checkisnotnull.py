import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3,3),index=[1,4,5],columns=[1,2,3])
print(df)

df=df.reindex([1,2,3,4,5,6])

print(df)

print(df[2].notnull())

print(df.fillna(10))

print(df.fillna(method=pad))



