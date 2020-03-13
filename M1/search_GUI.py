from flask import Flask, request, render_template
import os
from search import search_query

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

####### ROUTES #############
@app.route("/",methods =["GET","POST"])
def index():
	if request.method == "POST":
		text = request.form['text']
		print("TEXT = ", text)
        urls = search_query(text)
		### PASS QUERY INTO MAIN HERE, then pass results INTO FUNC BELOW
		return render_template("results.html",query = text, result = urls)
	return render_template("search.html")


if __name__ == "__main__":
	app.debug = True
	app.run()