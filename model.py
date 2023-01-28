import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import accuracy_score

# random seed
seed = 42

dataset = pd.read_csv('data/salary.csv')
dataset.sample(frac=1, random_state=seed)

dropped_columns = ['fnlwgt', 'education-num', 'capital-gain', 'capital-loss']
df = dataset.drop(columns= dropped_columns)

X = df.drop('salary', axis=1)
y = df[['salary']]

# split data into train and test sets
# 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=seed, stratify=y)

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

y_pred = pipe.predict(X_test)

# calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")


joblib.dump(pipe, 'test_rf_model.sav')
