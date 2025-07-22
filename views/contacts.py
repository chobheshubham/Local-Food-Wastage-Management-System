import streamlit as st
import queries

def display():
    st.subheader("📞 Find Food Providers by City")
    city = st.text_input("Enter City Name (case-sensitive):")
    if city:
        df = queries.get_providers_by_city(city)
        if not df.empty:
            st.dataframe(df)
        else:
            st.warning("No providers found in this city.")