import firebase_admin
from firebase_admin import credentials, db, auth
import streamlit as st
import json
import tempfile
import os

if not firebase_admin._apps:
    firebase_json = json.loads(st.secrets["FIREBASE_JSON"])
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(firebase_json, f)
        temp_path = f.name
    
    cred = credentials.Certificate(temp_path)
    firebase_admin.initialize_app(cred, {
        "databaseURL": st.secrets["FIREBASE_DB_URL"]
    })
    
    os.unlink(temp_path)

def get_db_reference(path):
    return db.reference(path)