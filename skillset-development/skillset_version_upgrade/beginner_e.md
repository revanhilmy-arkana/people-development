# Version Upgrade - Beginner (Poin E)

**Poin E:**
> *"Avoids unnecessary deep customization."*
> (Menghindari kustomisasi mendalam yang tidak diperlukan.)

Poin terakhir dari skillset *Version Upgrade* ini adalah tentang **Mindset Pencegahan**. Tugas seorang *developer* sejati bukan sekadar membuat sebuah fitur bisa berjalan hari ini, melainkan memastikan kode tersebut tidak menjadi "beban mematikan" (*Technical Debt*) saat klien meminta *upgrade* sistem Odoo ke versi baru tahun depan.

---

## 1. Apa itu "Deep Customization"?

*Deep Customization* (Kustomisasi Mendalam) terjadi ketika kamu merombak, menimpa (*override*), atau mengotak-atik alur fungsi inti (inti *framework*) bawaan Odoo.

**Contoh Kustomisasi Mendalam yang Buruk:**
- Meng-*override* fungsi super-inti seperti `create()` atau `write()` di model utama (misal `res.partner` atau `sale.order`) hanya untuk urusan sepele (contoh: sekadar memanipulasi teks menjadi huruf besar).
- Menulis sintaks *Raw SQL Query* (`env.cr.execute`) untuk menarik data *report*, padahal bisa diselesaikan dengan fungsi standar ORM `search()`.
- Men-*copy-paste* seluruh file JavaScript/QWeb *view* bawaan Odoo ke dalam modulmu hanya demi mengganti warna/teks satu buah tombol.

**Kenapa Ini Sangat Berbahaya (Musuh Utama Upgrade)?**
Saat Odoo merilis versi baru, mereka selalu melakukan optimalisasi dengan mengubah fungsi-fungsi inti mereka. Jika kodemu sangat bergantung pada "Kustomisasi Mendalam", saat proses migrasi versi, modulmu akan **rusak total**. Pekerjaan *upgrade* yang seharusnya memakan waktu 1 hari bisa bengkak menjadi 2 minggu hanya untuk memperbaiki satu fitur tersebut!

---

## 2. Apa yang Perlu Dilakukan? (Action Plan)

1. **Selalu Cari Fitur Standar (*Standard Feature*):** Sebelum kalap menulis ratusan baris kode kustom, bertanyalah pada Lead atau AI: *"Apakah Odoo punya fitur bawaan (native) untuk kebutuhan ini?"*. Sering kali, permintaan klien bisa diselesaikan cukup dengan "Mencentang Opsi" di menu *Settings* tanpa perlu *coding* 1 baris pun!
2. **Gunakan Fitur Sederhana (*Hooks*):** Daripada merombak fungsi penyimpan *database* (`create`/`write`), gunakanlah mekanisme dekorator standar Odoo yang sangat aman, seperti `@api.onchange` atau `@api.depends`.
3. **Patuhi Prinsip "Keep It Simple":** Semakin sedikit baris kode Python kustom yang kamu paksa masukkan ke sistem Odoo, semakin mudah modulmu meluncur mulus saat di-*upgrade* ke versi berapapun di masa depan.

---

## 🎯 Cara Membuktikan ke Lead/Reviewer (Achievement Poin E)

Reviewer senior sangat alergi melihat baris kode *override* (menimpa fungsi bawaan) yang tidak berguna. Kamu bisa membuktikan keahlian Poin E saat sedang merancang solusi.

**Contoh Argumenmu (Saat Rapat / Code Review):**
> *"Untuk fitur otomatisasi Nomor Kontrak ini, awalnya saya kepikiran untuk menimpa (override) method `create()` bawaan Odoo. Tapi menurut saya itu berisiko memicu *bug* panjang saat kita *upgrade* Odoo tahun depan (unnecessary deep customization).*
> 
> *Jadi solusinya, saya hanya menggunakan fitur standard Odoo `ir.sequence` XML saja. Kodenya jauh lebih simpel, murni 100% Odoo Way, dan pastinya sangat 'Upgrade-Safe'!"*

Mendengar argumen *upgrade-safe* (peduli masa depan) darimu, Lead-mu dipastikan langsung mencentang Poin E milikmu dengan nilai penuh (5)!
