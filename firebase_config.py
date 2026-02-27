import firebase_admin
from firebase_admin import credentials, db, auth
import streamlit as st

if not firebase_admin._apps:
    private_key = st.secrets["firebase"]["private_key"]
    
    # Fix key formatting — ensure real newlines
    if "\\n" in private_key:
        private_key = private_key.replace("\\n", "\n")

    firebase_creds = {
        "type": "service_account",
        "project_id": st.secrets["firebase"]["project_id"],
        "private_key_id": st.secrets["firebase"]["private_key_id"],
        "private_key": private_key,
        "client_email": st.secrets["firebase"]["client_email"],
        "client_id": str(st.secrets["firebase"]["client_id"]),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"],
        "universe_domain": "googleapis.com"
    }
    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://mentalmadhilo-6900d-default-rtdb.firebaseio.com/"
    })

def get_db_reference(path):
    return db.reference(path)