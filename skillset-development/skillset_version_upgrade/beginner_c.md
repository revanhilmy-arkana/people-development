# Version Upgrade - Beginner (Poin C)

**Poin C:**
> *"Tests modules after version changes."*
> (Melakukan pengujian (testing) pada modul setelah ada perubahan versi.)

Setelah kamu mengubah versi di `__manifest__.py` (Poin A) dan memperbaiki fungsi yang *deprecated* (Poin B), tugasmu belum selesai. Poin C menuntutmu untuk **membuktikan** bahwa kodemu benar-benar berjalan dan tidak rusak di Odoo versi baru melalui proses pengujian (*Testing*).

---

## 1. Mengapa Testing Pasca-Upgrade Sangat Penting?

Dalam pengembangan Odoo, *error* akibat migrasi versi terbagi menjadi dua jenis utama:
1. **Install-Time Error:** Error yang meledak di layar saat kamu mengklik tombol "Upgrade/Install" di menu Apps. Ini biasanya karena kesalahan *syntax* XML atau model Python gagal dimuat. (Biasanya mudah dideteksi).
2. **Run-Time Error:** Modul sukses terinstal tanpa error, tapi saat *user* mengklik tombol "Simpan", mencetak PDF, atau membuka menu tertentu, layar tiba-tiba berubah merah (*Internal Server Error*). Ini sangat sering terjadi karena parameter fungsi bawaan Odoo ada yang diubah oleh penciptanya.

Jika kamu hanya memastikan modul "bisa diinstal" (Install-Time) tanpa mencoba fungsinya, kamu berisiko besar meloloskan *Run-Time Error* ke *Production*. Itu adalah mimpi buruk bagi klien dan tim.

---

## 2. Apa yang Perlu Dilakukan? (Action Plan)

Sebagai developer *Beginner*, kamu belum dituntut untuk membuat *Automated Unit Test* yang rumit, namun kamu wajib melakukan **Manual Functional Testing** (Pengujian Fungsi Manual).

1. **Jalankan Server di Versi Baru:** Pastikan kamu menjalankan Odoo di versi target (misal Odoo 19), gunakan *database* khusus untuk *testing* (bukan *database* utama).
2. **Uji Instalasi (Install Test):** Buka Apps -> Update Apps List -> Install modulmu. Perhatikan layar terminalmu, pastikan bersih dari tumpukan *Traceback* merah.
3. **Uji Fungsionalitas Dasar (CRUD):** Buka menu modulmu, dan perlakukan modul itu seolah kamu adalah *user* awam:
   - **C**reate: Buat data baru dan simpan.
   - **R**ead: Buka data yang sudah ada, pastikan tampilannya tidak berantakan.
   - **U**pdate: Edit data tersebut.
   - **D**elete: Hapus data tersebut.
4. **Uji Tombol Khusus:** Jika modulmu punya tombol seperti "Approve" atau "Print Report", wajib hukumnya untuk diklik dan dites!

---

## 🎯 Cara Membuktikan ke Lead/Reviewer (Achievement Poin C)

Jangan biarkan Reviewer-mu atau QA (Quality Assurance) menjadi orang pertama yang menemukan *error* memalukan di modul hasil migrasimu!
Saat menyerahkan kode (Merge Request), sertakan bukti tesmu.

**Contoh Bukti di Merge Request:**
> *"Modul `arkana_hr_lembur` sudah selesai di-upgrade ke v19. Saya telah melakukan uji fungsional lokal dengan hasil:*
> *- Instalasi modul sukses.*
> *- Proses Create, Update, Delete data lembur berjalan normal.*
> *- Tombol 'Approve' sukses mengubah state tanpa memicu error ORM.*
> *Silakan di-review, terima kasih!"*

Komentar ini menunjukkan kepedulian yang tinggi terhadap kualitas (Quality Ownership), yang akan membuatmu langsung dicentang lulus untuk **Poin C**!
