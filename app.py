from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    try:
        youtube = YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        mensagem = "Download concluído!"
    except Exception as e:
        mensagem = "Ocorreu um erro durante o download: " + str(e)

    return render_template('resultado.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run()


