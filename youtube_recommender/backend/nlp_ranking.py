from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_channels(user_query, channels):
    if not channels or len(channels) < 2:
        return channels  # Return as-is if too few channels

    print(f"🔍 User Query: {user_query}")  # Debugging Step 1

    query_embedding = model.encode(user_query, convert_to_tensor=True)

    ranked_channels = []
    for channel in channels:
        description = channel.get("description", "").strip()
        if not description:
            description = f"{channel['name']} - {channel.get('subscribers', '0')} subscribers, {channel.get('videos', '0')} videos."

        desc_embedding = model.encode(description, convert_to_tensor=True)
        similarity_score = util.pytorch_cos_sim(query_embedding, desc_embedding).cpu().numpy()[0][0]
        
        print(f"🔹 {channel['name']} → Score: {similarity_score:.4f}")  # Debugging Step 2

        similarity_score = (similarity_score + 1) / 2  # Normalize to [0,1]
        subscribers = int(channel.get("subscribers", "0").replace(",", "").replace(".", "")) if channel.get("subscribers") else 0  

        final_score = (0.8 * similarity_score) + (0.2 * (subscribers / 1_000_000))  

        ranked_channels.append((channel, final_score))

    ranked_channels.sort(key=lambda x: x[1], reverse=True)

    print("\n✅ Final Ranked Channels:")
    for i, (channel, score) in enumerate(ranked_channels[:5]):
        print(f"{i+1}. {channel['name']} → Final Score: {score:.4f}")  # Debugging Step 3

    filtered_channels = [channel for channel, score in ranked_channels if score > 0.5]

    return filtered_channels if filtered_channels else ranked_channels[:5]
