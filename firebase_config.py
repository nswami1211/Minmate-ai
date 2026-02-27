import firebase_admin
from firebase_admin import credentials, db, auth
import streamlit as st

if not firebase_admin._apps:
    key = st.secrets["firebase"]["private_key"]
    
    # Fix all possible formatting issues automatically
    key = key.replace("\\n", "\n")  # literal \n to real newline
    key = key.replace(" ", "\n")     # spaces to newlines
    
    # Clean up header and footer
    key = key.replace("-----BEGIN\nPRIVATE\nKEY-----", "-----BEGIN PRIVATE KEY-----")
    key = key.replace("-----END\nPRIVATE\nKEY-----", "-----END PRIVATE KEY-----")
    
    # Ensure newlines after header and before footer
    key = key.replace("-----BEGIN PRIVATE KEY-----", "-----BEGIN PRIVATE KEY-----\n")
    key = key.replace("-----END PRIVATE KEY-----", "\n-----END PRIVATE KEY-----\n")
    
    # Clean double newlines
    while "\n\n" in key:
        key = key.replace("\n\n", "\n")

    firebase_creds = {
        "type": "service_account",
        "project_id": st.secrets["firebase"]["project_id"],
        "private_key_id": st.secrets["firebase"]["private_key_id"],
        "private_key": key,
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
        "databaseURL": st.secrets["FIREBASE_DB_URL"]
    })

def get_db_reference(path):
    return db.reference(path)