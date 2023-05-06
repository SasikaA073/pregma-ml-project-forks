from deta import Deta
import os
# from dotenv import load_dotenv
from classes import Patient


DETA_KEY = "d0E7NcjK5X8P_RVUiBBKMe36JY7P9pen6WsDBawji3GTM"

# Initialize Deta with a project key
deta = Deta(DETA_KEY)

# # create a DB and connect it
patients_db = deta.Base("patients_db")

# function to insert data to the patients database
def insert_patient(patient_id, first_name, last_name, nic, age, blood_group, mobile_number):
    patients_db.insert({
        "key": patient_id,
        "first_name": first_name,
        "last_name": last_name,
        "nic": nic,
        # "date_of_birth": date_of_birth,
        "age":age,
        "blood_group": blood_group,
        "mobile_number": mobile_number,
    })

    

# function to add test results data for the first month  to the database
def add_month_data(patient_id, month_no, systolicBP, diastolicBP,blood_sugar, body_temp, heart_rate, prediction, date):
    db = deta.Base(f"month{month_no}_db")
    db.insert({
        "key":patient_id,
        "systolicBP": systolicBP,
        "diastolicBP":diastolicBP,
        "blood_sugar":blood_sugar,
        "body_temp":body_temp, 
        "heart_rate":heart_rate, 
        "prediction":prediction, 
        "date":str(date)
    })


# function to get month data from the month databases when the patient id and month is given
def get_month_data(patient_id, month_no):
    db = deta.Base(f"month{month_no}_db")
    return db.get(patient_id)


# function to read data from the patients database
def get_patient(patient_id):
    return patients_db.get(patient_id)

# function to read all data from the patients database
def get_all_patients():
    return patients_db.fetch().items