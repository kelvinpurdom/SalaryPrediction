import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict


st.button('Predict type of Iris')

if st.button('Predict type of Iris'):
   result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
   st.text(result[0])
