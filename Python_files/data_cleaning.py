from sqlalchemy import create_engine
import pandas as pd

# Connect to your SQLite DB
engine = create_engine('sqlite:///food_waste.db')

# Load food_listings and fix Expiry_Date
food_listings = pd.read_sql("SELECT * FROM food_listings", engine)
food_listings['Expiry_Date'] = pd.to_datetime(food_listings['Expiry_Date'])

# Load claims and fix Timestamp
claims = pd.read_sql("SELECT * FROM claims", engine)
claims['Timestamp'] = pd.to_datetime(claims['Timestamp'])

# Replace existing tables with cleaned versions
food_listings.to_sql("food_listings", engine, if_exists="replace", index=False)
claims.to_sql("claims", engine, if_exists="replace", index=False)

print("✅ Date columns updated successfully in the database.")
