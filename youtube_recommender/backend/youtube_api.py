import requests
import config  # Store API key in config.py

YOUTUBE_API_KEY = config.YOUTUBE_API_KEY  
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
CHANNEL_URL = "https://www.googleapis.com/youtube/v3/channels"

def get_top_youtube_channels(query, max_results=5):
    """Fetch the most popular YouTube channels for a given query, prioritizing high-subscriber channels."""
    
    params = {
        "part": "snippet",
        "q": query,
        "type": "channel",
        "maxResults": 15,  # Fetch more results to filter later
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(SEARCH_URL, params=params)
    if response.status_code != 200:
        print("Error fetching channels:", response.text)  # Debugging output
        return []

    data = response.json()
    channel_ids = [item["id"]["channelId"] for item in data.get("items", [])]

    if not channel_ids:
        return []

    # Fetch detailed statistics
    stats_params = {
        "part": "snippet,statistics",
        "id": ",".join(channel_ids),
        "key": YOUTUBE_API_KEY
    }

    stats_response = requests.get(CHANNEL_URL, params=stats_params)
    if stats_response.status_code != 200:
        print("Error fetching channel stats:", stats_response.text)  # Debugging output
        return []

    stats_data = stats_response.json()

    top_channels = []
    for item in stats_data.get("items", []):
        channel_id = item["id"]
        snippet = item["snippet"]
        stats = item["statistics"]

        channel_name = snippet["title"]
        channel_desc = snippet["description"]
        channel_url = f"https://www.youtube.com/channel/{channel_id}"
        subscribers = int(stats.get("subscriberCount", 0))
        views = int(stats.get("viewCount", 0))
        videos = int(stats.get("videoCount", 0))

        # Debugging: Print fetched channel info
        print(f"Fetched: {channel_name} | Subs: {subscribers} | Views: {views} | Videos: {videos}")

        # Filter out channels with low subscribers (e.g., under 100K)
        if subscribers >= 100000:
            top_channels.append({
                "name": channel_name,
                "description": channel_desc,
                "url": channel_url,
                "subscribers": f"{subscribers:,}",  # Format with commas
                "views": f"{views:,}",
                "videos": f"{videos:,}"
            })

    # Sort by subscriber count (highest first)
    top_channels.sort(key=lambda x: int(x["subscribers"].replace(",", "")), reverse=True)

    # Return only the top N popular channels
    return top_channels[:max_results]
