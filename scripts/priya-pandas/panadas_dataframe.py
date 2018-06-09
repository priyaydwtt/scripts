import pandas as pd
dictionary1 = {'Name':['Anu','Banu','Munu','Sonu'],'Age':[34,35,27,42],'city':['mumbai','chennai','coimbatore','tveli']}
dataframe1 = pd.DataFrame(dictionary1,index=['rank1','rank2','rank3','rank4'])
print(dataframe1)