# IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import plotly.express as px
from deta import Deta
import os
from dotenv import load_dotenv
from classes import Patient
import pickle
from database2 import *


DETA_KEY = "d0E7NcjK5X8P_RVUiBBKMe36JY7P9pen6WsDBawji3GTM"

# Initialize Deta with a project key
deta = Deta(DETA_KEY)

try:
    # create databses from month 1 to 6
    patients_db = deta.Base("patients_db")

    # Streamlit interface
    st.set_page_config(
        page_title="PregMa - Mother's Health Monitoring System",
        page_icon="icon.png",
        layout="centered",
    )

    st.title("Nurse Dashboard")

    # a list of patients data
    all_patients_details = get_all_patients()
    all_patients_details = pd.DataFrame(all_patients_details)

    # change the dataframe column order
    all_patients_details = all_patients_details[
        ["key", "first_name", "last_name", "age", "blood_group", "nic", "mobile_number"]
    ]
    # all_patients_details = all_patients_details['key', 'first_name', 'last_name', 'age']

    # display all details of all patients in a table
    st.markdown("## All Patients")
    st.dataframe(all_patients_details)

    # a form to choose a patient from the list of patients
    st.markdown("## Select a patient")

    with st.form(key="patient_id_form"):
        # Choose the patient id that the nurse wants to view
        option = st.selectbox("Select a patient", all_patients_details["key"])

        submit_button = st.form_submit_button(label="Select")

        if submit_button:

            # get patient details
            patient_dict = get_patient(option)
            patient_name = patient_dict["first_name"] + " " + patient_dict["last_name"]
            patient_blood_group = patient_dict["blood_group"]
            # display clicked option
            st.write("You selected:", option)
            st.markdown(f"Patient Name :{patient_name}")
            # st.markdown(f"Patient Blood Group :{patient_blood_group}")

            st.markdown(
                f"**Blood Group:** {patient_dict['blood_group']}  \n**Age:** {patient_dict['age']}"
            )

            # display patient details in a table for months from 1 to 6
            st.markdown("## Patient Details")

            # Recomment patients who has a high risk level to the doctor

            # get patient object
            patient_id = patient_dict["key"]

            # get all months details from month 1 to 6
            month1_dict = get_month_data(patient_id, 1)
            month2_dict = get_month_data(patient_id, 2)
            month3_dict = get_month_data(patient_id, 3)
            month4_dict = get_month_data(patient_id, 4)
            month5_dict = get_month_data(patient_id, 5)
            month6_dict = get_month_data(patient_id, 6)

            # create a dataframe with all the months data

            # Assuming that all the months data has been given.
            df = pd.DataFrame(
                {
                    "Month": [1, 2, 3, 4, 5, 6],
                    "Blood Sugar (mmol/L)": [
                        month1_dict["blood_sugar"],
                        month2_dict["blood_sugar"],
                        month3_dict["blood_sugar"],
                        month4_dict["blood_sugar"],
                        month5_dict["blood_sugar"],
                        month6_dict["blood_sugar"],
                    ],
                    "Systolic BP (mm Hg)": [
                        month1_dict["systolicBP"],
                        month2_dict["systolicBP"],
                        month3_dict["systolicBP"],
                        month4_dict["systolicBP"],
                        month5_dict["systolicBP"],
                        month6_dict["systolicBP"],
                    ],
                    "Diastolic BP (mm Hg)": [
                        month1_dict["diastolicBP"],
                        month2_dict["diastolicBP"],
                        month3_dict["diastolicBP"],
                        month4_dict["diastolicBP"],
                        month5_dict["diastolicBP"],
                        month6_dict["diastolicBP"],
                    ],
                    "Body Temperature (°C)": [
                        month1_dict["body_temp"],
                        month2_dict["body_temp"],
                        month3_dict["body_temp"],
                        month4_dict["body_temp"],
                        month5_dict["body_temp"],
                        month6_dict["body_temp"],
                    ],
                    "Heart Rate (bpm)": [
                        month1_dict["heart_rate"],
                        month2_dict["heart_rate"],
                        month3_dict["heart_rate"],
                        month4_dict["heart_rate"],
                        month5_dict["heart_rate"],
                        month6_dict["heart_rate"],
                    ],
                    "Predicted Risk Level": [
                        month1_dict["prediction"],
                        month2_dict["prediction"],
                        month3_dict["prediction"],
                        month4_dict["prediction"],
                        month5_dict["prediction"],
                        month6_dict["prediction"],
                    ],
                    # Add sample values for Actual Risk Level
                    "Actual Risk Level": [1, 2, 2, 1, 2, 2],
                }
            )

            # display the dataframe
            st.dataframe(df)

            # display a line chart with all the months data
            fig = px.line(
                df,
                x="Month",
                y=[
                    "Blood Sugar (mmol/L)",
                    "Systolic BP (mm Hg)",
                    "Diastolic BP (mm Hg)",
                    "Body Temperature (°C)",
                    "Heart Rate (bpm)",
                ],
                title="Patient Health History",
            )
            st.plotly_chart(fig)

            # display a bar chart with all the months data
            fig = px.bar(
                df,
                x="Month",
                y=["Predicted Risk Level", "Actual Risk Level"],
                title="Patient Risk Level History",
            )
            st.plotly_chart(fig)

except Exception as e:
    st.write(e)
    st.write("Please check your internet connection and try again.")
