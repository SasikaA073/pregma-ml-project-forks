import streamlit as st
from pathlib import Path
from PIL import Image
# import streamlit_authenticator as stauth

# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader

st.set_page_config(
    page_title="PregMa App", 
    page_icon="icon.png",
    layout="centered",
)

st.title("PregMa ❤️")

# # User Authentication    
# credentials = {
#     "usernames":{
#         "eranga":{
#             "name":"Dr. Eranga",
#             "password": '$2b$12$JtByid2cjmgIfjF3/WjQkOpOYadkoWbv1yLtEc3XpAwaKOqeVY2tS'
#             },
#         "hiru":{
#             "name":"Dr. Hiru",
#             "password": '$2b$12$.0tFREKSvKXisqhwZt0AP.S9lqYlG8QYA0XpDUqtnnqRFokia64XO'
#             }            
#         }
#     }

# authenticator = stauth.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)

# name, authentication_status, username = authenticator.login('Login', 'main')

# if authentication_status == False:
#     st.error('Username/password is incorrect')

# if authentication_status == None:
#     st.warning('Please enter your username and password')
# # authentication_status = True
# if authentication_status:

#     authenticator.logout('Logout', 'sidebar', key='unique_key')
#     st.sidebar.write(f'Welcome *{name}*!')

st.subheader("Pregnant mother Health Monitoring System")

# Load image
logo = Image.open('logo.png')

# Display image using Streamlit
st.image(logo)
st.sidebar.error("Please use this under proper guidance of a medical staff officer!")

