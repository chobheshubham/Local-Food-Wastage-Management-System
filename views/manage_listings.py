import streamlit as st
import sqlite3
from datetime import date

def get_connection():
    return sqlite3.connect("food_waste.db")

def display():
    st.subheader("🛠️ Manage Food Listings (CRUD)")

    action = st.selectbox("What do you want to do?", ["Add", "Update", "Delete"])

    if action == "Add":
        with st.form("add_form"):
            food_id = st.number_input("Food ID", min_value=1)
            food_name = st.text_input("Food Name")
            quantity = st.number_input("Quantity", min_value=1)
            expiry = st.date_input("Expiry Date", min_value=date.today())
            provider_id = st.number_input("Provider ID", min_value=1)
            provider_type = st.text_input("Provider Type")
            location = st.text_input("City / Location")
            food_type = st.selectbox("Food Type", ["Vegetarian", "Non-Vegetarian", "Vegan"])
            meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snacks"])
            submit = st.form_submit_button("Add Food")

            if submit:
                conn = get_connection()
                cursor = conn.cursor()
                try:
                    cursor.execute("""
                        INSERT INTO food_listings 
                        (Food_ID, Food_Name, Quantity, Expiry_Date, Provider_ID, Provider_Type, Location, Food_Type, Meal_Type)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (food_id, food_name, quantity, expiry, provider_id, provider_type, location, food_type, meal_type)
                    )
                    conn.commit()
                    st.success("✅ Food item added successfully!")
                except sqlite3.IntegrityError:
                    st.error("❌ Food ID already exists.")
                conn.close()

    elif action == "Update":
        st.markdown("Update only: **Quantity**, **Expiry_Date**, **Meal_Type**, or **Food_Type**")
        food_id = st.number_input("Enter Food ID to Update", min_value=1)
        field = st.selectbox("Field to Update", ["Quantity", "Expiry_Date", "Meal_Type", "Food_Type"])
        new_value = st.text_input(f"Enter New Value for {field}")
        if st.button("Update Food"):
            conn = get_connection()
            cursor = conn.cursor()
            query = f"UPDATE food_listings SET {field} = ? WHERE Food_ID = ?"
            cursor.execute(query, (new_value, food_id))
            conn.commit()
            conn.close()
            st.success(f"✅ Food item {food_id} updated.")

    elif action == "Delete":
        food_id = st.number_input("Enter Food ID to Delete", min_value=1)
        if st.button("Delete Food"):
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM food_listings WHERE Food_ID = ?", (food_id,))
            conn.commit()
            conn.close()
            st.success(f"🗑️ Food item {food_id} deleted.")