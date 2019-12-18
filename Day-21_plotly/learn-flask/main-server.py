from flask import Flask, render_template, jsonify, abort, send_from_directory

server = Flask(__name__)

# home route
@server.route('/')
def home():
    return "<h1> Halo my world, my name is Nadia</h1>"

#render HTML
@server.route('/html')
def html():
    return render_template('index.html')

@server.route('/data')
def data():
    nama="Andi"
    # kota = "Jakarta"
    usia = 22
    return render_template(
        'data.html', # ini adalah file html yang dirender dalam route /data
        data ={'name' : nama, 'age' : usia} # ini adalah variabel dict yang bisa diakses di file HTML 
        ) 

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

@server.route('/pokemon')
def retrieve_pokemon():
    return jsonify(pokeList)

# Dynamic Route : pokemon/1
@server.route('/pokemon/<int:id>') #<format:namavariabel>
def retrieve_pokemon_one(id):
    if (id-1) > len(pokeList) or (id-1)<1:
        abort(404)
    else:
        return jsonify(pokeList[id-1])

# route untuk error 404
@server.errorhandler(404)
def notFound():
    return render_template('eror.html')

# route untuk mengakses gambar dari direkori storage
@server.route('/file/<path:namaFile>')
def myFile(namaFile): 
    return send_from_directory('storage', namaFile)

if __name__ == '__main__':
    server.run(debug=True)

# tugas
# buat biodata (cv) html => server Flask
# - home
# - about
# - education
# - skills
# - experience

# buat file flask, scrapping data dari digimon
# /table => buat custom html untuk menampilkan data digimon
# /JSON => JSON