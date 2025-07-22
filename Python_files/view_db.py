import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///food_waste.db')

# Example query to see what's inside
df = pd.read_sql("SELECT * FROM providers LIMIT 5", engine)
print(df)
