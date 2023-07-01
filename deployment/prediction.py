import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import json

with open('deployment/model_rfr.pkl', 'rb') as file_1:
  model_rfr = joblib.load(file_1)

def run():

    st.title('PREDIKSI KEKUATAN BETON')

    st.subheader('Input Nilai untuk melakukan Prediksi')

    with st.form(key='pb23'):
        
        st.markdown('---')

        Cement = st.number_input('Cement', min_value=100, max_value=540, value=280, step=5)
        Age = st.number_input('Age', min_value=1, max_value=365, value=29, step=7)
        Superplasticizer = st.slider('Superplasticizer', 0.0, 32.0, 6.0, 0.2)
        Fly_Ash = st.slider('Fly Ash', 0.0, 200.0, 55.5, 0.5)
        Blast_Furnace_Slag = st.slider('Blast Furnace Slag', 0.0, 360.0, 72.0, 0.5)

        submitted = st.form_submit_button('PREDIKSI')

    data_x_new = {
        'Cement': Cement,
        'Age': Age,
        'Superplasticizer': Superplasticizer,
        'Fly Ash': Fly_Ash,
        'Blast Furnace Slag': Blast_Furnace_Slag
    }

    data_x_new = pd.DataFrame([data_x_new])
    st.dataframe(data_x_new)
    
    if submitted:

        data_y_pred = model_rfr.predict(data_x_new)   
        st.write('# Prediksi Kekuatan Beton:', str(int(data_y_pred)))

if __name__ == '__main__':
    run()