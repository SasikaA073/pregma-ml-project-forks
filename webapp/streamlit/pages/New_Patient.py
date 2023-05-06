import streamlit as st
import easyocr as ocr  
from PIL import Image
import numpy as np
from classes import Patient
from database2 import *
import pickle
import datetime

# Load ML model
ml_model_name = "./month1_model.pkl"
ml_model = pickle.load(open(ml_model_name, 'rb'))

# A dictionary to map the output of the model to the risk level
risk_level_dict = {0:"Low risk", 1:"Medium risk", 2:"High risk"}

st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System", 
    page_icon="icon.png", 
    layout="centered",
)

st.title("Register a New Mother")


st.markdown("Optical Character Recognizer")

image = st.file_uploader(label = "Upload your image here autofill or you can fill the form",type=['png','jpg','jpeg'])

@st.cache_data
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

# Initialize the variables
ocr_first_name = ""
ocr_last_name = ""
ocr_nic = ""
ocr_mobile_number = ""
ocr_age = ""
ocr_blood_group = "A+"
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
            ocr_first_name = result_text[0].split(" ")[-1]
            ocr_last_name = result_text[1].split(" ")[-1]
            ocr_nic = result_text[2].split(" ")[-1]
            ocr_mobile_number = result_text[3].split(" ")[-1]
            ocr_age = result_text[4].split(" ")[-1]
            ocr_blood_group = result_text[5].split(" ")[-1]
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



with st.form(key='reg_form'):
    patient_id = st.text_input(label='Patient ID').lower()
    first_name = st.text_input(label='First Name', value=ocr_first_name)
    last_name = st.text_input(label='Last Name', value=ocr_last_name)
    nic = st.text_input(label='NIC', value=ocr_nic)
    mobile_number = st.text_input(label='Mobile Number', value=ocr_mobile_number)

    age = st.text_input(label='Age', value=ocr_age)
    blood_group = st.selectbox(label='Blood Group', options=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        
        st.success(f"Mother {patient_id} Registered Successfully".format(first_name))
        # st.balloons()
        st.write("First Name: ", first_name)
        st.write("Last Name: ", last_name)
        st.write("Age: ", age)
        st.write("Blood Group: ", blood_group)
        st.write("Mobile Number: ", mobile_number)

        # Get the current date
        
        date = str(datetime.datetime.now().date())

        # write to the database
        insert_patient(patient_id, first_name, last_name, nic, age, blood_group, mobile_number)

        st.success(f"{patient_id} Mother registered Successfully")
             
    


    st.sidebar.success("Let's start monitering after the Registration")