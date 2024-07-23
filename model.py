import numpy as np
import pickle

with open('model.pickle', 'rb') as f:
  model = pickle.load(f)

import streamlit as st
st.title('Sales Prediction')
col1, col2 = st.columns(2)
with col1:
    x1 = st.number_input('TV')
with col2:
    x2 = st.number_input('Radio')
button = st.button('Predict', use_container_width=True)
if button:
    if x2 == 0 or x1 == 0:
        st.snow()
        st.error('Please input TV or Radio ads')
    else:
        X = np.array([[x1,x2]])
        y = model.predict(X)
        st.balloons()
        st.success(f'Sales Prediction: {y[0]:.2f}')
