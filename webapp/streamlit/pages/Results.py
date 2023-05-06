import streamlit as st
import easyocr as ocr  
from PIL import Image
import numpy as np
import time

st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System", 
    page_icon="icon.png", 
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

#This function will return the diagnosis of the patient as a text output.
# Taking parameters (N=normal, L=low, H=high)
# Format : inputDict = {"systolicBP": None, "diastolicBP": None, "blood_sugar": None, "body_temp": None, "heart_rate": None, "month": None, "age": None}
def getdiagnosis(inputDict):
    outputString = ""

    
    # Evaluate the ranges of the parameters
    if 90 <= inputDict["systolicBP"] <= 120:
        inputDict["systolicBP"] = "N--"
    elif inputDict["systolicBP"] < 90:
        inputDict["systolicBP"] = "L--"
    else:
        inputDict["systolicBP"] = "H--"

    if 60 <= inputDict["diastolicBP"] <= 80:
        inputDict["diastolicBP"] = "N--"
    elif inputDict["diastolicBP"] < 60:
        inputDict["diastolicBP"] = "L--"
    else:
        inputDict["diastolicBP"] = "H--"

    if 100 <= inputDict["blood_sugar"] <= 125:
        inputDict["blood_sugar"] = "N--"
    elif inputDict["blood_sugar"] < 100:
        inputDict["blood_sugar"] = "L--"
    else:
        inputDict["blood_sugar"] = "H--"

    if 36.5 <= inputDict["body_temp"] <= 37.5:
        inputDict["body_temp"] = "N--"
    elif inputDict["body_temp"] < 36.5:
        inputDict["body_temp"] = "L--"
    else:
        inputDict["body_temp"] = "H--"

    if 60 <= inputDict["heart_rate"] <= 100:
        inputDict["heart_rate"] = "N--"
    elif inputDict["heart_rate"] < 60:
        inputDict["heart_rate"] = "L--"
    else:
        inputDict["heart_rate"] = "H--"

    if 18 <= inputDict["age"] <= 45:
        inputDict["age"] = "N--"
    elif inputDict["age"] < 18:
        inputDict["age"] = "L--"
    else:
        inputDict["age"] = "H--"

    # Decode the output(The knowledge tree)
    for parameter in inputDict:
        if inputDict[parameter] == "N--":
            pass
        elif inputDict[parameter] == "L--":
            match parameter:
                case "systolicBP":
                    outputString += "* Patient's systolic blood pressure is low. This patient has a risk of having cold and clammy skin, fainting, dizziness, fatigue, nausea,breathing difficulities and vomiting.\n"
                case "diastolicBP":
                    outputString += "* Patient's diastolic blood pressure is low. This patient has a increased risk of having heart diseasses.\n"
                case "blood_sugar":
                    outputString += "* Patient's blood sugar is not adequate. This can cause hormonal changes and may result in long term health effects.\n"
                case "body_temp":
                    outputString += "* Patient's body temperature is below the threshold. She will have a risk of having organ failiures and increased vulnerabilities to infections.\n"
                case "heart_rate":
                    outputString += "* Your patient's heart rate is low.This may result in reduced blood flow to the brain and other vital organs.\n"
                case "age":
                    outputString += "* Your patient's age can cause pre mature births if not diagnosed properly in upcoming trimesters.\n"
        else:
            match parameter:
                case "systolicBP":
                    outputString += "* Patient's systolic blood pressure is high. This can cause kidney diseases, Cardiovascular diseases, vision loss, angina and peripheral artery disease.\n"
                case "diastolicBP":
                    outputString += "* Your patients diastolic blood pressure is beyond the normal range.She has a risk of cardiovascular disease,eye damages and vulnerebility to dimentia.\n"
                case "blood_sugar":
                    outputString += "* Patient's blood sugar is high. This can damage her blood vessels and nerves and can be a cause for being vulnerable to infections.\n"
                case "body_temp":
                    outputString += "* Patient's body temperature is high and not in the normal range. May cause dehydration and other health issues.\n"
                case "heart_rate":
                    outputString += "* Your heart rate is above the threshold and this can cause reduced cardio ouput.\n"
                case "age":
                    outputString += "* Patient is somewhat older. This can cause low birth weights of child, pre mature births and other pregnancy complications\n"
        
        if outputString == "":
            outputString = "You are healthy. Please maintain your health."
    return outputString

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

        if systolicBP!="" and diastolicBP!="" and blood_sugar!="" and body_temp!="" and heart_rate!="" and month!="":
            st.success(f"Mother {patient_id}'s Month {month} results updated Successfully")
            pred = [0,1,2]
            time.sleep(2)
            if pred[0] == 0:
                st.success("Low Risk")
            elif pred[0] == 1:
                st.warning("Medium Risk")
            elif pred[0] == 2:
                st.error("High Risk")

            st.markdwon("## Diagnosis")
            st.markdown(getdiagnosis({"systolicBP":float(systolicBP), 
                                   "diastolicBP":float(diastolicBP), 
                                  "blood_sugar": float(blood_sugar),
                                    "body_temp": float(body_temp),
                                      "heart_rate":  float(heart_rate),
                                        "age": float(month)}))
        else :
            st.error("Please fill all the fields")

# st.sidebar.success("Let's monitor the Health status of the Mother")

# st.sidebar.subheader("Contact Us")
# st.sidebar.warning("Let's monitor the Health status of the Mother")