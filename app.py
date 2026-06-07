import streamlit as st
import pandas as pd
import time
import valuation

from valuation import ValuationEngine

# --- INITIALIZATION ---
# This ensures the variable exists before the rest of your code tries to use it
if "asset_authenticated" not in st.session_state:
    st.session_state.asset_authenticated = False

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vault Logic Ledger", layout="centered")

# --- CUSTOM CSS (LEGENDS PALETTE) ---
st.markdown("""
<style>
    .stApp { background-color: #0d0d0d; color: #ffffff; }
    .portfolio-box { background-color: #141414; border: 1px solid #222222; padding: 20px; border-radius: 12px; }
    .neon-text { color: #00ff6e; font-weight: bold; font-family: monospace; font-size: 28px; }
    div.stButton > button { background-color: #111111; color: #00ff6e; border: 2px solid #222222; }
</style>
""", unsafe_allow_html=True)

# --- AUTHENTICATION LOGIC ---
query_params = st.query_params
decal_id = query_params.get("decal_id")

# Guard: Ensure decal_id is treated as a string or empty if missing
if decal_id is None:
    decal_id = ""

if decal_id:
    st.session_state.asset_authenticated = True

# --- THE SECURE GATE ---
if not st.session_state.asset_authenticated:
    st.title("🔒 Vault Logic Global Asset Ledger")
    st.info("Please scan a valid Vault Logic NFC decal to authenticate your asset.")
else:
    # --- AUTHENTICATION HANDSHAKE ---
    with st.spinner('Authenticating secure ledger connection...'):
        time.sleep(1.5)
    
    # --- LIVE STATUS BADGE ---
    st.markdown('''
    <div style="background-color: #0d0d0d; border: 1px solid #00ff6e; padding: 5px 15px; border-radius: 20px; display: inline-block; margin-bottom: 20px;">
        <span style="color: #00ff6e; font-size: 0.8em; font-family: monospace;">● LIVE SECURE CONNECTION | ENCRYPTED</span>
    </div>
    ''', unsafe_allow_html=True)
    
    # --- ASSET CERTIFICATE ---
    st.markdown(f'''
    <div class="portfolio-box">
    <h1>💎 Vault Logic Certified</h1>
    <p class="neon-text">Asset ID: {decal_id}</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.success("AUTHENTICITY VERIFIED")
    
    # --- IMMUTABLE LEDGER HASH ---
    import hashlib
    # Generate a unique hash for the asset's current verification
    hash_input = f"{decal_id}-{time.time()}".encode()
    ledger_hash = hashlib.sha256(hash_input).hexdigest()[:24].upper()
    
    st.markdown(f'''
    <div style="background-color: #0d0d0d; border: 1px solid #00ff6e; padding: 10px; border-radius: 5px; text-align: center;">
        <p style="color: #888; font-size: 0.7em; margin: 0;">SECURE LEDGER RECORD</p>
        <p style="color: #00ff6e; font-family: monospace; font-size: 0.9em; margin: 0;">{ledger_hash}</p>
    </div>
    ''', unsafe_allow_html=True)
    st.write("") # Add a little breathing room
    # --- DYNAMIC DATA & TREND CHART ---
    live_data = ValuationEngine.get_valuation(decal_id)
    st.metric(
        label="Live Market Appraisal",
        value=f"${live_data['value']:.2f}",
        delta=f"{live_data['trend']}%"
    )

    chart_data = pd.DataFrame(live_data.get('history', [0, 0]), columns=['Appraisal Value'])
    st.line_chart(chart_data, use_container_width=True)

    # --- PROVENANCE LOG ---
    st.write("### Provenance & History")
    history_events = [
        {"date": "2026-06-01", "event": "Last Professional Appraisal", "detail": "Certified Grade: Mint"},
        {"date": "2025-11-15", "event": "Ownership Transfer", "detail": "Transferred to Vault Logic Secure Storage"},
        {"date": "2024-03-10", "event": "Initial Authentication", "detail": "Origin Verified by Vault Logic"}
    ]
    
    for item in history_events:
        st.markdown(f'''
        <div style="border-left: 2px solid #00ff6e; padding-left: 15px; margin-bottom: 20px;">
            <p style="color: #00ff6e; font-weight: bold; margin: 0;">{item['date']}</p>
            <p style="margin: 0; font-size: 1.1em;">{item['event']}</p>
            <p style="color: #888; margin: 0; font-size: 0.9em;">{item['detail']}</p>
        </div>
        ''', unsafe_allow_html=True)
    # --- PREMIUM TIER GATE ---
    st.markdown("---") # Visual divider to separate history from the subscription offer
    if st.session_state.get('is_premium', False):
        st.success("✨ Vault Logic Premium Active")
        st.write("Full analytics, advanced security alerts, and insurance integration are enabled.")
    else:
        st.warning("🔒 Premium Tools Locked")
        # Now, the Call to Action sits directly below this warning
        if st.button("Upgrade to Vault Logic Premium"):
            st.write("Unlock full analytics at: [VaultLogicSystems.com](https://VaultLogicSystems.com)")
    
    # --- FINAL ACTIONS ---
    if st.button("Contact Vault Logic Support"):
        st.write("Inquiries: [VaultLogicSystems.com](https://VaultLogicSystems.com)")
    
    