import streamlit as st
import easyocr as ocr  
from PIL import Image
import numpy as np
import time

st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System", 
    page_icon="❤️", 
    layout="centered",
)

st.title("User Profile")

st.markdown("Optical Character Recognizer")

image = st.file_uploader(label = "Upload your image here autofill or you can fill the form",type=['png','jpg','jpeg'])

@st.cache_data
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

# Initialize the variables
ocr_systolicBP = ""
ocr_diastolicBP = ""
ocr_blood_sugar = ""
ocr_body_temp = ""
ocr_heart_rate = ""

reader = load_model()
if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])


        try:
            ocr_systolicBP = result_text[6].split(" ")[-1]
            ocr_diastolicBP = result_text[7].split(" ")[-1]
            ocr_blood_sugar = result_text[8].split(" ")[-1]
            ocr_body_temp = result_text[9].split(" ")[-1]
            ocr_heart_rate = result_text[10].split(" ")[-1]
        except:
            pass
        
    st.warning("Please check the autofill data and fill the form if there are any missing data")
else:
    st.write("Upload an Image")


with st.form(key='pred_form'):
    patient_id = st.text_input(label="Patient ID")
    systolicBP = st.text_input(label='Systolic Blood Pressure', value=ocr_systolicBP)
    diastolicBP = st.text_input(label='Diastolic Blood Pressure',  value=ocr_diastolicBP)
    blood_sugar = st.text_input(label='Blood Sugar Level', value=ocr_blood_sugar)
    body_temp = st.text_input(label='Body Temperature (in Celsius))', value=ocr_body_temp)
    heart_rate = st.text_input(label='Heart Rate (in BPM)', value=ocr_heart_rate)
    month = st.selectbox(label='Month', options=['2', '3', '4', '5', '6'])

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

# st.sidebar.success("Let's monitor the Health status of the Mother")

# st.sidebar.subheader("Contact Us")
# st.sidebar.warning("Let's monitor the Health status of the Mother")
