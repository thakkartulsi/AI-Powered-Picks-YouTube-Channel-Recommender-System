import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/recommend"

st.title("📺 AI Powered Picks - YouTube Channel Recommender")
user_query = st.text_input("Enter what you want to learn (e.g., 'Data Science')")

if st.button("Find Best Channels"):
    response = requests.get(API_URL, params={"query": user_query})

    if response.status_code == 200:
        data = response.json()
        channels = data.get("recommended_channels", [])

        if channels:
            for idx, channel in enumerate(channels, start=1):
                name = channel["name"]
                description = channel["description"]
                url = channel["url"]
                subscribers = channel.get("subscribers", "N/A")
                views = channel.get("views", "N/A")
                videos = channel.get("videos", "N/A")

                st.write(f"""  
🔹 **{idx}. {name}** (📺 {subscribers} subs)  
   📝 {description}  
   📊 {videos} videos, {views} views  
   🔗 [Visit Channel]({url})  
                """)
        else:
            st.warning("No top channels found for this topic.")
    else:
        st.error("Failed to fetch recommendations. Please try again.")
