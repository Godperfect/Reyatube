from flask import Flask, render_template, jsonify, request
import requests
import json

app = Flask(__name__)

# YouTube API Key
API_KEY = 'AIzaSyD_GdN9HZUBz18I8Wk_XKb_OUJScW1jkqw'  # Replace with your API Key

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML file

@app.route('/search', methods=['GET'])
def search_videos():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    # Call YouTube API to search for videos
    api_url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={API_KEY}'
    response = requests.get(api_url)

    if response.status_code == 200:
        videos = response.json().get('items', [])
        video_data = []

        for video in videos:
            video_info = {
                'title': video['snippet']['title'],
                'description': video['snippet']['description'],
                'thumbnail': video['snippet']['thumbnails']['medium']['url'],
                'video_id': video['id'].get('videoId')
            }
            video_data.append(video_info)

        return jsonify(video_data)
    else:
        return jsonify({"error": "Error fetching video data from YouTube API"}), 500

@app.route('/download', methods=['GET'])
def download_video():
    video_id = request.args.get('video_id')
    file_type = request.args.get('type')  # 'audio' or 'video'

    if not video_id or not file_type:
        return jsonify({"error": "Missing video_id or type"}), 400

    download_url = None

    if file_type == 'audio':
        download_url = f'https://www.youtube.com/audio/{video_id}/high_quality'
    elif file_type == 'video':
        download_url = f'https://www.youtube.com/video/{video_id}/high_quality'

    if download_url:
        return jsonify({"download_url": download_url})
    else:
        return jsonify({"error": "Invalid file type"}), 400


if __name__ == '__main__':
    app.run(debug=True)
