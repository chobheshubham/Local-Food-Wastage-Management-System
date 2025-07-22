# db_setup.py
from sqlalchemy import create_engine, Table, Column, Integer, String, Date, MetaData, ForeignKey, DateTime
import pandas as pd

engine = create_engine('sqlite:///food_waste.db')
meta = MetaData()

providers = Table(
    'providers', meta,
    Column('Provider_ID', Integer, primary_key=True),
    Column('Name', String),
    Column('Type', String),
    Column('Address', String),
    Column('City', String),
    Column('Contact', String)
)

receivers = Table(
    'receivers', meta,
    Column('Receiver_ID', Integer, primary_key=True),
    Column('Name', String),
    Column('Type', String),
    Column('City', String),
    Column('Contact', String)
)

food_listings = Table(
    'food_listings', meta,
    Column('Food_ID', Integer, primary_key=True),
    Column('Food_Name', String),
    Column('Quantity', Integer),
    Column('Expiry_Date', Date),
    Column('Provider_ID', Integer, ForeignKey('providers.Provider_ID')),
    Column('Provider_Type', String),
    Column('Location', String),
    Column('Food_Type', String),
    Column('Meal_Type', String)
)

claims = Table(
    'claims', meta,
    Column('Claim_ID', Integer, primary_key=True),
    Column('Food_ID', Integer, ForeignKey('food_listings.Food_ID')),
    Column('Receiver_ID', Integer, ForeignKey('receivers.Receiver_ID')),
    Column('Status', String),
    Column('Timestamp', DateTime)
)

meta.create_all(engine)
