# Version Upgrade - Beginner (Poin D)

**Poin D:**
> *"Documents compatibility issues."*
> (Mendokumentasikan masalah kompatibilitas/kecocokan antar versi.)

Proses *upgrade* versi Odoo (misal dari versi 16 ke 19) tidak selamanya berjalan mulus layaknya jalan tol. Poin D ini menuntutmu untuk tidak sekadar "tahu" kalau ada kode yang rusak, tapi juga memiliki kebiasaan untuk **mencatat dan melaporkannya** secara terstruktur.

---

## 1. Apa itu Compatibility Issues?

*Compatibility Issues* (Masalah Kompatibilitas) terjadi ketika kode atau alur kerja (*workflow*) yang tadinya berjalan sempurna di Odoo versi lama, tiba-tiba rusak total di versi baru karena arsitektur inti Odoo-nya diubah oleh pembuatnya.

**Contoh Kasus Nyata di Lapangan:**
- Di Odoo 15, modul *custom* menggunakan *library* pihak ketiga yang sangat usang. Di Odoo 19 (yang menggunakan versi Python terbaru), *library* itu tidak dikenali lagi dan membuat instalasi gagal.
- Odoo 19 membuang total satu *view* menu yang dulunya kamu pakai sebagai tempat menempelkan (*inherit*) tombol kustom perusahaan.

---

## 2. Apa yang Perlu Dilakukan? (Action Plan)

Sebagai *Beginner*, kamu belum dituntut untuk bisa memecahkan dan mendesain ulang arsitektur besar sendirian saat terjadi kebuntuan kompatibilitas. Tugas utamamu adalah: **Menjadi mata dan telinga yang dapat diandalkan oleh tim.**

1. **Haram Menutupi Kesalahan:** Jika kamu menemukan fitur yang error dan terpaksa kamu matikan (di-*comment* kodenya) agar modul bisa terinstal di versi baru, **jangan pernah diam saja!**
2. **Catat Secara Tertulis:** Buat dokumentasi tertulis (bisa di file `UPGRADE_NOTES.md` di dalam modul, atau di tiket Trello/Jira/Gitlab).
3. **Gunakan Format Pelaporan 3W:**
   - **What:** Apa persisnya fitur yang rusak?
   - **Why:** Kenapa fitur itu rusak di Odoo versi baru?
   - **Workaround:** Apa solusi sementaramu saat ini agar proses *upgrade* tidak *stuck*?

---

## 🎯 Cara Membuktikan ke Lead/Reviewer (Achievement Poin D)

Momen terbaik untuk membuktikan pencapaian Poin D adalah saat pelaporan progres (Daily Standup) atau saat *Code Review*.

**Tunjukkan Bukti Dokumentasimu dan Katakan:**
> *"Mas/Mbak, progres upgrade modul `custom_hr` berjalan lancar, tapi saya menemukan satu **Compatibility Issue**. Fungsi tombol 'Print Rekap' terpaksa saya nonaktifkan sementara karena library yang kita pakai *crash* dengan Python bawaan Odoo 19. Detail teknis dan log error-nya sudah saya **dokumentasikan** di tiket #123 agar nanti bisa kita bahas solusinya bersama tim."*

Dengan melaporkan "ranjau" (masalah) secara transparan dan tertulis, kamu memposisikan dirimu sebagai profesional sejati, dan Poin D-mu langsung terpenuhi!
