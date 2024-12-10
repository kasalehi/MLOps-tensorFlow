
#lets bring the libraries and  models 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import sklearn 


# loading data
df=pd.read_csv("/workspaces/MLOps-tensorFlow/WA_Fn-UseC_-Telco-Customer-Churn.csv")

string=list(df.dtypes[df.dtypes=='object'].index)
string


for col in string:
    df[col]=df[col].str.replace(' ','_').str.lower()





df.columns=df.columns.str.replace(' ','_').str.lower()


num=list(df.dtypes[df.dtypes!='object'].index)
num

df.totalcharges=pd.to_numeric(df.totalcharges,errors='coerce')

df.totalcharge=df['totalcharges'].fillna(0)


from sklearn.model_selection import train_test_split

df_fulltrain,df_test=train_test_split(df,test_size=.2,random_state=42,shuffle=True)

df_train,df_val=train_test_split(df_fulltrain,test_size=.25,random_state=42)


df_train=df_train.reset_index(drop=True)
df_test=df_test.reset_index(drop=True)
df_val=df_val.reset_index(drop=True)

y_train=df_train['churn']
y_val=df_val['churn']
y_test=df_test['churn']



del df_train['churn'] 
del df_val['churn'] 
del df_test['churn'] 


cat=['gender', 'seniorcitizen', 'partner', 'dependents',
        'phoneservice', 'multiplelines', 'internetservice',
       'onlinesecurity', 'onlinebackup', 'deviceprotection', 'techsupport',
       'streamingtv', 'streamingmovies', 'contract', 'paperlessbilling',
       'paymentmethod']


num=['seniorcitizen', 'tenure', 'monthlycharges']

from sklearn.feature_extraction import DictVectorizer

dv=DictVectorizer(sparse=False)

train_dict=df_train[cat+num].to_dict(orient='records')

x_train=dv.fit_transform(train_dict)



val_dict=df_val[cat+num].to_dict(orient='records')


x_val=dv.transform(val_dict)

#lets call the model 
from sklearn.linear_model import LogisticRegression


model=LogisticRegression(random_state=42)

model.fit(x_train,y_train)

y_pred=model.predict(x_val)

#lets look at some metrics 
from sklearn.metrics import accuracy_score
    

print(f"the accuracy secor is :{accuracy_score(y_val,y_pred)}")




