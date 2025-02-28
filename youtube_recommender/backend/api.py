from flask import Flask, request, jsonify
from youtube_api import get_top_youtube_channels
from nlp_ranking import rank_channels

app = Flask(__name__)

@app.route("/recommend", methods=["GET"])
def recommend():
    query = request.args.get("query")

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    try:
        # Fetch channels from YouTube API
        channels = get_top_youtube_channels(query)

        if not channels:
            return jsonify({"error": "No popular channels found. Try a different topic."}), 404

        print("Fetched channels:", channels)  # Debugging: Check what YouTube API returns

        # Sort by subscribers (descending)
        channels.sort(key=lambda x: int(x["subscribers"].replace(",", "")), reverse=True)

        # Apply ranking if necessary
        ranked_channels = rank_channels(query, channels) if callable(rank_channels) else channels

        return jsonify({"recommended_channels": ranked_channels})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error. Please try again later."}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
