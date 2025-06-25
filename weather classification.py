# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 12:50:10 2025

@author: Asus
"""


import numpy as np
import pickle
import streamlit as st

#loading the saved models
loaded_model= pickle.load(open('weather.sav','rb'))

# Prediction function
def weather_prediction(input_data):
    # Convert input to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Predict
    prediction = loaded_model.predict(input_data_reshaped)
    
    
    # Return result as string
   
    if prediction[0]==0:
        return"sunny"
    elif prediction[0]==1:
        return"cloudy"
    else:
        return"rainy"

# Main function for UI
def main():
    st.title('weather Prediction Web App')


    # Input fields
    Temperature = st.text_input('Enter temparutre in celcius')
    Humidity = st.text_input('Enter humididty(1-100')
    Speed = st.text_input('enter Speed')
    Precipitation = st.text_input('Enter precipation level(1-100')
    Cloud_Cover = st.text_input('Enter cloudCover(party Cloudy:3,Overcast:2,Clear:0,cloudy:1)')
    Atmospheric_Pressure  = st.text_input('Enter Atmospheric Pressure')
    UV_Index = st.text_input('Enter UVIndex(1-10)')
    Season = st.text_input('Enter Season(Autumn:0,Summer:2,Spring:1,Winter:3)')
    Visibility = st.text_input('Enter visiblity in km(1-10)')
    Location = st.text_input('Enter Location(coastal:0,inland:1,mountain:2)')
    weather = ''

    # Button for prediction
    if st.button('weather Test Result'):
        try:
            # Convert inputs and predict
            input_list = [float(Temperature), float( Humidity), float( Speed),
                          float(Precipitation), float(Cloud_Cover), float(Atmospheric_Pressure),
                          float(UV_Index), float(Season),float(Visibility),float(Location )]
            weather = weather_prediction(input_list)
        except ValueError:
            weather = "Please enter valid numeric values in all fields."

    st.success(weather)
main()
    
            
    

    
