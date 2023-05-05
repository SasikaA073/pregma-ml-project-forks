from deta import Deta
import os
from dotenv import load_dotenv
from classes import Patient


# Load your Deta project key from an environment variable
load_dotenv(".env")
DETA_KEY = os.getenv('DETA_PROJECT_KEY') 


# Initialize Deta with a project key
deta = Deta(DETA_KEY)

# create a DB and connect it
patients_db = deta.Base("patients_db")

# Insert data
def insert_patient(patient_id, first_name, last_name, nic, date_of_birth, blood_group, mobile_number):
    patients_db.insert({
        "key": patient_id,
        "first_name": first_name,
        "last_name": last_name,
        "nic": nic,
        "date_of_birth": date_of_birth,
        "blood_group": blood_group,
        "mobile_number": mobile_number
    })



# insert_patient("P001", "Kamala", 25, 1)
# insert_patient("P002", "Nimala", 30, 2)

# Get data
def get_patient(patient_id):
    return patients_db.get(patient_id)

# print(get_patient("P001"))

# Fetch all data
def get_all_patients():
    return patients_db.fetch().items

# print(get_all_patients())

# Update data

def update_patient(patient_id, patient_name, patient_age, month):
    patients_db.put({
        "key": patient_id,
        "patient_name": patient_name,
        "patient_age": patient_age,
        "month": month
    })

# Delete data
def delete_patient(patient_id):
    patients_db.delete(patient_id)

# delete_patient("P002")
