from flask import Flask, render_template
from flask import request
from disp import *
from vectorize import *
from subjects import *
app = Flask(__name__,static_url_path="/static")

@app.route("/")

def main():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
	if request.method == "POST":
		t = request.form["text"]
		t=t.lower()
		#getsim(t)
		tarr=t.split()
		t=""
		for word in tarr:
			temp=searchterm(word)
			t=t+" "+temp
		t=t[1:]
		print(t)
		listoflinks=bfs(t)
		return render_template("index.html",listoflinks=listoflinks)

if __name__ == "__main__":
    app.run()