Dokumentasi Proyek Flask dengan PostgreSQL dan Bootstrap
1.	Pengaturan Awal
•	Install python
•	Buat dan aktifkan virtual evoironment
python -m venv venv		 // untuk linux/mac
venv\Scripts\activate  		// untuk windows
•	Instal dependensi
pip install Flask Flask-SQLAlchemy

2.	Struktur file
project/
|-- app/
|   |-- static/
|   |   |-- style.css
|   |-- templates/
|   |   |-- index.html
|   |   |-- login.html
|   |-- __init__.py
|   |-- models.py
|   |-- routes.py
|-- venv/
|-- config.py
|-- app.py

3.	Setup Database
•	Instal PostgreSQL dan pgAdmin
•	Buat database ‘ha’ di pgAdmin

4.	Konfigurasi Aplikasi
•	Buat file ‘config.py’ untuk menyimpan konfigurasi aplikasi	:
python
  SECRET_KEY = 'your_secret_key'
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:your_password@localhost:5432/ha'

5.	Model Mahasiswa
•	Dalam file `models.py`:
  python
  from flask_sqlalchemy import SQLAlchemy

  db = SQLAlchemy()

  class Mahasiswa(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      nama = db.Column(db.String(100))
      jurusan = db.Column(db.String(50))
      username = db.Column(db.String(50))
      encrypted_password = db.Column(db.LargeBinary)

6.	Setup Aplikasi
•	Dalam file ‘app.py’
python
  from flask import Flask
  from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI
  from flask_sqlalchemy import SQLAlchemy
  from app.routes import mahasiswa_bp

  app = Flask(__name__)
  app.config['SECRET_KEY'] = SECRET_KEY
  app.config['SQLALCHEMY_DATABASE_URI'] SQLALCHEMY_DATABASE_URI
  db = SQLAlchemy(app)

  app.register_blueprint(mahasiswa_bp)

7.	Rute dan Endpoint
•	Dalam file ‘routes.py’ :

from flask import Blueprint, render_template, request, jsonify
  from app.models import db, Mahasiswa
  from sqlalchemy.exc import IntegrityError

  mahasiswa_bp = Blueprint('mahasiswa', __name__)

  @mahasiswa_bp.route('/mahasiswa', methods=['GET'])
  def get_all_mahasiswa():

  @mahasiswa_bp.route('/mahasiswa/<int:mahasiswa_id>', methods=['GET'])
  def get_mahasiswa(mahasiswa_id):

  @mahasiswa_bp.route('/mahasiswa', methods=['POST'])
  def create_mahasiswa():

  @mahasiswa_bp.route('/mahasiswa/<int:mahasiswa_id>', methods=['PUT'])
  def update_mahasiswa(mahasiswa_id):

  @mahasiswa_bp.route('/mahasiswa/<int:mahasiswa_id>', methods=['DELETE'])
  def delete_mahasiswa(mahasiswa_id):
