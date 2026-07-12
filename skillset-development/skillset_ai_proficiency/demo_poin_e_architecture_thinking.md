# CONTOH PRAKTIS (DEMO) POIN E: ARCHITECTURE THINKING

Berikut adalah perbandingan *mindset* "Tukang Copas" vs "Developer Arsitek" saat dihadapkan pada sebuah *task* (tugas) pengembangan modul Odoo.

---

## ❌ SKENARIO BURUK (Bypassing Architecture Thinking)

**Tiket Tugas dari PM:** *"Buatkan fitur agar tim HR bisa mencatat laptop dan aset perusahaan yang sedang dipinjam oleh karyawan."*

**Langkah Si Developer Buruk:**
1. Langsung buka ChatGPT dan mengetik: *"Buatkan modul Odoo HR untuk pinjam barang."*
2. AI (karena tidak punya konteks) merespons dengan membuat model baru bernama `pinjam.barang` dari nol, tanpa menghubungkannya ke modul bawaan `hr.employee` atau `maintenance.equipment`.
3. Developer langsung *copy-paste* semua kode ke Odoo dan berhasil *running*.
4. **Hasil Akhir (Gagal Arsitektur):** Modul memang berjalan, tapi terisolasi. Saat HR membuka profil seorang Karyawan, HR tidak bisa melihat daftar barang apa saja yang sedang ia pinjam, karena datanya tidak berelasi (*Many2one*). Saat klien komplain, developer kebingungan mengubah strukturnya.

---

## ✅ SKENARIO BAIK (AI for Acceleration + Architecture Thinking)

**Tiket Tugas dari PM:** *"Buatkan fitur agar tim HR bisa mencatat laptop dan aset perusahaan yang sedang dipinjam oleh karyawan."*

**Langkah Si Developer Profesional (Poin E Achieved):**
1. **Berpikir Arsitektur:** Ia mendesain sejenak, *"Odoo sudah punya model `hr.employee` dan modul `maintenance`. Lebih baik saya tidak buat model dari nol. Saya akan meng-inherit model `hr.employee` lalu menambahkan relasi `One2many` ke tabel aset."*
2. **Akselerasi via AI:** Ia sudah tahu desainnya, ia hanya malas mengingat sintaks penulisan `xpath` Odoo yang panjang. Ia buka AI dan mengetik *Prompt Terstruktur*:
   > *"Tolong generate boilerplate kode Python dan XML Odoo 19 untuk meng-inherit `hr.employee`. Tambahkan field `One2many` bernama `equipment_ids` yang berelasi ke model `maintenance.equipment`. Buatkan juga *xpath* untuk menampilkan field ini di halaman Notebook profil karyawan."*
3. **Hasil Akhir:** AI memberikan *template* kode yang sangat akurat dalam hitungan detik. Developer men-*copy*, memvalidasi kodenya, dan fitur selesai dalam 10 menit dengan arsitektur Odoo yang sempurna dan *scalable*!

---

## 🚀 KESIMPULAN POIN E
Biarkan **otakmu** yang menjadi "Arsitek/Mandor", dan biarkan **AI** yang menjadi "Tukang Ketik/Kuli"-nya. Itulah level keahlian sejati seorang *AI Proficient Developer*!
