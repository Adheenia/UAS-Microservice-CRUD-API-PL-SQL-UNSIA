from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging
from flask_logging import Logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:demauye0911@localhost:5432/ha'
db = SQLAlchemy(app)


logging_handler = logging.FileHandler('app.log') 
logging_handler.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logging_handler.setFormatter(log_formatter)

app.logger.addHandler(logging_handler)

log = Logging(app)

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    jurusan = db.Column(db.String(50))
    username = db.Column(db.String(50))
    encrypted_password = db.Column(db.LargeBinary)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mahasiswa', methods=['GET'])
def get_all_mahasiswa():
    mahasiswa_list = Mahasiswa.query.all()
    mahasiswa_data = [{'id': mahasiswa.id, 'nama': mahasiswa.nama, 'jurusan': mahasiswa.jurusan} for mahasiswa in mahasiswa_list]
    return jsonify({'mahasiswa': mahasiswa_data})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return 'Login successful!'
        else:
            return 'Login failed. Please check your username and password.'

    return render_template('login.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


@app.route('/mahasiswa/<int:mahasiswa_id>', methods=['GET'])
def get_mahasiswa(mahasiswa_id):
    mahasiswa = Mahasiswa.query.get(mahasiswa_id)
    if mahasiswa:
        return jsonify({'id': mahasiswa.id, 'nama': mahasiswa.nama, 'jurusan': mahasiswa.jurusan})
    return jsonify({'message': 'Mahasiswa not found'}), 404

@app.route('/mahasiswa', methods=['POST'])
def create_mahasiswa():
    data = request.get_json()
    new_mahasiswa = Mahasiswa(nama=data['nama'], jurusan=data['jurusan'])
    db.session.add(new_mahasiswa)
    db.session.commit()
    return jsonify({'message': 'Mahasiswa created successfully'}), 201

@app.route('/mahasiswa/<int:mahasiswa_id>', methods=['PUT'])
def update_mahasiswa(mahasiswa_id):
    mahasiswa = Mahasiswa.query.get(mahasiswa_id)
    if not mahasiswa:
        return jsonify({'message': 'Mahasiswa not found'}), 404

    data = request.get_json()
    mahasiswa.nama = data['nama']
    mahasiswa.jurusan = data['jurusan']

    try:
        db.session.commit()
        return jsonify({'message': 'Mahasiswa updated successfully'})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Username already exists'}), 409

@app.route('/mahasiswa/<int:mahasiswa_id>', methods=['DELETE'])
def delete_mahasiswa(mahasiswa_id):
    mahasiswa = Mahasiswa.query.get(mahasiswa_id)
    if not mahasiswa:
        return jsonify({'message': 'Mahasiswa not found'}), 404

    db.session.delete(mahasiswa)
    db.session.commit()
    return jsonify({'message': 'Mahasiswa deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

