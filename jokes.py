from lxml import html
import requests
import random
from flask import Flask, render_template
import pandas as pd

def get_joke():
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})

    # Jokes list 1
    URL = 'https://ponly.com/funny-puns/'
    page = requests.get(URL, headers=HEADERS)
    tree = html.fromstring(page.content)
    elements = tree.xpath('//*[@id="smooth-content"]/main/div[1]/div[3]/div/p[position()>6]/text()')


    # Jokes list 2 (German)
    URL = 'https://www.thepioneerwoman.com/home-lifestyle/a35617884/best-dad-jokes/'
    page = requests.get(URL, headers=HEADERS)
    tree = html.fromstring(page.content)
    elements2 = tree.xpath('//*[@id="main-content"]/div[2]/div[3]/ul[1]/li[position()>=1]/text()')

    # Jokes list 3
    URL = 'https://www.rd.com/article/dad-joke-tweets/'
    page = requests.get(URL, headers=HEADERS)
    tree = html.fromstring(page.content)
    elements3 = tree.xpath('//*[@id="content"]/div[2]/div[2]/div[1]/div[6]/ul[1]/li[position()>=1]/text()')

    # Jokes list 4
    URL = 'https://www.goodhousekeeping.com/life/parenting/a36279135/best-corny-dad-jokes-for-kids/'
    page = requests.get(URL, headers=HEADERS)
    tree = html.fromstring(page.content)
    elements4 = tree.xpath('//*[@id="main-content"]/div[2]/div[3]/ul[1]/li[position()>=1]/text()')

    # Jokes list 5
    URL = 'https://www.harryanddavid.com/blog/best-dad-jokes/'
    page = requests.get(URL, headers=HEADERS)
    tree = html.fromstring(page.content)
    elements5 = tree.xpath('//*[@id="post-49508"]/div/div/article/div[2]/ol[position()>=1]/li[position()>=1]/text()')

    # Jokes list 6
    URL = 'https://www.thepresentfinder.co.uk/blog/60-bad-dad-jokes_73891843.htm'
    page = requests.get(URL, headers=HEADERS)
    tree = html.fromstring(page.content)
    elements6 = tree.xpath('//*[@id="a73891843"]/div/p[position()>=2]/text()')

    # Merging & Messaging
    allelements = elements
    allelements.extend(elements2)
    allelements.extend(elements3)
    allelements.extend(elements4)
    allelements.extend(elements5)
    allelements.extend(elements6)

    #print(len(allelements))

    #Remove dead bodies
    for e in allelements:
        if len(e) < 3:
            allelements.remove(e)


    element = random.choice(allelements)

    return element

get_joke()

app = Flask(__name__, template_folder='templates', static_folder='static')

app = Flask(__name__)

@app.route("/")
def dailyjoke():
    return render_template('index.html', joke = get_joke())


if __name__ == '__main__':
    #get_joke()
    app.run(host='0.0.0.0')
