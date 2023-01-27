import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import joblib


dataset = pd.read_csv('data/salary.csv')
dropped_columns = ['fnlwgt', 'education-num', 'capital-gain', 'capital-loss']
df = dataset.drop(columns= dropped_columns)

X = df.drop('salary', axis=1)
y = df['salary']

model = joblib.load('rf_class_model.pickle')

preprocessor = ColumnTransformer([
    ('num_encoder', StandardScaler(), make_column_selector(dtype_include="int64")),
    ('cat_encoder', OneHotEncoder(handle_unknown='ignore', sparse=False), make_column_selector(dtype_include="object"))
    ],remainder='passthrough')


pipe = Pipeline([
    ('preprocessing', preprocessor),
    ('RandomForestClassifier', model),
])

pipe.fit(X,y)
#y_pred = pipe.predict(pd.DataFrame[[39,'State-gov','Bachelors', 'Never-married','Adm-clerical',	'Not-in-family','White', 'Male', 40, 'United-States']],columns=['age', 'workclass', 'education', 'marital-status', 'occupation','relationship', 'race', 'sex', 'hours-per-week', 'native-country'])
#print(X[5:6])
ex = pd.DataFrame([[39,'State-gov','Bachelors', 'Never-married',
                      'Adm-clerical',	'Not-in-family',
                      'White', 'Male', 40, 'United-States']],
                  columns=['age', 'workclass', 'education', 'marital-status', 'occupation','relationship', 'race', 'sex', 'hours-per-week', 'native-country'])
y_pred = pipe.predict(ex)
print(y_pred)
