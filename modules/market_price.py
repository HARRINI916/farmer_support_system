import streamlit as st
import pandas as pd

def show_market_price():
    st.header("🧾 சந்தை விலை விவரம்")
    
    # Get user input and remove leading/trailing spaces
    location = st.text_input("உங்கள் இடத்தை உள்ளிடவும் (எ.கா. Chennai):").strip()
    
    if st.button("விலை காண்க"):
        if location == "":
            st.warning("தயவு செய்து ஒரு இடம் உள்ளிடவும்.")
            return
        
        try:
            df = pd.read_csv("data/market_prices.csv")
            
            # Ensure location column is string type and compare in lowercase
            df['location'] = df['location'].astype(str)
            data = df[df["location"].str.lower() == location.lower()]
            
            if not data.empty:
                st.success(f"{location} பகுதியில் கிடைக்கும் சந்தை விலை:")
                st.table(data[["crop", "price_per_kg"]])
            else:
                st.warning("இந்த இடத்திற்கான தரவு இல்லை.")
                
        except FileNotFoundError:
            st.error("தரவு கோப்பு இல்லை. தயவு செய்து data/market_prices.csv சேர்க்கவும்.")
        except Exception as e:
            st.error(f"தெரியாத பிழை ஏற்பட்டது: {e}")
