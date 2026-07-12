# CONTOH PRAKTIS (DEMO) POIN C: TESTING SCENARIO

Berikut adalah contoh skenario pengujian manual (Lembar Check-Up) yang bisa kamu simpan sebagai panduan tiap kali selesai me-migrasi modul ke Odoo versi baru.

---

## 🧪 Skenario Testing Modul: "arkana_hr_lembur"

### Sesi 1: Instalasi & Log Terminal
- [ ] Database baru Odoo (versi target) disiapkan.
- [ ] Modul di-*install* atau di-*upgrade* via layar Apps Odoo.
- [ ] **Ekspektasi:** Modul sukses terinstal.
- [ ] **Validasi:** Cek terminal VS Code. Apakah ada tulisan `WARNING` atau `ERROR`? Jika ada peringatan "deprecated", kembali ke **Poin B** dan perbaiki! Jika terminal bersih, lanjut ke Sesi 2.

### Sesi 2: Pengujian UI (User Interface)
- [ ] Klik menu "HR Lembur".
- [ ] **Ekspektasi:** Halaman *Tree View* (Daftar tabel lembur) terbuka normal.
- [ ] Buka salah satu data lembur.
- [ ] **Ekspektasi:** Halaman *Form View* terbuka. Kolom (*field*) tidak bertumpuk/berantakan, dan *field* yang diset `invisible` di versi lama benar-benar tersembunyi dengan sempurna di versi baru.

### Sesi 3: Pengujian Fungsionalitas (CRUD & Workflow)
- [ ] Klik "New" (Buat data lembur baru).
- [ ] Isi data Karyawan, Tanggal, dan Jam. Lalu klik icon awan / "Save".
- [ ] **Validasi (Create)**: Data tersimpan ke *database* tanpa memicu *error popup* merah.
- [ ] Klik tombol "Submit to Manager" (atau transisi *state* yang ada).
- [ ] **Validasi Workflow**: Status berubah dari `Draft` ke `Submitted`. Tidak ada error eksekusi Python (*Run-time error*).
- [ ] Klik data tersebut lagi, ubah jam lembur, lalu simpan ulang.
- [ ] **Validasi (Update)**: Data berhasil diperbarui.
- [ ] Hapus data lembur yang baru dibuat (Action -> Delete).
- [ ] **Validasi (Delete)**: Data terhapus bersih (tidak ada constraint error SQL yang mencegah penghapusan).

---

**Kesimpulan:**
Dengan merutinkan lembar pengujian (testing) sederhana ini sebelum meminta *review*, kamu telah membuktikan bahwa kode migrasi yang kamu tulis tidak sekadar "selesai diketik", tapi benar-benar siap diterjunkan untuk *Client* di Odoo versi baru. 

Inilah wujud nyata penguasaan **Poin C**!
