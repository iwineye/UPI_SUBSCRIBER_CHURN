import pandas as pd
import numpy as np 
import pickle

df=pd.read_csv('upi_data.csv')

df['AVG_MONTHLY_TRANSACTIONS']=df['AVG_MONTHLY_TRANSACTIONS'].astype(str).astype(int)
df['SUBSCRIPTION_STATUS']=df['SUBSCRIPTION_STATUS'].astype(str).astype(int)
df['DAILY_AVG_APP_DURATION']=df['DAILY_AVG_APP_DURATION'].astype(str).astype(int)

dummy_data=pd.get_dummies(df,drop_first=True)

dummy_data=dummy_data.set_index("CUSTOMER_ID")

X=dummy_data.iloc[:,[0,1,3,4,5,6]]

y=df.iloc[:,6:7]

#split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=10)

from sklearn.tree import DecisionTreeClassifier
treeclassifier=DecisionTreeClassifier()

treemodel=DecisionTreeClassifier()

treeclassifier.fit(X_train,y_train)

y_pred=treeclassifier.predict(X_test)

treeclassifier=DecisionTreeClassifier(max_depth=5)

DT=treeclassifier.fit(X_train,y_train)

pickle.dump(DT,open('prediction_model.pkl','wb'))