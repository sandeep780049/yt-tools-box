
from flask import Flask, render_template, request
import re
import os
import random

app = Flask(__name__)

# Helper: Extract video ID from YouTube URL
def extract_video_id(url):
    video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
    return video_id_match.group(1) if video_id_match else None

# Route: Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route: Thumbnail Downloader
@app.route('/thumbnail', methods=['GET', 'POST'])
def thumbnail():
    thumbnail_url = None
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = extract_video_id(video_url)
        if video_id:
            thumbnail_url = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
    return render_template('thumbnail.html', thumbnail_url=thumbnail_url)

# Route: AI-Based Tags Generator
@app.route('/tags', methods=['GET', 'POST'])
def tags():
    ai_tags = []
    if request.method == 'POST':
        video_url = request.form['video_url']
        sample_tags = ["trending", "viral", "YouTube", "subscribe", "funny", "2025", "AI", "explained", "how-to", "beginner"]
        random.shuffle(sample_tags)
        ai_tags = sample_tags[:10]
    return render_template('tags.html', tags=ai_tags)

# Route: AI Title & Description Generator
@app.route('/ai', methods=['GET', 'POST'])
def ai():
    titles, description = [], ""
    if request.method == 'POST':
        topic = request.form['video_topic']
        titles = [f"{topic} - Explained in 2 Minutes!", f"Top 5 Facts About {topic}", f"Why {topic} is Important!", f"{topic} Secrets Revealed!", f"{topic}: Everything You Need to Know", f"{topic} Full Tutorial", f"How {topic} Changed the World", f"Boost Your Channel with {topic}", f"Is {topic} Worth It?", f"{topic} - The Truth You Didn’t Know"]
        description = f"This video explains everything you need to know about {topic}. It's perfect for beginners and experts alike. Watch till the end to fully understand {topic} and how it impacts your life!"
    return render_template('ai.html', titles=titles, description=description)

# Route: Keywords Generator
@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    keywords = []
    if request.method == 'POST':
        topic = request.form['video_topic']
        base_keywords = [topic, f"{topic} 2025", f"best {topic}", f"how to {topic}", f"{topic} tutorial", f"{topic} in hindi", f"latest {topic}", f"top {topic} tips"]
        extra = ["growth", "viral", "shorts", "new", "expert", "strategy", "2025", "views", "tips", "guide", "learn", "trending", "hack"]
        keywords = base_keywords + random.sample(extra, 10)
    return render_template('keywords.html', keywords=keywords)

# No if __name__ == "__main__": block – Ready for Render deployment
