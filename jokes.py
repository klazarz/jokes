from flask import Flask, render_template
import requests
import random
import json


app = Flask(__name__)
#CORS(app)

@app.route('/', methods=['GET'])
def home():
    id = str(random.randint(1, 463))
    r = requests.get(f'https://g7306646445d18e-jokes.adb.eu-amsterdam-1.oraclecloudapps.com/ords/jokes/jokes/{id}',id)
    jr = r.json()

    return render_template('index.html', joke = jr['joke'])

@app.route('/all', methods=['GET'])
def all():
    baseurl = 'https://g7306646445d18e-jokes.adb.eu-amsterdam-1.oraclecloudapps.com/ords/jokes/jokes/'
    endpoint = '?offset='
    offset = 0

    r = requests.get(baseurl + endpoint +str(offset))

    jr = r.json()

    if jr['hasMore']:
        nextoffset = 25 + int(jr['offset'])

    prevoffset = 0

    return render_template('all.html', html_page_text = jr, nextoffset=nextoffset, prevoffset = prevoffset)

@app.route('/all/<int:offset>', methods=['GET'])
def offset(offset):
    baseurl = 'https://g7306646445d18e-jokes.adb.eu-amsterdam-1.oraclecloudapps.com/ords/jokes/jokes/'
    endpoint = '?offset='
    offset = offset

    r = requests.get(baseurl + endpoint +str(offset))

    print(baseurl + endpoint +str(offset))

    jr = r.json()

    if jr['hasMore']:
        nextoffset = 25 + int(jr['offset'])
    else:
        nextoffset = 0

    if jr['offset'] > 0:
        prevoffset = offset - 25
    else:
        prevoffset = 0


    return render_template('all.html', html_page_text = jr, nextoffset=nextoffset, prevoffset=prevoffset)


if __name__ == '__main__':
   app.run(debug = True)