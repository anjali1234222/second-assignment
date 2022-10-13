from operator import le
import pandas as pd
info ={'Gender':['Male','Female','Female','Male','Female','Female'],
       'Position':['Head','Asst.prof','Associate prof','Asst.prof','Associate prof','Head']}
df=pd.DataFrame(info)
print(df)
from sklearn.prepocessing import LabelEncoder
le = LabelEncoder()
gender_encoded =le.fit_transform(df['Gender'])
encoded_position =le.fit_transform(df['Position'])
df['Encoded_Gender']=gender_encoded
df['Encoded_Position']=encoded_position
print(df)