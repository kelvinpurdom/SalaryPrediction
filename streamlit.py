import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict


st.button('Predict type of Iris')

if st.button('Predict type of Iris'):
   result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
   st.text(result[0])




   ex = pd.DataFrame([[39,'State-gov','Bachelors', 'Never-married',
                      'Adm-clerical',	'Not-in-family',
                      'White', 'Male', 40, 'United-States']],
                  columns=['age', 'workclass', 'education',
                           'marital-status', 'occupation',
                           'relationship', 'race', 'sex',
                           'hours-per-week', 'native-country'])
