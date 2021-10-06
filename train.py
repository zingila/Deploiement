import pandas as pd
import numpy as np
import pickle

from nltk.corpus import stopwords
from nltk.tokenize import NLTKWordTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('DisneylandReviews.csv', encoding='cp1252')
df.head()

df.info()
df['Rating'].unique()

#Préparation des données
df = df.drop(['Review_ID', 'Year_Month', 'Reviewer_Location'], axis=1)

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    stop_words.update(["'ve", "", "'ll", "'s", ".", ",", "?", "!", "(", ")", "..", "'m", "n", "u"])
    tokenizer = NLTKWordTokenizer()
    
    text = text.lower()
    
    tokens = tokenizer.tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    
    return ' '.join(tokens)

df['Review_Text'] = df['Review_Text'].apply(preprocess_text)
df.head()
df['Review_Text'][1]

#Premier modele
#Le premier modèle consiste à considérer toutes les branches ensemble
df1 = df.drop(['Branch'], axis=1)
df1.head()

features = df['Review_Text']
target = df['Rating']

X_train, X_test, y_train, y_test = train_test_split(features, target)

count_vectorizer_unique = CountVectorizer(max_features=2000)

X_train_cv = count_vectorizer_unique.fit_transform(X_train)
X_test_cv = count_vectorizer_unique.transform(X_test)

model_unique = RandomForestClassifier(max_depth=3, n_estimators=100)
#model_unique = LogisticRegression()
#model_unique = DecisionTreeClassifier(max_depth=8)

model_unique.fit(X_train_cv, y_train)

model_unique.score(X_test_cv, y_test)
print("\n")
#Deuxieme modele
#Dans ce modele les branches sont séparées en 3
df['Branch'].unique()

count_vectorizers = {}
models = {}

for branch in df['Branch'].unique():
    count_vectorizer = CountVectorizer(max_features=2000)
#     model = LogisticRegression()
    model = RandomForestClassifier(n_estimators=20, max_depth=5)
    
    df_temp = df[df['Branch'] == branch]
    
    X_train, X_test, y_train, y_test = train_test_split(df_temp['Review_Text'], df_temp['Rating'])
    
    X_train_cv = count_vectorizer.fit_transform(X_train)
    X_test_cv = count_vectorizer.transform(X_test)
    
    model.fit(X_train_cv, y_train)
    print(branch, ':', model.score(X_test_cv, y_test))
    
    count_vectorizers[branch] = count_vectorizer
    models[branch] = model

with open("./api/data/model.pkl", "wb") as f:
    pickle.dump([model_unique,models], f)
