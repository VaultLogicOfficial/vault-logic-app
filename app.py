import streamlit as st
import pandas as pd
import plotly.express as px
from auth import SecurityVault

# Page Configuration
st.set_page_config(page_title="Vault Logic", layout="centered")

# 1. Initialize the Vault
vault = SecurityVault()
password = st.sidebar.text_input("Enter Vault Key", type="password")

# 2. Security Check
if password != "SECRET123":
    st.warning("Access Denied: Please enter the correct Vault Key.")
    st.stop()

# 3. Main Display
st.title("Vault Logic Official")
st.metric("Current Asset Value", "$125,000", "+5.2%")


# 5. ---GATEWAY HEADER  ---
st.markdown("""
    <div style="background-color: #2E2E2E; padding: 20px; border-radius: 10px; border: 2px solid #D4AF37;">
        <h1 style="color: #D4AF37; text-align: center; font-family: sans-serif;">Vault Logic Discovery</h1>
        <p style="color: #FFFFFF; text-align: center; font-size: 1.2em;">Discovery Authorized: Official Asset Ledger</p>
    </div>
""", unsafe_allow_html=True)
st.write("")


# 6. The Navigation Vault - Now Dynamic


# The Growth Chart (Vault Logic Discovery Edition)
st.subheader("Asset Performance")
# 'df' already contains the 'value' column from your CSV
fig = px.line(df, x='date', y='value', markers=True, line_shape='spline')

# Applying the Legends Palette aesthetic
fig.update_traces(line_color='#D4AF37') # Legend Gold

fig.update_layout(
    plot_bgcolor='#2E2E2E', # Gotham Matte
    paper_bgcolor='#2E2E2E',
    font_color='#FFFFFF',
    xaxis=dict(showgrid=True, gridcolor='#444444'),
    yaxis=dict(showgrid=True, gridcolor='#444444')
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
    <style>
    /* Styling the text input fields */
    div[data-baseweb="input"] {
        border: 2px solid #D4AF37 !important;
        background-color: #2E2E2E !important;
    }
    /* Making sure the text inside the fields is visible */
    input {
        color: #FFFFFF !important;
    }
    /* Styling the label text */
    label {
        color: #D4AF37 !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

   # The Submission Portal
with st.expander("Add New Provenance Record"):
    with st.form("entry_form"):
        new_date = st.date_input("Date")
        new_event = st.text_input("Event")
        new_detail = st.text_input("Detail")
        new_value = st.number_input("Value", min_value=0)
        
        submitted = st.form_submit_button("Commit to Ledger")
        
        if submitted:
            # Create a new row
            new_data = pd.DataFrame([[new_date, new_event, new_detail, new_value]], 
                                    columns=['date', 'event', 'detail', 'value'])
            # Append to your existing file
            new_data.to_csv("history.csv", mode='a', header=False, index=False)
            st.success("Record committed to the global ledger.")



