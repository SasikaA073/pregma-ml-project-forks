import streamlit as st
from PIL import Image

# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader

st.set_page_config(
    page_title="PregMa App", 
    page_icon="icon.png",
    layout="centered",
)

st.title("PregMa ❤️")
st.subheader("Pregnant mother Health Monitoring System")

# Load image
logo = Image.open('logo.png')

# Display image using Streamlit
st.image(logo)

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

st.sidebar.caption("Email : reigonalmedicalofficer@gmail.com")
st.sidebar.caption("Dr. S. M. S. S. Senarathne,\n\nCasal Hospital,\n\nDarley Road,\n\nColombo 10")

st.sidebar.warning("Contact the doctor in an Emergency")

st.sidebar.write('--------------')

st.sidebar.error("Please use this under proper guidance of a medical staff officer!")

