import streamlit as st

st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System", 
    page_icon="❤️", 
    layout="centered",
)

st.title("Register a New Mother")

with st.form(key='reg_form'):
    first_name = st.text_input(label='First Name')
    last_name = st.text_input(label='Last Name')
    nic = st.text_input(label='NIC')
    date_of_birth = st.date_input(label='Date of Birth')
    blood_group = st.selectbox(label='Blood Group', options=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    mobile_number = st.text_input(label='Mobile Number')

    submit_button = st.form_submit_button(label='Register')

    if submit_button:
        st.success("Mother {} Registered Successfully".format(first_name))
        st.balloons()
        st.write("First Name: ", first_name)
        st.write("Last Name: ", last_name)
        st.write("Date of Birth: ", date_of_birth)
        st.write("Blood Group: ", blood_group)
        st.write("Mobile Number: ", mobile_number)

st.title("User Profile")

with st.form(key='pred_form'):
    systolicBP = st.text_input(label='Systolic Blood Pressure')
    diastolicBP = st.text_input(label='Diastolic Blood Pressure')
    blood_sugar = st.text_input(label='Blood Sugar Level')
    body_temp = st.text_input(label='Body Temperature (in Celsius))')
    heart_rate = st.text_input(label='Heart Rate (in BPM)')
    month = 1

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.success("Mother's Month 1 results updated Successfully".format(first_name))
        st.balloons()
        st.write("Systolic Blood Pressure: ", systolicBP)   
        st.write("Diastolic Blood Pressure: ", diastolicBP)
        st.write("Blood Sugar Level: ", blood_sugar)
        st.write("Body Temperature (in Celsius): ", body_temp)
        st.write("Heart Rate (in BPM): ", heart_rate)
        st.write("Month: ", month)
    


    st.sidebar.success("Let's start monitering after the Registration")