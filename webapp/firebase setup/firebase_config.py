import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from google.oauth2 import id_token
from google.auth.transport import requests
import webbrowser

# Initialize Firebase SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Create a reference to the Firestore database
db = firestore.client()

# You will need to create a Google OAuth2 client using the client ID and secret you obtained earlier
from requests_oauthlib import OAuth2Session

client_id = '457198646172-t2f9jg3q5nq87b343a5dedoq5441haos.apps.googleusercontent.com'
client_secret = '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'

client = OAuth2Session(client_id, redirect_uri='http://localhost:8501/login/google/callback')
client.scope = ['openid', 'email', 'profile']
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://accounts.google.com/o/oauth2/token'


# Create a login function that handles the authentication flow
def login():
    # Check if the user is already logged in
    if 'user' in st.session_state:
        return True
    
    # Check if the user has a valid token
    token = st.secrets['token']
    try:
        # Verify the token and get the user info
        info = id_token.verify_oauth2_token(token, requests.Request())
        st.session_state['user'] = info
        return True
    except:
        return False


# =============== streamlit_app.py ===============
# Set up your Streamlit app to use this login function
if not login():
    # If the user is not logged in, display a login button
    st.write('Please log in with your Google account to use this app.')
    auth_url, _ = client.authorization_url('https://accounts.google.com/o/oauth2/auth', access_type='offline')
    if st.button('Log in with Google'):
        webbrowser.open(auth_url)
else:
    # If the user is logged in, display the app
    st.write('Welcome, {}!'.format(st.session_state['user']['name']))
    
    # TODO: Add your app code here
    pass
