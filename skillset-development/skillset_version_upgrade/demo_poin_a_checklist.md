# CONTOH PRAKTIS (DEMO) POIN A: UPGRADE CHECKLIST

Untuk menguasai **Poin A**, kamu bisa menggunakan *template checklist* di bawah ini setiap kali ditugaskan untuk melakukan *upgrade* modul Odoo ke versi terbaru. 

*Copy-paste* daftar ini ke Notion, Trello, atau tiket Gitlab-mu agar kamu tidak melewatkan apa pun!

---

## 📋 Standard Odoo Module Upgrade Checklist (Beginner)

### 1. Persiapan Awal (Metadata)
- [ ] Buka file `__manifest__.py`.
- [ ] Ubah angka versi Odoo di depan *version* (Misal: dari `'version': '17.0.1.0.0'` menjadi `'version': '19.0.1.0.0'`).
- [ ] Pastikan daftar `depends` (modul bawaan Odoo) masih ada dan tidak diubah namanya oleh Odoo pusat di versi baru.

### 2. Penyesuaian View (XML)
- [ ] Cari fitur `attrs` yang sudah *deprecated*. (Odoo 17+ sudah membuang `attrs="{'invisible': [('state', '=', 'draft')]}"` dan menggantinya dengan `invisible="state == 'draft'"`).
- [ ] Pastikan tidak ada tag HTML/XML bawaan versi lama yang dihapus di versi baru (misal struktur *header* atau *sheet*).

### 3. Penyesuaian Backend (Python)
- [ ] Cek warning *Deprecation* di terminal saat server dijalankan.
- [ ] Pastikan pemanggilan fungsi ORM seperti `search()`, `read()`, `write()`, dan `unlink()` mematuhi aturan argumen versi terbaru (jika ada perubahan keamanan dari Odoo).

### 4. Testing Sederhana (Validasi Lokal)
- [ ] *Restart* server lokal dengan versi Odoo target (misal Odoo 19).
- [ ] Lakukan *Update Module List*.
- [ ] *Install* / *Upgrade* modul tersebut dari layar Apps.
- [ ] Buka modulnya, buat 1 *record* baru (*Create*), Edit, dan Delete.
- [ ] Pastikan tidak ada pesan *Internal Server Error* di layar atau terminal.

---

**Pesan Penting:**
Menjadi *Beginner* di skillset ini berarti kamu **dapat dipercaya** untuk mengeksekusi daftar di atas secara menyeluruh, teliti, dan disiplin tanpa ada *item* yang di-*skip*!
