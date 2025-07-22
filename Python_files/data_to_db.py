import pandas as pd
from sqlalchemy import create_engine

# Connect to the SQLite DB
engine = create_engine('sqlite:///food_waste.db')

# Load CSV files
providers = pd.read_csv('data/providers_data.csv')
receivers = pd.read_csv('data/receivers_data.csv')
food_listings = pd.read_csv('data/food_listings_data.csv')
claims = pd.read_csv('data/claims_data.csv')

# Save to DB
providers.to_sql('providers', con=engine, if_exists='replace', index=False)
receivers.to_sql('receivers', con=engine, if_exists='replace', index=False)
food_listings.to_sql('food_listings', con=engine, if_exists='replace', index=False)
claims.to_sql('claims', con=engine, if_exists='replace', index=False)

print("✅ All CSV data has been inserted into the database.")
