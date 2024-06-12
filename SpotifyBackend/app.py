from flask import Flask, request, redirect, session, jsonify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_COOKIE_NAME'] = 'spotify-session'

# Spotify API credentials
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

scope = "user-top-read"
sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                        client_secret=SPOTIPY_CLIENT_SECRET,
                        redirect_uri=SPOTIPY_REDIRECT_URI,
                        scope=scope)

@app.route('/')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect('/stats')

def get_token():
    token_info = session.get('token_info', None)
    if not token_info:
        raise Exception("Token not found")
    
    now = datetime.now()
    is_expired = token_info['expires_at'] - now.timestamp() < 60
    if is_expired:
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info

@app.route('/stats')
def stats():
    token_info = get_token()
    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    time_range = request.args.get('time_range', 'medium_term')
    data_type = request.args.get('data_type', 'tracks')
    
    if data_type == 'artists':
        top_data = sp.current_user_top_artists(limit=10, time_range=time_range)
    else:
        top_data = sp.current_user_top_tracks(limit=10, time_range=time_range)
        
    return jsonify(top_data['items'])

@app.route('/stats/artists')
def stats_artists():
    return get_stats('artists')

@app.route('/stats/tracks')
def stats_tracks():
    return get_stats('tracks')

def get_stats(data_type):
    token_info = get_token()
    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    time_ranges = ['short_term', 'medium_term', 'long_term']
    stats = {}

    for time_range in time_ranges:
        if data_type == 'artists':
            top_data = sp.current_user_top_artists(limit=10, time_range=time_range)
        else:
            top_data = sp.current_user_top_tracks(limit=10, time_range=time_range)
        
        stats[time_range] = top_data['items']
    
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
