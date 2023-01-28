import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Cap-diameter(cm):', min_value=0.0, max_value=64.0, value=1.0, step= 0.05)
    workclass= st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken'])
    education = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken'])

with col2:
    marital_status = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken'])
    occupation = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken'])
    relationship = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken'])
    race = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken'])


with col3:
    sex = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken'])
    hours_per_week = st.number_input('Stem Width(cm):', min_value=0.0, max_value=34.0, value=1.0,step= 0.05)
    native_country = st.selectbox('Cap Shape:', ['Convex', 'Flat', 'Sunken'])


st.button('Predict type of Iris')

if st.button('Predict type of Iris'):
   result = predict(np.array([[age, workclass, education,
                           marital_status, occupation,
                           relationship, race, sex,
                           hours_per_week, native_country]]))
   st.text(result[0])




   ex = pd.DataFrame([[39,'State-gov','Bachelors', 'Never-married',
                      'Adm-clerical',	'Not-in-family',
                      'White', 'Male', 40, 'United-States']],
                  columns=['age', 'workclass', 'education',
                           'marital-status', 'occupation',
                           'relationship', 'race', 'sex',
                           'hours-per-week', 'native-country'])
