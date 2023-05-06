import streamlit as st
import time

st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System", 
    page_icon="❤️", 
    layout="centered",
)

st.title("User Profile")

with st.form(key='pred_form'):
    patient_id = st.text_input(label="Patient ID")
    systolicBP = st.text_input(label='Systolic Blood Pressure')
    diastolicBP = st.text_input(label='Diastolic Blood Pressure')
    blood_sugar = st.text_input(label='Blood Sugar Level')
    body_temp = st.text_input(label='Body Temperature (in Celsius))')
    heart_rate = st.text_input(label='Heart Rate (in BPM)')
    month = st.selectbox(label='Month', options=['2'])

    submit_button = st.form_submit_button(label='Update')

    if submit_button:
        # st.success("Mother {}'s Month {} results updated Successfully")
        # st.balloons()
        st.write("Systolic Blood Pressure: ", systolicBP)   
        st.write("Diastolic Blood Pressure: ", diastolicBP)
        st.write("Blood Sugar Level: ", blood_sugar)
        st.write("Body Temperature (in Celsius): ", body_temp, "°C")
        st.write("Heart Rate (in BPM): ", heart_rate)
        st.write("Month: ", month)

        
        st.success(f"Mother {patient_id}'s Month {month} results updated Successfully")
        pred = [0,1,2]
        time.sleep(2)
        if pred[0] == 0:
            st.success("Low Risk")
        elif pred[0] == 1:
            st.warning("Medium Risk")
        elif pred[0] == 2:
            st.error("High Risk")

st.sidebar.success("Let's monitor the Health status of the Mother")

st.sidebar.subheader("Contact Us")
st.sidebar.warning("Let's monitor the Health status of the Mother")
