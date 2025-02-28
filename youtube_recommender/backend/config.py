import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# YouTube API Key (Replace with your actual API key)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# YouTube API Base URL
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search"

# Number of channels to return
TOP_N_CHANNELS = 3

# Default search parameters
YOUTUBE_SEARCH_PARAMS = {
    "part": "snippet",
    "type": "channel",
    "maxResults": 10,  # Fetch more results to process ranking later
}

# NLP Model Configuration
NLP_MODEL = {
    "name": "all-MiniLM-L6-v2",  # Sentence Transformer Model
    "similarity_threshold": 0.75  # Threshold for relevance scoring
}

# Logging Configuration
LOGGING = {
    "level": "INFO",
    "format": "%(asctime)s - %(levelname)s - %(message)s",
}

# Print settings for debugging
if __name__ == "__main__":
    print(f"YOUTUBE_API_KEY: {YOUTUBE_API_KEY}")
    print(f"YOUTUBE_API_URL: {YOUTUBE_API_URL}")
    print(f"TOP_N_CHANNELS: {TOP_N_CHANNELS}")
    print(f"NLP_MODEL: {NLP_MODEL}")
