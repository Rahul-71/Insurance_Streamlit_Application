from pycaret.regression import load_model, predict_model, setup
import streamlit as st
import pandas as pd
import numpy as np

# Loading the model
model = load_model("deployment_04042022")
# Initial Setup
# lr = setup(data = pd.read_csv('insurance.csv'), target = 'charges')


def run():

    from PIL import Image
    image_hospital = Image.open("hospital_image.jpg")

    st.title("Insurance Application")
    st.sidebar.info("This application is created using Pycaret and streamlit")
    st.sidebar.success("Welcome to our Insurance Application")
    st.sidebar.image(image_hospital)

    # adding elements to take user input
    age = st.number_input("Age", max_value=50, min_value=15, value=21)
    bmi = st.number_input("BMI", max_value=50, min_value=10, value=18)
    sex = st.selectbox("Gender", ['Male', 'Female'])
    children = st.selectbox("Children", [0,1,2,3,4,5,6,7,8])

    if st.checkbox("Smoker"):
        smoker = 'yes'
    else:
        smoker = 'no'
    
    region = st.selectbox('Region', ['southwest', 'northwest', 'northeast', 'southeast'])

    output = ""

    # Input dictionary
    input_dict = {
        "age":age,
        "sex":sex,
        "bmi":bmi, 
        "children":children, 
        "smoker": smoker, 
        "region":region
    } 
    input_df = pd.DataFrame([input_dict])

    # Predict
    if st.button("Predict"):
        output = predict_model(model, data=input_df)
        st.success(f"The Insurance amount is ${output['Label'][0]:,}")
    


if __name__ == '__main__':
    run()