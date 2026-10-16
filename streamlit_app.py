import streamlit as st
import requests

API_URL = 'https://cali-house-pred-app-434951853629.us-east1.run.app/predict'

st.set_page_config(page_title="California House Price Predictor", page_icon="🏠", layout="centered")

with st.sidebar:
    st.title("About")
    st.write(
        "Predicts the **median house value** of a California neighborhood (census block group) "
        "using the 1990 California Housing dataset."
    )
    st.caption("Values are from 1990 census data, so prices are far below today's market.")

st.title("🏠 California House Price Predictor")
st.markdown("Describe a neighborhood, then click **Predict**. Hover over the **?** to see what each input means.")

col1, col2 = st.columns(2)

with col1:
    med_inc = st.slider(
        "Median income (×$10,000)", 0.5, 15.0, 3.9, 0.1,
        help="Median household income in the neighborhood. 3.9 means about $39,000.")
    house_age = st.slider(
        "House age (years)", 1, 52, 29,
        help="Median age of the houses in the neighborhood.")
    ave_rooms = st.slider(
        "Average rooms (rooms per household)", 1.0, 15.0, 5.4, 0.1,
        help="Average number of rooms per household.")
    ave_bedrms = st.slider(
        "Average bedrooms (bedrooms per household)", 0.5, 5.0, 1.1, 0.1,
        help="Average number of bedrooms per household.")

with col2:
    population = st.slider(
        "Population (people)", 3, 10000, 1400, 10,
        help="Number of people living in the neighborhood.")
    ave_occup = st.slider(
        "Average occupancy (people per household)", 1.0, 10.0, 3.0, 0.1,
        help="Average number of people per household.")
    latitude = st.slider(
        "Latitude (degrees north)", 32.5, 42.0, 34.2, 0.01,
        help="How far north. San Diego is about 32.7, San Francisco about 37.8.")
    longitude = st.slider(
        "Longitude (degrees east)", -124.5, -114.0, -118.5, 0.01,
        help="Negative numbers are west of Greenwich. Los Angeles is about -118.2.")

st.write("---")

if st.button("Predict", type="primary"):
    payload = {
        'med_inc': med_inc,
        'house_age': house_age,
        'ave_rooms': ave_rooms,
        'ave_bedrms': ave_bedrms,
        'population': population,
        'ave_occup': ave_occup,
        'latitude': latitude,
        'longitude': longitude,
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        if response.status_code == 200:
            price = response.json()['prediction']
            st.metric("Predicted median house value", f"${price:,.0f}")
        else:
            st.error(f"Server Error: {response.status_code}")
    except requests.exceptions.RequestException:
        st.error("Connection Error: Could not reach the prediction service.")
