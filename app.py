import streamlit as st

from auth import SecurityVault

# 1. Initialize the Vault (The Door)
vault = SecurityVault()
password = st.sidebar.text_input("Enter Vault Key", type="password")

# 2. The Checkpoint (The Lock)
if password != "SECRET123": 
    st.warning("Access Denied: Please enter the correct Vault Key.")
    st.stop() 

# 3. The Display Layer (The Room - keep your existing code here)

st.set_page_config(page_title="Vault Logic", layout="centered")

# 2. Main Title
st.title("Vault Logic Official")

# 1. The Intelligence Header
st.metric("Current Asset Value", "$125,000", "+5.2%")
# 2. The Navigation Vault
with st.expander("View Provenance History"):
    history_events = [
        {"date": "2026-06-01", "event": "Last Professional Appraisal", "detail": "Certified"},
        {"date": "2025-11-15", "event": "Ownership Transfer", "detail": "Transferred"},
        {"date": "2024-03-10", "event": "Initial Authentication", "detail": "Authenticated"}
    ]
    
    # Notice this is now indented under the 'with' statement
    for item in history_events:
        st.markdown(f'''
            <div style="border-left: 2px solid #00ff6e; padding-left: 15px; margin-bottom: 10px;">
            <p style="color: #00ff6e; font-weight: bold; margin: 0;">{item['date']}</p>
            <p style="margin: 0; font-size: 1.1em;">{item['event']}</p>
            <p style="color: #888; margin: 0; font-size: 0.9em;">{item['detail']}</p>
            </div>
        ''', unsafe_allow_html=True)




