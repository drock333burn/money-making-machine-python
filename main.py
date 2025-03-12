import streamlit as st
import random
import time
import requests

st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="wide")

st.sidebar.title("💡 Navigation")
page = st.sidebar.radio("Go to:", ["💰 Money Generator", "🌟 Motivational Quotes"])

def fetchQuoteApi():
    try:
        response = requests.get("https://dummyjson.com/quotes")
        if response.status_code == 200:
            quotes = response.json()            
            return random.choice(quotes['quotes'])["quote"]
        else:
            return("No Quotes Found")
    except:
        return("Something went wrong")

def generateMoney():
    return random.randint(1, 1000)

if page == "💰 Money Generator":
    st.title("💰 Money Making Machine 💰")
    st.subheader("Generate Instant Cash!")

    if st.button("💸 Generate Money", use_container_width=True):
        with st.spinner("Counting your money..."):
            time.sleep(3)
            amount = generateMoney()
            st.success(f"🎉 You made ${amount}")

elif page == "🌟 Motivational Quotes":
    st.title("🌟 Get Inspired!")
    st.subheader("Generate a Motivational Quote")

    if st.button("📜 Generate Quote", use_container_width=True):
        with st.spinner("Fetching an inspiring quote..."):
            time.sleep(3)
            quote = fetchQuoteApi()
            st.success(quote)
