# TrashCash ♻️💰

**Ubah Sampah Jadi Rupiah!**

TrashCash adalah aplikasi web inovatif yang dirancang untuk menjembatani masyarakat yang memiliki barang rongsokan/daur ulang dengan pengepul atau pabrik daur ulang. Tujuan kami adalah memberdayakan masyarakat, terutama dari kalangan bawah, untuk mendapatkan penghasilan tambahan sekaligus berkontribusi pada lingkungan yang lebih bersih melalui ekonomi sirkular.

## ✨ Fitur Utama (Versi Hackathon MVP)

* **Untuk Penjual:**
    * Pendaftaran & Login yang mudah.
    * Membuat listing barang rongsokan (misalnya kardus, botol plastik, kertas, logam) dengan informasi material dan lokasi (pilih di peta).
    * Melihat status listing yang telah dibuat.
    * **(Fitur Bonus dengan AI ✨)** Jika memilih material "Lainnya", dapatkan bantuan deskripsi otomatis dari AI (menggunakan Gemini API) untuk listing Anda.
* **Untuk Pembeli (Pengepul/Pabrik):**
    * Pendaftaran & Login.
    * Menjelajahi listing barang rongsokan yang tersedia di sekitar lokasi mereka melalui tampilan peta interaktif.
    * Menyatakan minat pada listing tertentu.
    * Melihat riwayat interaksi dengan listing.
    * **(Fitur Bonus dengan AI ✨)** Dapatkan ide pemanfaatan material dari listing yang dilihat melalui Gemini API.

## 🚀 Teknologi yang Digunakan

* **Frontend:** HTML, Tailwind CSS, JavaScript (Vanilla JS dengan ES6 Modules)
* **Backend:** Flask (Python)
* **Database:** Firestore (Firebase)
* **Autentikasi:** Firebase Authentication
* **Peta:** Google Maps JavaScript API
* **AI Generatif:** Gemini API (untuk deskripsi otomatis dan ide pemanfaatan material)

## 🔧 Cara Menjalankan Proyek (Lokal)

1.  **Prasyarat:**
    * Python 3.x
    * pip (Python package installer)
    * Akun Firebase & Akun Google Cloud Platform (untuk API Key Google Maps & Gemini)

2.  **Setup:**
    * Clone repositori ini:
        ```bash
        git clone [URL_REPO_ANDA_NANTI]
        cd trashcash 
        ```
    * Buat dan aktifkan virtual environment (opsional tapi direkomendasikan):
        ```bash
        python -m venv venv
        source venv/bin/activate  # Pada Windows: venv\Scripts\activate
        ```
    * Install dependensi Flask:
        ```bash
        pip install Flask
        ```
    * **Konfigurasi Firebase & Google Maps:**
        * Pastikan Anda telah membuat proyek Firebase dan mengaktifkan Firestore serta Authentication (Email/Password).
        * Dapatkan konfigurasi Firebase Anda dan API Key Google Maps.
        * Untuk API Key Gemini, jika menggunakan model `gemini-2.0-flash` melalui platform seperti Google AI Studio atau Vertex AI, pastikan key Anda valid. (Dalam kode hackathon ini, API key Gemini di-placeholder untuk diisi oleh platform Canvas).
        * Masukkan API Key Google Maps Anda di file `app.py` pada variabel `Maps_API_KEY`.
        * Masukkan konfigurasi Firebase Anda di dalam file `templates/app_shell.html` pada objek `firebaseConfig`.

3.  **Menjalankan Aplikasi:**
    ```bash
    python app.py
    ```
    Aplikasi akan berjalan di `http://127.0.0.1:5001`.

## 🤝 Kontribusi

Saat ini proyek ini adalah hasil dari pengembangan cepat (hackathon). Jika Anda tertarik untuk berkontribusi, silakan buat *issue* atau *pull request*.

## 💡 Visi ke Depan

* Integrasi pembayaran dalam aplikasi.
* Sistem rating dan review untuk penjual dan pembeli.
* Fitur notifikasi real-time.
* Gamifikasi untuk mendorong partisipasi.
* Analitik dampak lingkungan.

---

Terima kasih telah mengunjungi TrashCash!
