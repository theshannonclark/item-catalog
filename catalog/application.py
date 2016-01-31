from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Item Catalog"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
