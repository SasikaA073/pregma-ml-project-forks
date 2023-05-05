import streamlit as st
# import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title="PregMa - Mother's Health Monitoring System", 
    page_icon="❤️", 
    layout="centered",
)

st.title("PregMa ❤️")
st.subheader("Mother's Health Monitoring System")
st.write('--------------')

# Create a login/logout widget
# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# name, authentication_status, username = authenticator.login('Login', 'main')
 
# # Authenticate the user
# if st.session_state["authentication_status"]:
#     authenticator.logout('Logout', 'main', key='unique_key')
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state["authentication_status"] is False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] is None:
#     st.warning('Please enter your username and password')


st.sidebar.subheader("Contact Us")

st.sidebar.caption("Dr. H. M. N. Dilum Bandara")
st.sidebar.caption("National Hospital of Sri Lanka")
st.sidebar.caption("Colombo 10")

st.sidebar.warning("Contact on an Emergency Situation")

st.sidebar.write('--------------')

st.sidebar.success("Let's monitor the Health status of the Mother")

