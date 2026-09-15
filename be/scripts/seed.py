import sys
from pathlib import Path

# Ensure backend root is in sys.path
BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.db.session import SessionLocal
from app.models.campus import Campus
from app.models.faculty import Faculty
from app.models.major import Major


CAMPUSES_DATA = [
    {
        "name": "Universitas Indonesia",
        "short_name": "UI",
        "slug": "universitas-indonesia",
        "type": "PTN",
        "accreditation": "Unggul",
        "city": "Depok",
        "province": "Jawa Barat",
        "address": "Jl. Margonda Raya, Pondok Cina, Kecamatan Beji, Kota Depok, Jawa Barat 16424",
        "website": "https://www.ui.ac.id",
        "logo_url": "https://upload.wikimedia.org/wikipedia/id/thumb/8/87/Makara_UI.svg/800px-Makara_UI.svg.png",
        "banner_url": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=1200&q=80",
        "description": "Universitas Indonesia adalah salah satu perguruan tinggi negeri tertua dan paling bergengsi di Indonesia dengan kampus hijau di Depok dan Salemba.",
        "ranking_national": 1,
        "faculties": [
            {
                "name": "Fakultas Ilmu Komputer (Fasilkom)",
                "slug": "fasilkom-ui",
                "majors": [
                    {
                        "name": "Ilmu Komputer",
                        "slug": "ilmu-komputer-ui",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 150,
                        "tuition_min": 0,
                        "tuition_max": 15000000,
                        "career_prospects": "Software Engineer, Data Scientist, Machine Learning Engineer, Security Analyst",
                    },
                    {
                        "name": "Sistem Informasi",
                        "slug": "sistem-informasi-ui",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 120,
                        "tuition_min": 0,
                        "tuition_max": 15000000,
                        "career_prospects": "IT Consultant, Product Manager, Business Analyst, Enterprise Architect",
                    },
                ],
            },
            {
                "name": "Fakultas Kedokteran (FK)",
                "slug": "fk-ui",
                "majors": [
                    {
                        "name": "Pendidikan Dokter",
                        "slug": "pendidikan-dokter-ui",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 250,
                        "tuition_min": 0,
                        "tuition_max": 20000000,
                        "career_prospects": "Dokter Umum, Dokter Spesialis, Peneliti Klinis, Konsultan Medis",
                    },
                ],
            },
            {
                "name": "Fakultas Ekonomi dan Bisnis (FEB)",
                "slug": "feb-ui",
                "majors": [
                    {
                        "name": "Manajemen",
                        "slug": "manajemen-ui",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 200,
                        "tuition_min": 0,
                        "tuition_max": 15000000,
                        "career_prospects": "Business Strategist, Marketing Manager, Operations Manager",
                    },
                    {
                        "name": "Akuntansi",
                        "slug": "akuntansi-ui",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 200,
                        "tuition_min": 0,
                        "tuition_max": 15000000,
                        "career_prospects": "Auditor Publik, Konsultan Pajak, Financial Analyst, CFO",
                    },
                ],
            },
        ],
    },
    {
        "name": "Institut Teknologi Bandung",
        "short_name": "ITB",
        "slug": "institut-teknologi-bandung",
        "type": "PTN",
        "accreditation": "Unggul",
        "city": "Bandung",
        "province": "Jawa Barat",
        "address": "Jl. Ganesa No.10, Lb. Siliwangi, Kecamatan Coblong, Kota Bandung, Jawa Barat 40132",
        "website": "https://www.itb.ac.id",
        "logo_url": "https://upload.wikimedia.org/wikipedia/id/thumb/9/95/Ganesha_ITB.svg/800px-Ganesha_ITB.svg.png",
        "banner_url": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1200&q=80",
        "description": "Institut Teknologi Bandung adalah perguruan tinggi teknik pertama di Indonesia yang berdedikasi menghasilkan lulusan berkualitas dunia di bidang sains dan teknologi.",
        "ranking_national": 2,
        "faculties": [
            {
                "name": "Sekolah Teknik Elektro dan Informatika (STEI)",
                "slug": "stei-itb",
                "majors": [
                    {
                        "name": "Teknik Informatika",
                        "slug": "teknik-informatika-itb",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 180,
                        "tuition_min": 0,
                        "tuition_max": 14500000,
                        "career_prospects": "Software Architect, Cloud Engineer, AI Specialist, Tech Lead",
                    },
                    {
                        "name": "Sistem dan Teknologi Informasi",
                        "slug": "sti-itb",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 100,
                        "tuition_min": 0,
                        "tuition_max": 14500000,
                        "career_prospects": "IT Solution Architect, Information Security Analyst, IT Project Manager",
                    },
                    {
                        "name": "Teknik Elektro",
                        "slug": "teknik-elektro-itb",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 120,
                        "tuition_min": 0,
                        "tuition_max": 14500000,
                        "career_prospects": "Hardware Engineer, Embedded System Engineer, Telecom Specialist",
                    },
                ],
            },
            {
                "name": "Fakultas Teknologi Industri (FTI)",
                "slug": "fti-itb",
                "majors": [
                    {
                        "name": "Teknik Industri",
                        "slug": "teknik-industri-itb",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 160,
                        "tuition_min": 0,
                        "tuition_max": 14500000,
                        "career_prospects": "Supply Chain Specialist, Operations Planner, Industrial Consultant",
                    },
                ],
            },
        ],
    },
    {
        "name": "Universitas Gadjah Mada",
        "short_name": "UGM",
        "slug": "universitas-gadjah-mada",
        "type": "PTN",
        "accreditation": "Unggul",
        "city": "Sleman",
        "province": "D.I. Yogyakarta",
        "address": "Bulaksumur, Caturtunggal, Kec. Depok, Kabupaten Sleman, Daerah Istimewa Yogyakarta 55281",
        "website": "https://www.ugm.ac.id",
        "logo_url": "https://upload.wikimedia.org/wikipedia/id/thumb/e/e0/Emblem_of_Universitas_Gadjah_Mada.svg/800px-Emblem_of_Universitas_Gadjah_Mada.svg.png",
        "banner_url": "https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=1200&q=80",
        "description": "Universitas Gadjah Mada adalah universitas kerakyatan terbesar di Indonesia yang menjunjung tinggi kebudayaan dan keilmuan nasional.",
        "ranking_national": 3,
        "faculties": [
            {
                "name": "Fakultas MIPA",
                "slug": "fmipa-ugm",
                "majors": [
                    {
                        "name": "Ilmu Komputer",
                        "slug": "ilmu-komputer-ugm",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 90,
                        "tuition_min": 0,
                        "tuition_max": 12000000,
                        "career_prospects": "Fullstack Developer, Data Scientist, Researcher",
                    },
                    {
                        "name": "Statistika",
                        "slug": "statistika-ugm",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 90,
                        "tuition_min": 0,
                        "tuition_max": 12000000,
                        "career_prospects": "Aktuaris, Data Analyst, Quantitative Researcher",
                    },
                ],
            },
            {
                "name": "Fakultas Teknik",
                "slug": "ft-ugm",
                "majors": [
                    {
                        "name": "Teknik Sipil",
                        "slug": "teknik-sipil-ugm",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 150,
                        "tuition_min": 0,
                        "tuition_max": 13000000,
                        "career_prospects": "Structural Engineer, Construction Manager, Urban Infrastructure Planner",
                    },
                ],
            },
        ],
    },
    {
        "name": "Institut Teknologi Sepuluh Nopember",
        "short_name": "ITS",
        "slug": "institut-teknologi-sepuluh-nopember",
        "type": "PTN",
        "accreditation": "Unggul",
        "city": "Surabaya",
        "province": "Jawa Timur",
        "address": "Jl. Teknik Kimia, Sukolilo, Surabaya, Jawa Timur 60111",
        "website": "https://www.its.ac.id",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Lambang_ITS.png/800px-Lambang_ITS.png",
        "banner_url": "https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?auto=format&fit=crop&w=1200&q=80",
        "description": "ITS Surabaya adalah perguruan tinggi maritim dan teknologi terkemuka di Indonesia dengan keunggulan riset robotika dan kelautan.",
        "ranking_national": 4,
        "faculties": [
            {
                "name": "Fakultas Teknologi Elektro dan Informatika Cerdas (FTEIC)",
                "slug": "fteic-its",
                "majors": [
                    {
                        "name": "Teknik Informatika",
                        "slug": "teknik-informatika-its",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 180,
                        "tuition_min": 0,
                        "tuition_max": 10000000,
                        "career_prospects": "Backend Developer, AI Engineer, Mobile App Developer",
                    },
                    {
                        "name": "Sistem Informasi",
                        "slug": "sistem-informasi-its",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 150,
                        "tuition_min": 0,
                        "tuition_max": 10000000,
                        "career_prospects": "Business Process Analyst, IT Product Manager",
                    },
                ],
            },
        ],
    },
    {
        "name": "Universitas Airlangga",
        "short_name": "UNAIR",
        "slug": "universitas-airlangga",
        "type": "PTN",
        "accreditation": "Unggul",
        "city": "Surabaya",
        "province": "Jawa Timur",
        "address": "Jl. Airlangga No. 4 - 6, Gubeng, Surabaya, Jawa Timur 60115",
        "website": "https://www.unair.ac.id",
        "logo_url": "https://upload.wikimedia.org/wikipedia/id/thumb/9/91/Lambang_Universitas_Airlangga.svg/800px-Lambang_Universitas_Airlangga.svg.png",
        "banner_url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1200&q=80",
        "description": "Universitas Airlangga terkenal dengan keunggulan riset di bidang kesehatan, sains hayat, dan ilmu sosial.",
        "ranking_national": 5,
        "faculties": [
            {
                "name": "Fakultas Kedokteran",
                "slug": "fk-unair",
                "majors": [
                    {
                        "name": "Kedokteran",
                        "slug": "kedokteran-unair",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 200,
                        "tuition_min": 0,
                        "tuition_max": 25000000,
                        "career_prospects": "Dokter, Ahli Patologi, Peneliti Kesehatan",
                    },
                ],
            },
            {
                "name": "Fakultas Farmasi",
                "slug": "farmasi-unair",
                "majors": [
                    {
                        "name": "Farmasi",
                        "slug": "farmasi-unair-major",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 180,
                        "tuition_min": 0,
                        "tuition_max": 14000000,
                        "career_prospects": "Apoteker Klinis, Formulator Kosmetik & Obat, QC Industri Farmasi",
                    },
                ],
            },
        ],
    },
    {
        "name": "Bina Nusantara University",
        "short_name": "BINUS",
        "slug": "bina-nusantara-university",
        "type": "PTS",
        "accreditation": "Unggul",
        "city": "Jakarta Barat",
        "province": "DKI Jakarta",
        "address": "Jl. K. H. Syahdan No. 9, Palmerah, Kota Jakarta Barat, DKI Jakarta 11480",
        "website": "https://www.binus.ac.id",
        "logo_url": "https://upload.wikimedia.org/wikipedia/id/thumb/a/a2/Logo_Binus_University.png/800px-Logo_Binus_University.png",
        "banner_url": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1200&q=80",
        "description": "BINUS University adalah universitas swasta terkemuka di Indonesia dengan kurikulum berorientasi industri teknologi dan global recognition.",
        "ranking_national": 8,
        "faculties": [
            {
                "name": "School of Computer Science",
                "slug": "socs-binus",
                "majors": [
                    {
                        "name": "Computer Science",
                        "slug": "computer-science-binus",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 500,
                        "tuition_min": 18000000,
                        "tuition_max": 25000000,
                        "career_prospects": "Full Stack Developer, Cyber Security Analyst, Mobile Developer",
                    },
                    {
                        "name": "Game Application and Technology",
                        "slug": "game-tech-binus",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 150,
                        "tuition_min": 18000000,
                        "tuition_max": 25000000,
                        "career_prospects": "Game Developer, Gameplay Programmer, VR/AR Developer",
                    },
                ],
            },
        ],
    },
    {
        "name": "Telkom University",
        "short_name": "Tel-U",
        "slug": "telkom-university",
        "type": "PTS",
        "accreditation": "Unggul",
        "city": "Bandung",
        "province": "Jawa Barat",
        "address": "Jl. Telekomunikasi No. 1, Terusan Buahbatu, Sukapura, Dayeuhkolot, Kabupaten Bandung, Jawa Barat 40257",
        "website": "https://telkomuniversity.ac.id",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Logo_Telkom_University_potrait.png/800px-Logo_Telkom_University_potrait.png",
        "banner_url": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=80",
        "description": "Telkom University adalah perguruan tinggi swasta nomor satu di Indonesia yang berfokus pada teknologi informasi, telekomunikasi, dan industri kreatif.",
        "ranking_national": 9,
        "faculties": [
            {
                "name": "Fakultas Informatika",
                "slug": "fif-telkom",
                "majors": [
                    {
                        "name": "Informatika",
                        "slug": "informatika-telkom",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 450,
                        "tuition_min": 12000000,
                        "tuition_max": 16000000,
                        "career_prospects": "Software Engineer, Cloud Solutions Specialist, AI Developer",
                    },
                    {
                        "name": "Sains Data",
                        "slug": "sains-data-telkom",
                        "degree": "S1",
                        "accreditation": "Unggul",
                        "capacity": 150,
                        "tuition_min": 12000000,
                        "tuition_max": 16000000,
                        "career_prospects": "Data Scientist, Business Intelligence Analyst, Big Data Engineer",
                    },
                ],
            },
        ],
    },
    {
        "name": "Politeknik Negeri Bandung",
        "short_name": "POLBAN",
        "slug": "politeknik-negeri-bandung",
        "type": "PTK",
        "accreditation": "Unggul",
        "city": "Bandung Barat",
        "province": "Jawa Barat",
        "address": "Jl. Gegerkalong Hilir, Ciwaruga, Kec. Parongpong, Kabupaten Bandung Barat, Jawa Barat 40559",
        "website": "https://www.polban.ac.id",
        "logo_url": "https://upload.wikimedia.org/wikipedia/id/thumb/7/7b/Logo_Polban.png/800px-Logo_Polban.png",
        "banner_url": "https://images.unsplash.com/photo-1519452635265-7b1fbfd1e4e0?auto=format&fit=crop&w=1200&q=80",
        "description": "Politeknik Negeri Bandung adalah perguruan tinggi vokasi terkemuka di Indonesia yang menghasilkan tenaga profesional terampil siap kerja.",
        "ranking_national": 15,
        "faculties": [
            {
                "name": "Jurusan Teknik Komputer dan Informatika",
                "slug": "jtki-polban",
                "majors": [
                    {
                        "name": "D3 Teknik Informatika",
                        "slug": "d3-teknik-informatika-polban",
                        "degree": "D3",
                        "accreditation": "Unggul",
                        "capacity": 90,
                        "tuition_min": 0,
                        "tuition_max": 7500000,
                        "career_prospects": "Junior Programmer, Web Developer, Database Administrator",
                    },
                    {
                        "name": "D4 Teknik Informatika",
                        "slug": "d4-teknik-informatika-polban",
                        "degree": "D4",
                        "accreditation": "Unggul",
                        "capacity": 60,
                        "tuition_min": 0,
                        "tuition_max": 8500000,
                        "career_prospects": "Software Engineer, System Integrator, DevOps Specialist",
                    },
                ],
            },
        ],
    },
]


