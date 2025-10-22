from flask import Flask, render_template
app = Flask(__name__, template_folder="templates", static_folder='static')

@app.route('/')
def hello():
    # Hardcode the prefix for now (replace with your actual subpath if it changes)
    proxy_prefix = '/proxy/7857'
    return render_template('index.html', static_prefix=proxy_prefix)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7857, debug=True)