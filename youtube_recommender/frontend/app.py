import streamlit as st
import requests

# Set a red background color, white text color, black placeholder and button text using div
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(45deg, #000000, #8B0000, #5A0000, #330000);
            color: white;  /* White text color for overall app */
        }

        /* Change all text color to white */
        div {
            color: white !important;
        }

        /* Set the input text color to white */
        .stTextInput input {
            color: black !important;
            background-color: rgba(255, 255, 255, 0.2) !important;
        }

        /* Style for button text, background color to light red, text color to white, and center the button */
        .stButton button {
            color: white !important; /* Set button text color to white */
            background-color: #5A0000 !important; /* Light red background */
            border: none !important; /* Remove button border */
            text-align: center;
            display: block; /* Make the button a block-level element */
            margin-left: auto; /* Center the button horizontally */
            margin-right: auto; /* Center the button horizontally */
        }

        /* Hover effect for button */
        .stButton button:hover {
            background-color: #8B0000 !important; /* Darker red on hover */
        }
        
        /* Optional: Shine effect (subtle reflection) */
        .stApp::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, rgba(255,255,255,0.2) 10%, rgba(255,255,255,0) 50%);
            pointer-events: none;
            opacity: 0.1;
            animation: shine 3s infinite;
        }

        @keyframes shine {
            0% { left: -100%; }
            50% { left: 100%; }
            100% { left: -100%; }
        }

        /* Center the title and subtitle */
        .center-title {
            text-align: center;
            margin: 0; /* Remove margin */
            padding: 0; /* Remove padding */
        }

        /* Title font size */
        .stTitle {
            font-size: 30px !important;
            font-weight: bold;
        }

        /* Add margin top to the text input */
        .stTextInput {
            margin-top: 30px !important;
        }

        /* Increase the font size of the label */
        .stTextInput label {
            font-size: 18px !important; /* Increase font size for label */
        }

    </style>
    """,
    unsafe_allow_html=True,
)

# Centered title and subtitle
st.markdown(
    "<h1 class='center-title' style='font-size: 30px; color: white;'>📺 AI-Powered Picks - YouTube Channel Recommender</h1>",
    unsafe_allow_html=True
)

# API URL for recommendations
API_URL = "http://127.0.0.1:5000/recommend"

# Title and user input for any topic search with updated label
user_query = st.text_input("Search for topics (e.g., 'Data Science', 'Cooking', 'Fitness') to get top YouTube channels")

# If the button is clicked
if st.button("Find Best Channels"):
    if user_query:  # Check if the user has entered a query
        response = requests.get(API_URL, params={"query": user_query})

        if response.status_code == 200:
            data = response.json()
            channels = data.get("recommended_channels", [])

            if channels:
                st.write(f"**Recommended channels for '{user_query}'**:")
                for idx, channel in enumerate(channels, start=1):
                    name = channel["name"]
                    description = channel["description"]
                    url = channel["url"]
                    subscribers = channel.get("subscribers", "N/A")
                    views = channel.get("views", "N/A")
                    videos = channel.get("videos", "N/A")

                    # Use HTML to set text color to white
                    st.markdown(f"""
                        <p style="color:white;">
                            🔹 {idx}. {name} (📺 {subscribers} subs)<br>
                            📝 {description}<br>
                            📊 {videos} videos, {views} views<br>
                            🔗 <a href="{url}" style="color:white;" target="_blank">Visit Channel</a>
                        </p>
                    """, unsafe_allow_html=True)

            else:
                st.warning(f"No top channels found for the topic '{user_query}'.")
        else:
            st.error("Failed to fetch recommendations. Please try again.")
    else:
        st.warning("Please enter a topic to search for YouTube channels.")
