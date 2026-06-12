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

import pandas as pd
import plotly.express as px
import streamlit as st

# The Navigation Vault - Now Dynamic
with st.expander("View Provenance History"):
    # Load the data directly from the CSV
    df = pd.read_csv("history.csv")
    
    # Iterate through the rows of the CSV
    for index, item in df.iterrows():

        st.markdown(f'''
            <div style="border-left: 2px solid #00ff6e; padding-left: 15px; margin-bottom: 10px;">
            <p style="color: #00ff6e; font-weight: bold; margin: 0;">{item['date']}</p>
            <p style="margin: 0; font-size: 1.1em;">{item['event']}</p>
            <p style="color: #888; margin: 0; font-size: 0.9em;">{item['detail']}</p>
            </div>
        ''', unsafe_allow_html=True)

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



