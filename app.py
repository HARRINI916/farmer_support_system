import streamlit as st
from modules import market_price, crop_recommendation, query_system

st.title("🚜 விவசாயி ஆதரவு அமைப்பு")

option = st.sidebar.selectbox(
    "தேர்வு செய்யவும்:",
    ["சந்தை விலை", "பயிர் பரிந்துரை", "விவசாயி கேள்வி"]
)

if option == "சந்தை விலை":
    market_price.show_market_price()
elif option == "பயிர் பரிந்துரை":
    crop_recommendation.suggest_crops()
elif option == "விவசாயி கேள்வி":
    query_system.farmer_query()
