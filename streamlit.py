import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict


st.title('Salary Predictor')

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Age:', min_value=17, max_value=90, value=35, step= 1)
    workclass= st.selectbox('Workclass:', [' State-gov', ' Self-emp-not-inc', ' Private', ' Federal-gov',
                                           ' Local-gov', ' ?', ' Self-emp-inc', ' Without-pay',' Never-worked'
                                           ])
    education = st.selectbox('Education:', [' Bachelors', ' HS-grad', ' 11th', ' Masters', ' 9th',
                                            ' Some-college', ' Assoc-acdm', ' Assoc-voc', ' 7th-8th',
                                            ' Doctorate', ' Prof-school', ' 5th-6th', ' 10th',
                                            ' 1st-4th',' Preschool', ' 12th'
                                            ])

with col2:
    marital_status = st.selectbox('Marital Status:', [' Never-married', ' Married-civ-spouse',
                                                       ' Divorced',' Married-spouse-absent', ' Separated',
                                                       ' Married-AF-spouse',' Widowed'
                                                       ])
    occupation = st.selectbox('Occupation:', [' Adm-clerical', ' Exec-managerial', ' Handlers-cleaners',
                                              ' Prof-specialty', ' Other-service', ' Sales', ' Craft-repair',
                                              ' Transport-moving', ' Farming-fishing', ' Machine-op-inspct',
                                              ' Tech-support', ' ?', ' Protective-serv', ' Armed-Forces',' Priv-house-serv'])
    relationship = st.selectbox('Relationship:', [' Not-in-family', ' Husband', ' Wife',
                                                  ' Own-child', ' Unmarried',' Other-relative'
                                                  ])
    race = st.selectbox('Race:', [' White', ' Black', ' Asian-Pac-Islander',
                                  ' Amer-Indian-Eskimo',' Other'
                                  ])


with col3:
    sex = st.selectbox('Sex:', [' Male', ' Female'])
    hours_per_week = st.number_input('Hours Per Week:', min_value=0, max_value=99, value=40,step= 1)
    native_country = st.selectbox('Native Country:', [' United-States', ' Cuba', ' Jamaica',
                                                      ' India', ' ?', ' Mexico',' South', ' Puerto-Rico',
                                                      ' Honduras', ' England', ' Canada',' Germany',
                                                      ' Iran', ' Philippines', ' Italy', ' Poland',
                                                      ' Columbia', ' Cambodia', ' Thailand', ' Ecuador',
                                                      ' Laos',' Taiwan', ' Haiti', ' Portugal', ' Dominican-Republic',
                                                      ' El-Salvador', ' France', ' Guatemala', ' China', ' Japan',
                                                      ' Yugoslavia', ' Peru', ' Outlying-US(Guam-USVI-etc)', ' Scotland',
                                                      ' Trinadad&Tobago', ' Greece', ' Nicaragua', ' Vietnam', ' Hong',
                                                      ' Ireland', ' Hungary', ' Holand-Netherlands'
                                                      ])




if st.button('Predict Salary'):
   result = predict(pd.DataFrame([[age, workclass, education,
                           marital_status, occupation,
                           relationship, race, sex,
                           hours_per_week, native_country]],
                                 columns= ['age', 'workclass', 'education',
                                           'marital-status', 'occupation',
                                           'relationship', 'race', 'sex',
                                           'hours-per-week', 'native-country'
                                           ]))
   if result[0] == ' >50k':
       st.text('You will probably earn more than 50K')
   else:
       st.text('You will probably earn less than 50K')
