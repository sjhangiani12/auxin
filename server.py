from flask import Flask, request
import requests
from waitress import serve
from error import InvalidUsage
import random
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=["GET"])
def ping():
    return "Jarvis, start the engines."

@app.route("/getData", methods=["GET"])
def get_data():
    if not has_args(request.json, ['url']):
      raise InvalidUsage('missing parameters')

    incoming_url = request.json["url"]

    page = requests.get(incoming_url)
    soup = BeautifulSoup(page.content, "html.parser")
    video_url = soup.find("meta", property="og:video:url")['content']
    title = soup.find("meta", property="og:title")['content']
    author = soup.find("meta", property="descript:author")['content']
    return_dict = {"video_url" : video_url, "title" : title, "author" : author}

    return return_dict


if __name__ == "__main__":
    app.run()

# serve(app, host="0.0.0.0", port=3000)

