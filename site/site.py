from flask import Flask, render_template_string, send_file, redirect, url_for
import subprocess
import time

app = Flask(__name__)
process = None  

HTML_PAGE = '''
    <h1>🎥 Surveillance</h1>
    <form action="/start" method="post"><button type="submit">▶️ Lancer la surveillance</button></form>
    <form action="/stop" method="post"><button type="submit">⏹️ Stop</button></form>
    <br>
    <img src="/image?{{ time }}" width="640">
    <script>
        setInterval(() => {
            document.querySelector('img').src = "/image?" + new Date().getTime();
        }, 1000);
    </script>
'''

@app.route('/')
def index():
    return render_template_string(HTML_PAGE, time=int(time.time()))

@app.route('/image')
def image():
    return send_file("../web.jpg", mimetype='image/jpeg')

@app.route('/start', methods=['POST'])
def start():
    global process
    if process is None:
        process = subprocess.Popen(["python", "cam.py"])
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop():
    global process
    if process is not None:
        process.terminate()
        process = None
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

