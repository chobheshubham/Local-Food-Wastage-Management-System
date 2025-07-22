import streamlit as st
import queries

def display():
    st.subheader("🍛 Claims per Food Item")
    st.dataframe(queries.get_claims_per_food())

    st.subheader("🍽️ Most Claimed Meal Types")
    st.dataframe(queries.get_top_meal_type())

    st.subheader("📊 Quantity Donated by Providers")
    st.dataframe(queries.get_quantity_by_provider())