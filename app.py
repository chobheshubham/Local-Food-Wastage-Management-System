import streamlit as st
import queries
from views import summary, food_listings, claims_analysis, contacts, manage_listings

st.set_page_config(page_title="Local Food Wastage System", layout="wide")
st.title("🍽️ Local Food Wastage Management System")
st.markdown("Connect food donors with those in need to reduce food waste.")

st.sidebar.header("📂 Navigation")
tab = st.sidebar.radio("Select a Section", [
    "Summary",
    "Food Listings",
    "Claims Analysis",
    "Contacts",
    "Manage Food Listings"
])

# Layout: Left - Nav (sidebar), Right - Content
left_col, right_col = st.columns([1, 4])

# Show content in right column
with right_col:
    if tab == "Summary":
        summary.display()
    elif tab == "Food Listings":
        food_listings.display()
    elif tab == "Claims Analysis":
        claims_analysis.display()
    elif tab == "Contacts":
        contacts.display()
    elif tab == "Manage Food Listings":
        manage_listings.display()