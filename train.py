from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics, preprocessing, model_selection, svm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

df = pd.read_csv('churn.csv')
df.info()

df.info()

#Préparation des données
df.TotalCharges = df.TotalCharges.replace([' '], [0])
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])
df.gender = df.gender.replace(['Male', 'Female'], [1, 0])
df = df.replace(['No internet service','No phone service'], ['No','No'])
df[['Partner','Dependents','PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling', 'Churn']] = df[['Partner','Dependents','PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling', 'Churn']].replace(['Yes','No'], [0,1])
df = df.join(pd.get_dummies(df['Contract'], prefix='Contract'))
df = df.join(pd.get_dummies(df['PaymentMethod'], prefix='PaymentMethod'))
df = df.join(pd.get_dummies(df['InternetService'], prefix='InternetService'))

df = df.drop(['customerID','tenure', 'Contract', 'PaymentMethod', 'InternetService'], axis=1)

data = df.drop('Churn', axis = 1)
target = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(data,target,test_size=0.2) # 80% training and 20% test

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

y_pred = dt.predict(X_test)


#Enregistrement du modele decisiontreeclassifier
with open("./api/data/model.pkl", "wb") as f:
    pickle.dump([y_test,y_pred], f)
