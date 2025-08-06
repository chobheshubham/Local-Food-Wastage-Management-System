# 🍽️ Local Food Wastage Management System

A community-focused platform built with **Python**, **SQL**, and **Streamlit** that connects food donors (restaurants, households, etc.) with receivers (NGOs, individuals) to reduce food waste and enhance food accessibility.

---

## 🧠 Project Overview

This system allows users to:
- List surplus food for donation.
- Claim available food by NGOs or individuals.
- View and analyze food donations, claims, and trends.
- Filter food listings by provider, location, type, and meal.
- Manage and track food listings using a user-friendly interface.

---

## 📊 Key Features

- 🔍 **Food Listings Dashboard**: View all available food items, filter by city, type, or meal.
- 🧾 **Claims Analysis**: See who’s claiming food, most donated items, and top meal types.
- 📇 **Contacts View**: Get contact details of food providers and receivers.
- ⚙️ **Manage Listings**: Perform CRUD operations (Add, Update, Delete food records).
- 📈 **SQL-Driven Insights**: Data retrieved and analyzed using powerful SQL queries.

---

## 🛠️ Tech Stack

| Tool | Description |
|------|-------------|
| 🐍 Python | Main programming language |
| 🧮 SQL (SQLite) | Backend database for food, claims, providers |
| 📊 Streamlit | Web interface for visualizing and interacting |
| 🧠 Pandas | Data handling and transformation |
| 🧵 SQLAlchemy | SQL engine for Python-DB connection |

---

## 📁 Project Structure

📦 project-root/\
├── app.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;             # Main Streamlit app interface\
├── queries.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         # SQL queries to fetch data from database\
├── food_waste.db &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      # SQLite database storing all core data\
├── views/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            # Streamlit view files (summary, listings, contacts, etc.)\
├── data/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;              # (Optional) CSV dataset files for providers, receivers, etc.\
└── README.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          # Project documentation

---

## 📂 Datasets Used

- **providers_data.csv** – Information about food donors.
- **receivers_data.csv** – NGOs/individuals receiving food.
- **food_listings_data.csv** – Food items available for claim.
- **claims_data.csv** – Claimed food records.

---

## ❓ SQL-Based Questions Answered

The app answers 15+ real-world questions using SQL, such as:
- Which cities have the most providers and receivers?
- Who are the top food donors?
- What meal types are most claimed?
- What is the claim status distribution?
- Who has the most successful claims?
- What is the average food quantity claimed per receiver?

All queries are implemented in [`queries.py`](queries.py) and visualized in the Streamlit app.

---

## 🚀 How to Run Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/chobheshubham/Local-Food-Wastage-Management-System.git
   cd Local-Food-Wastage-Management-System

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py

## ✅ Outcomes
- A live dashboard showcasing food donation and claim activity.
- SQL insights on food distribution, demand trends, and wastage reduction.
- Scalable architecture ready for cloud deployment or NGO partnerships.

## 🙌 Contributions & Feedback
Have suggestions or want to contribute? Feel free to open issues or pull requests!

## 👨‍💻 Developed By
Shubham Chobhe
🌐 [GitHub Profile](https://github.com/chobheshubham)
