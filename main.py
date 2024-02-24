from flask import Flask, request, render_template, send_file
from pytube import YouTube, Playlist
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    youtube_url = request.form['url']
    file_type = request.form['file_type']
    download_method = request.form['download_method']
    
    
    if download_method == 'link':
        yt = YouTube(youtube_url)
        if file_type == 'video':
            yt.streams.get_highest_resolution().download(os.path.join(os.path.expanduser("~"), "Downloads"))
        elif file_type == 'audio':
            yt.streams.filter(only_audio=True).first().download(os.path.join(os.path.expanduser("~"), "Downloads"))
    elif download_method == 'playlist':
        playlist = Playlist(youtube_url)
        for video in playlist.video_urls:
            yt = YouTube(video)
            if file_type == 'video':
                yt.streams.get_highest_resolution().download(os.path.join(os.path.expanduser("~"), "Downloads"))
            elif file_type == 'audio':
                yt.streams.filter(only_audio=True).first().download(os.path.join(os.path.expanduser("~"), "Downloads"))
    

    return "File DownLoad in Download Folder"

if __name__ == '__main__':
    app.run(debug=True)
