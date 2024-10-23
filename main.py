
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    images = [
        {"image": "image1.jpg", "caption": "Image 1"},
        {"image": "image2.jpg", "caption": "Image 2"},
        {"image": "image3.jpg", "caption": "Image 3"},
    ]
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run()
