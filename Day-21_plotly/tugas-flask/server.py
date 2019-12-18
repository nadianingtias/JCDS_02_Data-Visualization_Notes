from flask import Flask, render_template, jsonify, abort
import requests
from bs4 import BeautifulSoup as bs 

server = Flask(__name__)

pokeList = [
    {
        'id':1,
        'name': "pikachu",
        'power' : 100
    },
    {
        'id':2,
        'name': "pikaboo",
        'power' : 78
    },
    {
        'id':3,
        'name': "pikasha",
        'power' : 89
    }
]
url = "http://digidb.io/digimon-list/"
dataDigimon = requests.get(url).content
dataDigi = bs(dataDigimon,'html.parser')

# print(dataDigi)
def scrapDigimon():
    counter = 0
    dataDigitoCSV = []
    temList = []
    header = []
    for i in dataDigi.find_all('th'):
        cek = str(i.text)
        header.append(cek)

    for i in dataDigi.find_all('td'):
    #     print(counter)
        cek = str(i.text)
            
        print(cek, end = ' ')
        if cek[0]== ' ': print('y')
        
        temList.append(cek.replace('\xa0', '')) # replace some noise character
    #     temList.append(cek)
        counter += 1
        # get each row by counting the column. end the nCols is 13
        if (counter%13==0):
            dataDigitoCSV.append(temList)
            temList =[]
            print()
            counter = 0
    return dataDigitoCSV, header

# home route
@server.route('/')
def home():
    return  render_template('index.html',
            data = pokeList,
            pikachu = pokeList
    )



@server.route('/digimon')
def routeDigimon():
    myDigi, header = scrapDigimon()
    for i in myDigi:
        print(i)
    return render_template('digi.html',
        data = myDigi,
        headers = header
    )

def makeDictionary(head, lisOfLis):
    dictList = []
    for i in lisOfLis:
        temDict = dict(zip(head, i))
        dictList.append(temDict)
    return dictList

@server.route('/digimon/json')
def routeDigimonJson():
    myDigi, header = scrapDigimon()
    dictList = makeDictionary(header, myDigi)
    return jsonify(dictList)

@server.route('/digimon/json/<int:id>')
def routeDigimonJsonOne(id):
    myDigi, header = scrapDigimon()
    if (id-1) > len(myDigi) or (id-1)<1:
        abort(404)
    else:
        return jsonify(myDigi[id-1])

if __name__ == '__main__':
    server.run(
        debug=True

    )