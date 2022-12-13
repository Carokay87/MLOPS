
#Basic falsk serveur
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/uploader", methods=["POST"])
def uploader():
    f = request.files["file"]
    f.save(f.filename)
    
    

if __name__ == "__main__":
    app.run(debug=True)
    