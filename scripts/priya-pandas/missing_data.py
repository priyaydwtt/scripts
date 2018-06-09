import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'c', 'e', 'f'], columns=['one', 'two', 'three'])

df = df.reindex(['a','b','c','d','e','f','g','h'])

print(df)

print(df['one'].isnull())


"""

df = pd.DataFrame(np.random.randn(5, 3), index=[1,2,3,4,5,6,7],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df)

"""