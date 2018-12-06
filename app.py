
from flask import Flask, render_template
from flask import request
from disp import *
from vectorize import *
app = Flask(__name__,static_url_path="/static")

@app.route("/")

def main():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
	if request.method == "POST":
		t = request.form["text"]
		#getsim(t)
		listoflinks=bfs(t)
		return render_template("index.html",listoflinks=listoflinks)

if __name__ == "__main__":
    app.run()