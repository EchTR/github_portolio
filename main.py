# github.com/echtr

from github import Github
from flask import Flask
from flask import render_template

g = Github("token")
user = g.get_user("user_name")
repos = user.get_repos()

my_repos = sorted([[i.name, i.stargazers_count, i.forks] for i in repos if i.fork == False], key = lambda x: x[1], reverse = True)

app = Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html", my_repos = my_repos)
print(my_repos)

app.run()