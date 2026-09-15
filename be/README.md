# 🎓 CariKampus Backend API — Tutorial & Dokumentasi Lengkap

Dokumentasi arsitektur, panduan pembuatan step-by-step, dan panduan deployment untuk Backend API **CariKampus** berbasis **FastAPI**, **SQLAlchemy 2.0**, **PostgreSQL**, dan **Alembic**.

---

## 📑 Daftar Isi
1. [Ringkasan & Tech Stack](#-ringkasan--tech-stack)
2. [Arsitektur Proyek](#-arsitektur-proyek)
3. [Panduan Pembuatan & Penjelasan Kode](#-panduan-pembuatan--penjelasan-kode)
   - [1. Konfigurasi Lingkungan (`app/core/config.py`)](#1-konfigurasi-lingkungan)
   - [2. Database Engine & Session (`app/db/session.py`)](#2-database-engine--session)
   - [3. Database Models (`app/models/`)](#3-database-models)
   - [4. Pydantic Schemas (`app/schemas/`)](#4-pydantic-schemas)
   - [5. Repository Pattern (`app/repositories/`)](#5-repository-pattern)
   - [6. Service Layer (`app/services/`)](#6-service-layer)
   - [7. API Router & Endpoints (`app/api/v1/`)](#7-api-router--endpoints)
   - [8. Inisialisasi Aplikasi (`app/main.py`)](#8-inisialisasi-aplikasi)
   - [9. Migrasi Database dengan Alembic](#9-migrasi-database-dengan-alembic)
   - [10. Seeding Data Awal (`scripts/seed.py`)](#10-seeding-data-awal)
4. [Menjalankan di Lokal (Development Setup)](#-menjalankan-di-lokal-development-setup)
5. [Panduan Deployment ke Server Produksi](#-panduan-deployment-ke-server-produksi)
   - [Metode 1: Deploy ke AWS EC2 + RDS (Nginx + Systemd + SSL Certbot)](#metode-1-deploy-ke-aws-ec2--rds-rekomendasi-produksi)
   - [Metode 2: Deploy Menggunakan Docker & Docker Compose](#metode-2-deploy-menggunakan-docker--docker-compose)
   - [Metode 3: Deploy ke Cloud PaaS (Render / Railway / Koyeb)](#metode-3-deploy-ke-cloud-paas-render--railway)
6. [Daftar Endpoint API](#-daftar-endpoint-api)

---

## 🚀 Ringkasan & Tech Stack

- **Framework Web**: [FastAPI](https://fastapi.tiangolo.com/) (asinkron, performa tinggi, auto-dokumentasi Swagger/OpenAPI)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **ORM (Object-Relational Mapping)**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/)
- **Database Driver**: [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) (PostgreSQL)
- **Migrasi Skema**: [Alembic](https://alembic.sqlalchemy.org/)
- **Validasi & Serialization**: [Pydantic v2](https://docs.pydantic.dev/) & [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

---

## 🏛 Arsitektur Proyek

Aplikasi ini menggunakan **Layered Architecture (Clean Architecture)** dengan pemisahan tanggung jawab (*Separation of Concerns*) yang jelas:

```
be/
├── alembic.ini                  # Konfigurasi Alembic Migration
├── requirements.txt             # Dependensi Python
├── Dockerfile                   # Konfigurasi kontainer Docker
├── docker-compose.yml           # Orkestrasi Docker (App + DB)
├── .env.example                 # Contoh file environment
├── scripts/
│   └── seed.py                  # Script populasi data kampus & jurusan
└── app/
    ├── main.py                  # Entrypoint FastAPI & CORS setup
    ├── core/
    │   └── config.py            # Pydantic Settings (.env loader)
    ├── db/
    │   ├── base.py              # DeclarativeBase SQLAlchemy
    │   ├── session.py           # Engine & get_db session generator
    │   └── migrations/          # File migrasi Alembic
    ├── models/                  # Tabel Database (SQLAlchemy ORM)
    │   ├── campus.py
    │   ├── faculty.py
    │   └── major.py
    ├── schemas/                 # Data Transfer Objects (Pydantic models)
    │   ├── campus.py
    │   ├── faculty.py
    │   ├── major.py
    │   └── common.py
    ├── repositories/            # Layer Query Database murni
    │   └── campus.py
    ├── services/                # Layer Business Logic
    │   └── campus.py
    ├── api/
    │   └── v1/
    │       ├── router.py        # Agregasi route v1
    │       └── endpoints/       # Route handlers
    │           ├── campuses.py
    │           └── health.py
    └── dependencies/
        └── db.py                # Dependency injection get_db
```

### Keuntungan Struktur Ini:
1. **Controller / Endpoint** hanya menangani validasi request HTTP, status code, dan serialisasi response.
2. **Service Layer** menangani aturan bisnis (kalkulasi paginasi, validasi data unik, aggregasi).
3. **Repository Layer** memisahkan query ORM/SQL sehingga mudah diuji (*unit testing*) dan dimodifikasi tanpa mengganggu logika bisnis.

---

## 🛠 Panduan Pembuatan & Penjelasan Kode

### 1. Konfigurasi Lingkungan
File: `app/core/config.py`
Menggunakan `pydantic-settings` agar variabel konfigurasi di-validasi secara *type-safe* dari file `.env`:
```python
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "CariKampus"
    APP_ENV: str = "development"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = ""
    FRONTEND_URLS: str = "http://localhost:3000,http://127.0.0.1:3000"

    @property
    def cors_origins(self) -> List[str]:
        if not self.FRONTEND_URLS:
            return ["*"]
        return [url.strip() for url in self.FRONTEND_URLS.split(",") if url.strip()]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

settings = Settings()
```

### 2. Database Engine & Session
File: `app/db/session.py`
Menyediakan session database menggunakan generator pattern untuk Dependency Injection:
```python
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

engine = None
SessionLocal = None

if settings.DATABASE_URL:
    engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session, None, None]:
    if SessionLocal is None:
        raise RuntimeError("DATABASE_URL is not configured in environment or settings.")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 3. Database Models
File: `app/models/campus.py`, `faculty.py`, `major.py`
Memodelkan hierarki relasi antar entitas:
- **Campus** memiliki banyak **Faculty** dan **Major** (`relationship(..., cascade="all, delete-orphan")`).
- **Faculty** berada di bawah **Campus** dan memiliki banyak **Major**.
- **Major** terhubung ke **Campus** dan opsional ke **Faculty**.

### 4. Pydantic Schemas
File: `app/schemas/campus.py`, `common.py`
- `CampusListItem`: Payload ringan untuk listing kampus pada halaman katalog (nama, logo, jenis, akreditasi, jumlah jurusan).
- `CampusDetailResponse`: Payload lengkap dengan relasi fakultas & jurusan untuk halaman detail kampus.
- `PaginatedResponse[T]`: Skema generik untuk respons berhalaman (`items`, `total`, `page`, `limit`, `total_pages`).

### 5. Repository Pattern
File: `app/repositories/campus.py`
Mengoptimalkan query database dengan `selectinload` untuk menghindari masalah *N+1 Query*:
```python
def get_by_slug(self, db: Session, slug: str) -> Optional[Campus]:
    return (
        db.query(Campus)
        .options(
            selectinload(Campus.faculties).selectinload(Faculty.majors),
            selectinload(Campus.majors),
        )
        .filter(Campus.slug == slug)
        .first()
    )
```
Mendukung pencarian multi-kolom (`ilike`), filter akreditasi, kota, dan tipe kampus.

### 6. Service Layer
File: `app/services/campus.py`
Menghitung offset paginasi, kalkulasi `total_pages` menggunakan `math.ceil()`, dan mengembalikan exception HTTP 404 jika slug kampus tidak ditemukan:
```python
def get_by_slug(self, db: Session, slug: str) -> CampusDetailResponse:
    campus = campus_repository.get_by_slug(db, slug)
    if not campus:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Kampus dengan slug '{slug}' tidak ditemukan.",
        )
    return CampusDetailResponse.model_validate(campus)
```

### 7. API Router & Endpoints
File: `app/api/v1/endpoints/campuses.py`
Menyediakan endpoint RESTful:
- `GET /api/v1/campuses` (dengan query params `page`, `limit`, `search`, `type`, `accreditation`, `city`, `province`)
- `GET /api/v1/campuses/{slug}`
- `GET /api/v1/health`

### 8. Inisialisasi Aplikasi
File: `app/main.py`
Menggabungkan router v1, mendaftarkan middleware CORS dinamis, dan menambahkan root health route.

### 9. Migrasi Database dengan Alembic
File: `alembic.ini` dan `app/db/migrations/env.py`
Alembic dikonfigurasi untuk membaca model `Base.metadata` dan membaca `DATABASE_URL` langsung dari konfigurasi aplikasi (`app.core.config.settings`).

### 10. Seeding Data Awal
File: `scripts/seed.py`
Memasukkan data universitas terkemuka di Indonesia (UI, ITB, UGM, ITS, Undip, Unpad, IPB, Telkom University, Binus, dll.) beserta fakultas, jurusan, daya tampung, akreditasi, dan rentang biaya kuliah.

---

## 💻 Menjalankan di Lokal (Development Setup)

### 1. Buat dan Aktifkan Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependensi
```bash
pip install -r requirements.txt
```

### 3. Konfigurasi `.env`
Salin template `.env.example` ke `.env`:
```bash
cp .env.example .env
```
Sesuaikan isi `.env`:
```env
APP_NAME=CariKampus
APP_ENV=development
DATABASE_URL=postgresql://postgres:password@localhost:5432/carikampus
FRONTEND_URLS=http://localhost:3000,http://127.0.0.1:3000
```
> **Catatan**: Jika menggunakan cloud PostgreSQL gratis seperti **Neon** (`neon.tech`), cukup tempel connection string dari dashboard Neon dengan parameter `?sslmode=require`.

### 4. Eksekusi Migrasi Database
```bash
alembic upgrade head
```

### 5. Jalankan Seed Data Kampus
```bash
python scripts/seed.py
```

### 6. Jalankan Server Development
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
Buka browser:
- API Root: `http://localhost:8000/`
- Dokumentasi Interaktif (Swagger UI): `http://localhost:8000/docs`
- Dokumentasi Alternatif (ReDoc): `http://localhost:8000/redoc`

---

## 🌐 Panduan Deployment ke Server Produksi

---

### Metode 1: Deploy ke AWS EC2 + RDS (Rekomendasi Produksi)

Arsitektur produksi standar menggunakan **AWS EC2 (Ubuntu 22.04 / 24.04 LTS)** untuk aplikasi FastAPI, dan **AWS RDS PostgreSQL** (atau Neon DB) sebagai basis data terkelola.

```
Internet (Port 80/443 HTTPS)
           │
           ▼
     [AWS EC2]
         ├── Nginx (Reverse Proxy & SSL Let's Encrypt)
         └── Systemd Daemon ──> Uvicorn (FastAPI Port 8000)
                                      │
                                      ▼
                             [AWS RDS PostgreSQL]
```

#### Langkah 1: Akses EC2 Instance via SSH
Gunakan file private key yang ada pada repositori (`carikampus-key.pem`):
```bash
# Set permission file key (khusus Linux/Mac/WSL)
chmod 400 aws/carikampus-key.pem

# Login ke instance EC2
ssh -i aws/carikampus-key.pem ubuntu@<IP_PUBLIK_EC2>
```

#### Langkah 2: Setup Server Linux (Update & Instalasi Tools)
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv git nginx libpq-dev certbot python3-certbot-nginx
```

#### Langkah 3: Clone Project & Setup Virtual Environment
```bash
cd /var/www
sudo git clone <URL_REPOSITORY_GIT> carikampus
sudo chown -R ubuntu:ubuntu /var/www/carikampus
cd /var/www/carikampus/be

# Buat virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn
```

#### Langkah 4: Buat File `.env` Produksi
```bash
nano .env
```
Isi dengan konfigurasi produksi:
```env
APP_NAME=CariKampus
APP_ENV=production
DATABASE_URL=postgresql://postgres:<PASSWORD_RDS>@<RDS_ENDPOINT>:5432/<DB_NAME>
FRONTEND_URLS=https://domain-frontend-anda.com,https://www.domain-frontend-anda.com
```

#### Langkah 5: Jalankan Migrasi & Seeding
```bash
alembic upgrade head
python scripts/seed.py
```

#### Langkah 6: Konfigurasi Service Daemon (Systemd)
Buat file service agar FastAPI berjalan di latar belakang dan restart otomatis bila server mati:
```bash
sudo nano /etc/systemd/system/carikampus.service
```
Isi konfigurasi berikut:
```ini
[Unit]
Description=Gunicorn/Uvicorn Daemon for CariKampus FastAPI
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/carikampus/be
EnvironmentFile=/var/www/carikampus/be/.env
ExecStart=/var/www/carikampus/be/.venv/bin/gunicorn app.main:app \
          --workers 3 \
          --worker-class uvicorn.workers.UvicornWorker \
          --bind 127.0.0.1:8000 \
          --access-logfile /var/log/carikampus_access.log \
          --error-logfile /var/log/carikampus_error.log

Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

Aktifkan dan jalankan service:
```bash
sudo systemctl daemon-reload
sudo systemctl start carikampus
sudo systemctl enable carikampus

# Cek status service
sudo systemctl status carikampus
```

#### Langkah 7: Konfigurasi Nginx Reverse Proxy
Buat file konfigurasi virtual host Nginx:
```bash
sudo nano /etc/nginx/sites-available/carikampus
```
Isi konfigurasi:
```nginx
server {
    listen 80;
    server_name api.domain-anda.com; # Atau IP Publik EC2

    client_max_body_size 20M;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Aktifkan konfigurasi dan restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/carikampus /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Langkah 8: Pasang SSL HTTPS Gratis (Certbot Let's Encrypt)
Jika sudah menggunakan nama domain:
```bash
sudo certbot --nginx -d api.domain-anda.com
```

---

### Metode 2: Deploy Menggunakan Docker & Docker Compose

Jika server sudah memiliki Docker & Docker Compose:

#### 1. Jalankan Container (App + PostgreSQL)
```bash
docker compose up -d --build
```
Container akan secara otomatis:
1. Membangun image Python 3.11-slim.
2. Menjalankan container PostgreSQL 15.
3. Menunggu database siap (*healthcheck*).
4. Menjalankan `alembic upgrade head`.
5. Menjalankan script seeding data `python scripts/seed.py`.
6. Menjalankan FastAPI di port `8000`.

#### 2. Cek Log Container
```bash
docker compose logs -f api
```

#### 3. Menghentikan Container
```bash
docker compose down
```

---

### Metode 3: Deploy ke Cloud PaaS (Render / Railway)

Untuk deployment tanpa konfigurasi server Linux manual:

#### Opsi A: Render.com
1. Buat akun di [Render.com](https://render.com).
2. Buat **PostgreSQL Database** di Render (atau gunakan [Neon.tech](https://neon.tech)).
3. Buat **New Web Service** dan hubungkan repositori Git Anda.
4. Tentukan konfigurasi:
   - **Root Directory**: `be`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt && alembic upgrade head && python scripts/seed.py`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Tambahkan **Environment Variables**:
   - `DATABASE_URL`: Connection string PostgreSQL Anda.
   - `APP_ENV`: `production`
   - `FRONTEND_URLS`: URL frontend Vercel/Netlify Anda.

#### Opsi B: Railway.app
1. Buat project baru di [Railway.app](https://railway.app).
2. Tambahkan layanan **PostgreSQL**.
3. Hubungkan repositori Git untuk direktori `be`.
4. Railway akan otomatis mendeteksi `Dockerfile` yang telah disediakan.
5. Hubungkan variabel `DATABASE_URL` dari database PostgreSQL Railway.

---

## 📡 Daftar Endpoint API

| Method | Endpoint | Deskripsi | Parameter Query |
|---|---|---|---|
| `GET` | `/` | Status API Root | - |
| `GET` | `/api/v1/health` | Health Check status | - |
| `GET` | `/api/v1/campuses` | Katalog daftar kampus (paginated) | `page`, `limit`, `search`, `type`, `accreditation`, `city`, `province` |
| `GET` | `/api/v1/campuses/{slug}` | Detail informasi kampus, fakultas & jurusan | `slug` (path) |

### Contoh Request: Filter Kampus PTN Akreditasi Unggul di Jawa Barat
```http
GET /api/v1/campuses?type=PTN&accreditation=Unggul&province=Jawa%20Barat&page=1&limit=10 HTTP/1.1
Host: localhost:8000
```

### Contoh Response:
```json
{
  "items": [
    {
      "id": 1,
      "name": "Universitas Indonesia",
      "short_name": "UI",
      "slug": "universitas-indonesia",
      "type": "PTN",
      "accreditation": "Unggul",
      "city": "Depok",
      "province": "Jawa Barat",
      "logo_url": "https://upload.wikimedia.org/wikipedia/id/thumb/8/87/Makara_UI.svg/800px-Makara_UI.svg.png",
      "ranking_national": 1,
      "majors_count": 2
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 10,
  "total_pages": 1
}
```
