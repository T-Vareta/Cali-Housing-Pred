import streamlit as st
import pickle
import pandas as pd

st.title('Housing Price Prediction for the California Region for XYZ Brokerage')
st.write('This web app predicts the **House Price** in the California Region for XYZ Brokerage')

# to read the model from the pickle file
model=pickle.load(open('model_lr.pkl','rb'))

# get the input from the user
med_inc=st.number_input('Median Income')
house_age=st.number_input('House Age')
ave_rooms=st.number_input('Ave Rooms')
ave_bedrms=st.number_input('Ave Bedrooms')
population=st.number_input('Population')
ave_occup=st.number_input('Ave Occupancy')
latitude=st.number_input('Latitude')
longitude=st.number_input('Longitude')

# convert the user input to a dataframe
user_data=pd.DataFrame({'MedInc':med_inc,
    'HouseAge':house_age,
    'AveRooms':ave_rooms,
    'AveBedrms':ave_bedrms,
    'Population':population,
    'AveOccup':ave_occup,
    'Latitude':latitude,
    'Longitude':longitude}, index=[0])

# predict the house price
prediction=model.predict(user_data)

if st.button('Predict'):
    st.write(f'The predicted house price is {prediction[0]* 100000}')