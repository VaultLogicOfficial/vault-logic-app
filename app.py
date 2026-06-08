# --- PROVENANCE LOG ---
st.write("### Provenance & History")
history_events = [
    {"date": "2026-06-01", "event": "Last Professional Appraisal"},
    {"date": "2025-11-15", "event": "Ownership Transfer"}
]

for item in history_events:
    st.write(f"{item['date']} - {item['event']}")
