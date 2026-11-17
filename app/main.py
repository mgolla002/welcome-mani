from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
	return "Welcome mani"


def run():
	app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
	run()
