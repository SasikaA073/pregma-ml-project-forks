import streamlit_authenticator as stauth

passwords = ['abc123', 'def456']

hashed_passwords = stauth.Hasher(passwords).generate()

print(hashed_passwords)