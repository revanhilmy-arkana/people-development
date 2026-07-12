# Version Upgrade - Beginner (Poin A)

Selamat datang di skillset **Version Upgrade**! Skill ini membahas bagaimana caramu menjaga agar kodemu tetap bisa bertahan (survive) ketika Odoo melakukan *upgrade* versi (misalnya dari Odoo 17 ke 18 atau 19).

**Poin A:**
> *"Follows upgrade checklist strictly."*
> (Mengikuti daftar periksa (checklist) upgrade secara ketat/disiplin.)

Di level *Beginner* ini, kamu **belum dituntut** untuk merancang strategi *upgrade* database dari nol. Tugas utamamu adalah: Jika tim memintamu me-migrasi modul `custom_hr` dari Odoo 17 ke Odoo 19, kamu harus mengerjakan penyesuaian kodenya berdasarkan panduan (*guidance* / *checklist*) yang sudah ada tanpa ada yang terlewat!

---

## 1. Apa Maksudnya "Strictly" (Secara Ketat)?

Dalam proses *upgrade* versi Odoo, ada banyak sekali perubahan kecil (tapi fatal) yang dirilis oleh Odoo pusat. 
Misalnya:
- Atribut `attrs` di XML sudah dihapus di Odoo 17+ dan diganti langsung dengan `invisible="..."`.
- Penamaan parameter di fungsi tertentu mungkin berubah.

Jika Lead-mu memberikan *Checklist* yang berisi 5 hal yang harus diubah, kamu harus mengecek dan mengubah kelimanya! Jika kamu hanya mengerjakan 4 dan melewatkan 1 poin (karena malas atau lupa), modul tersebut akan *crash* di *production*. Itulah kenapa kedisiplinan (*strictly*) menjadi poin pertama.

---

## 2. Apa yang Perlu Dilakukan? (Action Plan)

1. **Selalu Minta atau Cari Checklist:** Saat mendapat tugas migrasi modul ke versi Odoo baru, jangan langsung *coding* membabi buta. Tanyakan pada Lead: *"Apakah ada dokumen panduan/checklist perubahan dari Odoo versi X ke versi Y?"* atau cari tahu di Release Notes Odoo.
2. **Ubah `__manifest__.py` Terlebih Dahulu:** Langkah absolut pertama dalam *upgrade* adalah memastikan `'version'` di *manifest* sudah dinaikkan sesuai versi Odoo target.
3. **Patuhi Panduan Tim:** Jika Arkana memiliki standar panduan internal tentang cara me-migrasi kode (misal menggunakan skrip tertentu atau refactor manual), ikuti aturan tersebut.

---

## 🎯 Cara Membuktikan ke Lead/Reviewer (Achievement Poin A)

Kamu bisa membuktikan bahwa kamu menguasai poin ini saat mengerjakan tiket/tugas migrasi modul.

**Skenario Bukti:**
Saat kamu menyerahkan hasil *upgrade* (membuat PR/Merge Request), lampirkan *checklist* di kolom komentar *Pull Request* dan centang semua daftarnya!

> **Komentar di Merge Request:**
> *"Halo Mas/Mbak, saya sudah selesai memigrasi modul `arkana_hr_lembur` ke Odoo 19. Berikut checklist yang sudah saya pastikan (strictly followed):*
> *[x] Update versi di __manifest__.py ke 19.0.1.0.0*
> *[x] Mengganti semua `attrs` di XML menjadi format baru (`invisible` dll)*
> *[x] Memastikan icon modul sudah terbaca*
> *[x] Test install di lokal tanpa error"*

Melihat kedisiplinanmu mencentang panduan ini, Reviewer akan otomatis menganggap Poin A-mu terpenuhi.
