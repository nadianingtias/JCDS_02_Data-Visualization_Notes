from flask import Flask, redirect, jsonify, render_template, request
app = Flask(__name__)
import mysql.connector as mc

# link to formulir
@app.route('/')
def toIndex():
    return render_template('index.html')

@app.route('/data')
def toData():
    return render_template('data.html')

# redirect ke route yang lain
@app.route('/home')
def toHome():
    return redirect('/')

# method http yang sering dipakai : get, post, put, delete,
# get : ambil data dari server
# post : client setor dari ke server
@app.route('/test', methods=['GET', 'POST'] )
def test():
    if request.method == 'GET':
        return "this is GET"
    elif request.method == 'POST':
        # return "this is POST"
        body = request.json #di postman : body - raw - json
        print(body['kota'])
        return jsonify({
            'status' : 'Data sukses terkirim',
            'name' : body['nama'],
            'city' : body['kota']
        })
        
    else:
        return "this is not both"
dbku = mc.connect(
    host='localhost',
    user = "root",
    passwd = '',
    database = 'test'
)

# READ ALL
@app.route('/db', methods=['GET'])
def getDB():
    if request.method == 'GET':
        c = dbku.cursor()
        c.execute('select * from daftarkaryawan')
        hasil = c.fetchall()
        print(hasil)
        head = ['index','id', 'nama', 'email', 'waktu']
        hasil2 = list(map(lambda a: dict(zip(head,a)), hasil))
        print(hasil2)
        return jsonify(hasil2)

# READ 1
@app.route('/db/<int:id>', methods=['GET', 'POST'])
def getOneDB(id):
    if request.method == 'GET':
        c = dbku.cursor()
        sql = f'select * from daftarkaryawan where id = {id}'
        c.execute(sql)
        hasil = c.fetchall()
        head = ['index','id', 'nama', 'email', 'waktu']
        hasil2 = list(map(lambda a: dict(zip(head,a)), hasil))
        return jsonify(hasil2)

# CREATE 1 via request.json
@app.route('/post/db', methods=['POST'])
def postOneDB():
    if request.method == 'POST':
        body = request.json

        c = dbku.cursor()
        data = (body['nama'], body['email'])
        sql = f'insert into daftarkaryawan (nama, email) values {data}'
        c.execute(sql)
        dbku.commit()
        # hasil = c.fetchall()
        # head = ['index','id', 'nama', 'email', 'waktu']
        # hasil2 = list(map(lambda a: dict(zip(head,a)), hasil))
        return jsonify({
            'status' : "terkirim",
            'nama' : body['nama'],
            'email' : body['email']
        })
        # return 'post'

@app.route('/form/db', methods=['POST'])
def postFormOneDB():
    if request.method == 'POST':
        body = request.form

        c = dbku.cursor()
        data = (body['nama'], body['email'])
        sql = f'insert into daftarkaryawan (nama, email) values {data}'
        c.execute(sql)
        dbku.commit()
        return redirect('/db')

if __name__ == '__main__':
    app.run(debug=True)
    