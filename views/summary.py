import streamlit as st
import queries

def display():
    st.subheader("📍 Providers & Receivers by City")
    st.dataframe(queries.get_providers_receivers_by_city())

    st.subheader("🏆 Top Provider Types by Contributions")
    st.dataframe(queries.get_top_provider_type())

    st.subheader("📦 Total Quantity of Food Available")
    st.dataframe(queries.get_total_food_quantity())

    st.subheader("🏙️ Cities with Most Food Listings")
    st.dataframe(queries.get_top_city_by_listings())

    st.subheader("🥗 Commonly Available Food Types")
    st.dataframe(queries.get_common_food_types())