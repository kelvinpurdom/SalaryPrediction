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

preprocessor = ColumnTransformer([
    ('num_encoder', StandardScaler(), make_column_selector(dtype_include="int64")),
    ('cat_encoder', OneHotEncoder(handle_unknown='ignore', sparse=False), make_column_selector(dtype_include="object"))
    ],remainder='passthrough')


pipe = Pipeline([
    ('preprocessing', preprocessor),
    ('RandomForestClassifier', RandomForestClassifier(criterion='entropy', max_depth=20, max_features='auto',
                       n_estimators=56)),
])

pipe.fit(X,y)


joblib.dump(pipe, 'test_rf_model.sav')
