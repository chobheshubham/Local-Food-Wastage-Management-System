import streamlit as st
import queries

def display():
    st.subheader("✅ Top Receivers by Claims")
    st.dataframe(queries.get_top_receivers())

    st.subheader("📈 Provider with Most Completed Claims")
    st.dataframe(queries.get_top_provider_by_claims())

    st.subheader("📊 Claims by Status")
    st.dataframe(queries.get_claim_status_distribution())

    st.subheader("📉 Avg Quantity Claimed Per Receiver")
    st.dataframe(queries.get_avg_claim_quantity())