def seed_database():
    print("🌱 Memulai seeding data kampus...")
    db = SessionLocal()
    try:
        campuses_created = 0
        faculties_created = 0
        majors_created = 0

        for campus_data in CAMPUSES_DATA:
            existing = db.query(Campus).filter(Campus.slug == campus_data["slug"]).first()
            if existing:
                print(f"⏩ Kampus '{campus_data['name']}' sudah ada. Melewati...")
                continue

            faculties_data = campus_data.pop("faculties", [])

            # Create campus
            campus = Campus(**campus_data)
            db.add(campus)
            db.flush()
            campuses_created += 1

            for fac_data in faculties_data:
                majors_data = fac_data.pop("majors", [])
                faculty = Faculty(**fac_data, campus_id=campus.id)
                db.add(faculty)
                db.flush()
                faculties_created += 1

                for major_data in majors_data:
                    major = Major(
                        **major_data,
                        campus_id=campus.id,
                        faculty_id=faculty.id,
                    )
                    db.add(major)
                    majors_created += 1

        db.commit()
        print(f"✅ Seeding selesai!")
        print(f"   - {campuses_created} Kampus ditambahkan")
        print(f"   - {faculties_created} Fakultas ditambahkan")
        print(f"   - {majors_created} Program Studi ditambahkan")
    except Exception as e:
        db.rollback()
        print(f"❌ Error saat seeding data: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
