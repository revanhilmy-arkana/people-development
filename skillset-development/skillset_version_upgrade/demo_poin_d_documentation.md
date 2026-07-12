# CONTOH PRAKTIS (DEMO) POIN D: DOCUMENTING ISSUES

Berikut adalah perbandingan *mindset* antara seorang "Developer Awam" melawan "Developer Profesional (Poin D)" saat dihadapkan pada masalah ketika melakukan *upgrade* Odoo.

---

## ❌ CARA BURUK (Tanpa Dokumentasi / Hanya Lisan)

**Si Developer Awam:** 
*(Hanya melapor seadanya di grup chat WhatsApp)*
> *"Mas, modul `arkana_reporting` error terus nih pas di-install di Odoo 19. Kayaknya fitur bawaan Odoo-nya banyak yang dirombak. Ya udah, bagian reportnya saya komen (matikan) aja ya kodenya, biar modul lain bisa jalan dulu."*

**Kenapa Cara Ini Sangat Buruk?**
- PM (Project Manager) dan Lead Developer tidak tahu **bagian mana** dari modul report yang sebenarnya mati.
- 3 bulan kemudian saat klien komplain karena fitur reportnya tiba-tiba hilang, tidak ada *history* tertulis satupun mengapa fitur itu dihilangkan. Semua orang lupa, dan kamu akan disalahkan!

---

## ✅ CARA BAIK (Terstruktur - Standar Poin D)

**Si Developer Profesional:** 
*(Segera membuat tiket Issue di Gitlab / Trello, atau membuat file `UPGRADE_NOTES.md`)*

**Format Dokumentasi (Template):**

```text
Judul Issue: [Odoo 19 Upgrade] Compatibility Issue - Modul Arkana Reporting

[DESKRIPSI MASALAH (WHAT)]
Saat melakukan upgrade modul `arkana_reporting` dari Odoo 16 ke Odoo 19, fitur pencetakan 'Laporan Rekap Bulanan' tidak berfungsi dan memicu Internal Server Error.

[PENYEBAB TEKNIS (WHY)]
Di versi Odoo 16, kita meng-override fungsi `_build_report_context()` bawaan dari `ir.actions.report`. Namun pada Odoo 19, Odoo pusat telah mengubah arsitektur QWeb reporting, sehingga parameter/method tersebut dihapus.

[STATUS / WORKAROUND (SOLUSI SEMENTARA)]
- Agar proses upgrade keseluruhan tidak tertahan, untuk sementara tombol 'Laporan Rekap Bulanan' saya sembunyikan (`invisible="1"`) di file `view_report.xml`.
- Potongan kode Python yang menyebabkan error sudah saya amankan ke dalam komentar (comment out).

[TINDAK LANJUT (NEXT ACTION)]
Membutuhkan diskusi dengan Senior Developer untuk mencari alternatif cara membuat report menggunakan framework Odoo 19 yang baru.
```

---

## 🚀 KESIMPULAN POIN D

Dokumentasi terstruktur di atas akan menjadi **"pelampung penyelamat" (lifesaver)** bagi timmu. 

Meskipun sebagai *Beginner* kamu mungkin belum sanggup memecahkan masalah arsitektur *reporting* tersebut sendirian, tapi kamu telah menyelamatkan reputasi proyek dengan menandai "lokasi ranjau" agar tim tahu apa yang harus diperbaiki ke depannya. Itulah wujud nyata penguasaan **Poin D**!
