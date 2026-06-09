import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Vault Logic", layout="centered")

# 2. Main Title
st.title("Vault Logic Official")

# 3. Provenance Header
st.write("### Provenance & History")
history_events = [
    {"date": "2026-06-01", "event": "Last Professional Appraisal", "detail": "Certified"},
    {"date": "2025-11-15", "event": "Ownership Transfer", "detail": "Transferred"},
    {"date": "2024-03-10", "event": "Initial Authentication", "detail": "Authenticated"}
]

for item in history_events:
    st.markdown(f'''
        <div style="border-left: 2px solid #00ff6e; padding-left: 15px; margin-bottom: 10px;">
            <p style="color: #00ff6e; font-weight: bold; margin: 0;">{item['date']}</p>
            <p style="margin: 0; font-size: 1.1em;">{item['event']}</p>
            <p style="color: #888; margin: 0; font-size: 0.9em;">{item['detail']}</p>
        </div>
    ''', unsafe_allow_html=True)