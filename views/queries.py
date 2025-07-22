# queries.py
import pandas as pd
from sqlalchemy import create_engine

# Connect to your SQLite database
engine = create_engine('sqlite:///food_waste.db')

# 1. Number of providers and receivers in each city
def get_providers_receivers_by_city():
    query = """
    SELECT City, 
           COUNT(DISTINCT Provider_ID) AS Providers, 
           (SELECT COUNT(*) FROM receivers r WHERE r.City = p.City) AS Receivers
    FROM providers p
    GROUP BY City
    """
    return pd.read_sql(query, engine)

# 2. Type of provider contributing most food
def get_top_provider_type():
    query = """
    SELECT Provider_Type, COUNT(*) AS Total 
    FROM food_listings 
    GROUP BY Provider_Type 
    ORDER BY Total DESC
    """
    return pd.read_sql(query, engine)

# 3. Contact info of providers in a city
def get_providers_by_city(city):
    query = f"""
    SELECT Name, Type, Contact 
    FROM providers 
    WHERE City = '{city}'
    """
    return pd.read_sql(query, engine)

# 4. Receivers who claimed the most food
def get_top_receivers():
    query = """
    SELECT r.Name, COUNT(c.Claim_ID) AS Total_Claims
    FROM claims c
    JOIN receivers r ON c.Receiver_ID = r.Receiver_ID
    GROUP BY r.Name
    ORDER BY Total_Claims DESC
    LIMIT 5
    """
    return pd.read_sql(query, engine)

# 5. Total quantity of food available
def get_total_food_quantity():
    query = "SELECT SUM(Quantity) AS Total_Quantity FROM food_listings"
    return pd.read_sql(query, engine)

# 6. City with highest food listings
def get_top_city_by_listings():
    query = """
    SELECT Location AS City, COUNT(*) AS Listings 
    FROM food_listings 
    GROUP BY Location 
    ORDER BY Listings DESC
    """
    return pd.read_sql(query, engine)

# 7. Most commonly available food types
def get_common_food_types():
    query = """
    SELECT Food_Type, COUNT(*) AS Count 
    FROM food_listings 
    GROUP BY Food_Type 
    ORDER BY Count DESC
    """
    return pd.read_sql(query, engine)

# 8. Number of claims per food item
def get_claims_per_food():
    query = """
    SELECT f.Food_Name, COUNT(c.Claim_ID) AS Claims
    FROM claims c
    JOIN food_listings f ON c.Food_ID = f.Food_ID
    GROUP BY f.Food_Name
    ORDER BY Claims DESC
    """
    return pd.read_sql(query, engine)

# 9. Provider with highest successful claims
def get_top_provider_by_claims():
    query = """
    SELECT p.Name, COUNT(c.Claim_ID) AS Successful_Claims
    FROM claims c
    JOIN food_listings f ON c.Food_ID = f.Food_ID
    JOIN providers p ON f.Provider_ID = p.Provider_ID
    WHERE c.Status = 'Completed'
    GROUP BY p.Name
    ORDER BY Successful_Claims DESC
    LIMIT 5
    """
    return pd.read_sql(query, engine)

# 10. Status distribution of claims
def get_claim_status_distribution():
    query = """
    SELECT Status, COUNT(*) AS Count 
    FROM claims 
    GROUP BY Status
    """
    return pd.read_sql(query, engine)

# 11. Avg quantity of food claimed per receiver
def get_avg_claim_quantity():
    query = """
    SELECT r.Name, AVG(f.Quantity) AS Avg_Quantity
    FROM claims c
    JOIN food_listings f ON c.Food_ID = f.Food_ID
    JOIN receivers r ON c.Receiver_ID = r.Receiver_ID
    GROUP BY r.Name
    ORDER BY Avg_Quantity DESC
    LIMIT 10
    """
    return pd.read_sql(query, engine)

# 12. Most claimed meal type
def get_top_meal_type():
    query = """
    SELECT Meal_Type, COUNT(*) AS Total_Claims
    FROM claims c
    JOIN food_listings f ON c.Food_ID = f.Food_ID
    GROUP BY Meal_Type
    ORDER BY Total_Claims DESC
    """
    return pd.read_sql(query, engine)

# 13. Total quantity of food donated by provider
def get_quantity_by_provider():
    query = """
    SELECT p.Name, SUM(f.Quantity) AS Total_Quantity
    FROM food_listings f
    JOIN providers p ON f.Provider_ID = p.Provider_ID
    GROUP BY p.Name
    ORDER BY Total_Quantity DESC
    """
    return pd.read_sql(query, engine)
