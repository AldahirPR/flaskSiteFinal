from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	return redirect(redirect_index())

@app.route("/about_me")
def about_me():
	return render_template("about.html")
	return redirect(redirect_index())

@app.route("/contact")
def contact():
	return render_template("contact.html")
	return redirect(redirect_index())

@app.route("/randomF")
def randomF():
	return render_template("randomF.html")
	return redirect(redirect_index())


if __name__ == "__main__":
	app.run(debug=True)