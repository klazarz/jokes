from flask import Flask, render_template, request
import requests
import random
import json


app = Flask(__name__)
#CORS(app)

@app.route('/', methods=['GET'])
def home():
    # This is a rest call to get the id for the last joke
    rid = requests.get('https://g7306646445d18e-jokes.adb.eu-amsterdam-1.oraclecloudapps.com/ords/jokes/max_id/')
    maxid = rid.json()
    maxxid = (maxid['items'][0]['max_id']) #here i get the last ID

    id = str(random.randint(1, maxxid))
    r = requests.get(f'https://g7306646445d18e-jokes.adb.eu-amsterdam-1.oraclecloudapps.com/ords/jokes/jokes/{id}',id)
    jr = r.json()

    return render_template('index.html', joke = jr['joke'])

@app.route('/onepun/<int:onepun>', methods=['GET'])
def onepun(onepun):
     # This is a rest call to get the id for the last joke
    rid = requests.get('https://g7306646445d18e-jokes.adb.eu-amsterdam-1.oraclecloudapps.com/ords/jokes/max_id/')
    maxid = rid.json()
    maxxid = (maxid['items'][0]['max_id']) #here i get the last ID

    if onepun>maxxid:
        onepun=maxxid

    id = str(onepun)
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

@app.route('/addjoke/', methods=['GET','POST'])
def addjoke():
    if request.method == 'POST':
        # This is a rest call to get the id for the last joke
        rid = requests.get('https://g7306646445d18e-jokes.adb.eu-amsterdam-1.oraclecloudapps.com/ords/jokes/max_id/')
        maxid = rid.json()
        maxxid = (maxid['items'][0]['max_id']) + 1 #here i get the last ID
        baseurl="https://g7306646445d18e-jokes.adb.eu-amsterdam-1.oraclecloudapps.com/ords/jokes/jokes/"

        if request.form is not None:
            joke = request.form.get('content')
            data = {
                "id": maxxid,
                 "joke": joke
                    }
            r = requests.post(url=baseurl, data=data)
            # print(r)
            # print(r.text)
        else:
            pass

    return render_template('addjoke.html')

if __name__ == '__main__':
   app.run(debug = True)