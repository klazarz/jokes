from flask import Flask, render_template
# from flask_restful import Resource, Api
# from flask_cors import CORS
import requests
import random
# from requests.exceptions import HTTPError
# import json

app = Flask(__name__)
#CORS(app)

@app.route('/', methods=['GET'])
def home():
    id = str(random.randint(1, 463))
    r = requests.get(f'https://g7306646445d18e-jokes.adb.eu-amsterdam-1.oraclecloudapps.com/ords/jokes/jokes/{id}',id)
    jr = r.json()

    return render_template('index.html', joke = jr['joke'])

if __name__ == '__main__':
   app.run(debug = True)