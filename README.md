NAMA KELOMPOK : 1. Ade Kurnia Budiman
                2. Ahmad Bisyral Hafi
                3. Ahmad Munazar
                4. Aldi Yahya Awaluddin

Noted : Dikerjakan oleh 
        1. Ade Kurnia Budiman
        2. Ahmad Bisyral Hafi
              

```markdown
# Aplikasi Mahasiswa Flask

Aplikasi sederhana menggunakan Flask dan SQLAlchemy untuk manajemen data mahasiswa.

## Instalasi

1. Clone repositori:

    ```bash
    git clone https://github.com/username/repo.git
    cd repo
    ```

2. Instal dependensi:

    ```bash
    pip install -r requirements.txt
    ```

3. Konfigurasi database: (sesuaikan `SQLALCHEMY_DATABASE_URI` di `app.py`)

4. Jalankan aplikasi:

    ```bash
    python app.py
    ```

## Fitur

### Manajemen Mahasiswa

1. **Get All Mahasiswa:** Mendapatkan daftar semua mahasiswa.

    ```http
    GET /mahasiswa
    ```

2. **Get Mahasiswa by ID:** Mendapatkan informasi mahasiswa berdasarkan ID.

    ```http
    GET /mahasiswa/<int:mahasiswa_id>
    ```

3. **Create Mahasiswa:** Menambahkan mahasiswa baru.

    ```http
    POST /mahasiswa
    ```

    Request Body:

    ```json
    {
        "nama": "Nama Mahasiswa",
        "jurusan": "Jurusan Mahasiswa"
    }
    ```

4. **Update Mahasiswa:** Memperbarui informasi mahasiswa berdasarkan ID.

    ```http
    PUT /mahasiswa/<int:mahasiswa_id>
    ```

    Request Body:

    ```json
    {
        "nama": "Nama Mahasiswa Baru",
        "jurusan": "Jurusan Mahasiswa Baru"
    }
    ```

5. **Delete Mahasiswa:** Menghapus mahasiswa berdasarkan ID.

    ```http
    DELETE /mahasiswa/<int:mahasiswa_id>
    ```

### Fitur Baru - Manajemen Log

Aplikasi ini telah diperbarui untuk mencatat log aktivitas ke dalam file. File log dapat disesuaikan dengan mengganti nama file dan format log.

### Konfigurasi Log

1. **Nama File Log:** Ganti 'app.log' dengan nama file log yang diinginkan di `app.py`.

    ```python
    logging_handler = logging.FileHandler('app.log')
    ```

2. **Format Log Pesan:** Sesuaikan format pesan log di `app.py`.

    ```python
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ```
```
