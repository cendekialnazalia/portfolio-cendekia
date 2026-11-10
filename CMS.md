# Mengedit isi website dengan Pages CMS

Isi website ada di `site/data/*.json`, foto di `site/media/`. Pages CMS membaca `.pages.yml` dan menampilkan form untuk tiap file.

## Sekali saja
1. Push project ini ke GitHub (repo baru, branch `main`).
2. Deploy ke Vercel: Framework **Other**, Root Directory **`site`**, build command kosong.
3. Buka https://app.pagescms.org, login dengan GitHub, izinkan akses ke repo ini.

## Sehari-hari
1. Buka app.pagescms.org → pilih repo → pilih bagian (Journey, Projects, dst).
2. Edit / tambah item, upload foto, klik **Save**.
3. Pages CMS membuat commit ke GitHub → Vercel deploy ulang otomatis (±30 detik).

## Bagian yang bisa diedit
| Menu di CMS | File |
|---|---|
| Journey (buku per tahun) | `site/data/journey.json` |
| Projects | `site/data/projects.json` |
| Produk digital | `site/data/products.json` |
| Work with me | `site/data/services.json` |
| Achievements | `site/data/achievements.json` |
| Testimoni | `site/data/testimonial.json` |
| Collaborated with | `site/data/partners.json` |
| Hero (teks slide) | `site/data/hero.json` |
| Let's connect | `site/data/contact.json` |

## Tips
- **Journey:** foto yang dicentang "Satu halaman dengan foto berikutnya" ditaruh berdua di satu halaman. Rasio foto dideteksi otomatis.
- **Foto:** kecilkan dulu ke lebar ±1400 px sebelum upload supaya website tetap cepat.
- **Warna:** tulis kode hex, mis. `#E8392B` (merah), `#2F5BEA` (biru), `#1F9D55` (hijau), `#F0459A` (pink).
- Bagian HELLO, Skills, dan foto potongan di hero masih di `site/index.html` (perlu edit kode).

## Preview lokal
```bash
python3 serve.py
```
Lalu buka http://localhost:5173. (Membuka `index.html` langsung dari Finder tidak bisa, karena data dimuat lewat server.)
