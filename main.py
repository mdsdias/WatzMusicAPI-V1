from flask import Flask, render_template, request
from youtubesearchpython import *
import json
app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "docs": [
            {
                "name": "Search Videos",
                "route": "/api/search/videos/< string:Pesquisa >/< int:Pesquisas or default >",
                "desc": "Pesquisas de videos, sendo o <em>Pesquisas</em> o limite, pode-se usar o `default` no lugar de qualquer número",
            },
            {
                "name": "Search Playlists",
                "route": "/api/search/playlists/< string:Pesquisa >/< int:Pesquisas or default >",
                "desc": "Pesquisas de playlists, sendo o <em>Pesquisas</em> o limite, pode-se usar o `default` no lugar de qualquer número",
            }
        ]
    }
    return render_template("docs.html.j2", **data)

@app.route('/api/search/videos/<query>/<limit>')
def youtube_search(query, limit):
    if limit == "default":
        limit = 1
    videosSearch = VideosSearch(query, limit = 1)
    
    return videosSearch.result()

@app.route('/api/search/playlists/<query>/<limit>')
def youtube_search_Playlists(query, limit):
    if limit == "default":
        limit = 1
    else:
        limit = int(limit)
    playlistsSearch = PlaylistsSearch(query, limit)

    return playlistsSearch.result()

@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        """return the information for <user_id>"""
        return 
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        data = request.form 
        return 
    if request.method == 'DELETE':
        """delete user with ID <user_id>"""
        return 
    else:
        # POST Error 405 Method Not Allowed
        return

app.run('0.0.0.0', 9999, debug=True)