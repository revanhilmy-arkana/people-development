# Version Upgrade - Beginner (Poin B)

**Poin B:**
> *"Fixes deprecated methods correctly."*
> (Memperbaiki metode/fungsi yang sudah kedaluwarsa (*deprecated*) dengan benar.)

Dalam dunia *software development*, fungsi yang hari ini sangat sering kita pakai bisa jadi besok dianggap usang (*deprecated*) oleh pencipta *framework*-nya (Odoo) karena ada fungsi baru yang lebih cepat, aman, atau logis. 

Di level *Beginner* ini, kamu harus tahu cara menangani fungsi-fungsi usang tersebut secara tepat saat melakukan *upgrade* modul.

---

## 1. Apa itu Deprecated Methods?

*Deprecated* artinya fungsi tersebut **"sudah tidak disarankan untuk digunakan lagi, dan kemungkinan besar akan dihapus secara total di versi Odoo berikutnya"**.

Contoh nyata di Odoo:
- Di Odoo lama (versi 16 ke bawah), jika kita ingin mengubah tampilan nama *record* di *dropdown*, kita wajib menggunakan fungsi `name_get()`. 
- Di Odoo baru (17 ke atas), fungsi `name_get()` ini dinyatakan *deprecated* dan diganti dengan mekanisme yang lebih modern yaitu mengubah nilai field `_compute_display_name()`.

**Mengapa ini penting?**
Kalau kamu membiarkan fungsi *deprecated* tetap ada di dalam kodemu hasil migrasi, modul memang (kadang-kadang) masih bisa jalan, TAPI:
1. Log server akan dipenuhi *warning* merah/kuning yang menyebalkan.
2. Performa sistem menurun.
3. Saat klien minta *upgrade* ke versi berikutnya lagi (misal tahun depan ke Odoo 20), modulmu dipastikan akan *crash* dan mati total karena fungsi itu sudah benar-benar dihapus!

---

## 2. Apa yang Perlu Dilakukan? (Action Plan)

1. **Pantau Log Terminal:** Saat kamu menjalankan modul lamamu di Odoo versi baru (misal Odoo 19), perhatikan log terminal secara saksama! Jika ada tulisan `WARNING: ... is deprecated`, **JANGAN DIABAIKAN!** Itu adalah musuh yang harus dibasmi.
2. **Cari Penggantinya (The Right Way):** Jangan pernah menebak-nebak cara memperbaikinya. Buka *source code* Odoo bawaan (cari file asli Odoo) atau tanyakan pada AI: *"Apa pengganti fungsi `name_get()` di Odoo 19?"*
3. **Refactor Kode Menyeluruh:** Jika fungsi usang itu dipanggil di 10 tempat berbeda di dalam modulmu, gunakan fitur `Search and Replace` (Ctrl+Shift+F di VS Code) untuk mengubah kesepuluh tempat tersebut. Jangan sampai ada yang terlewat!

---

## 🎯 Cara Membuktikan ke Lead/Reviewer (Achievement Poin B)

Bukti terbaik untuk poin ini adalah dari kebersihan log server dan kerapian kodemu saat disetorkan ke Gitlab/Github.

Jika Reviewer (Lead-mu) melihat kodemu dan bertanya: 
*"Kenapa kamu menghapus fungsi `name_get()` bawaan dari Odoo versi sebelumnya dan menggantinya dengan fungsi compute?"*

**Jawabanmu (Buktikan pemahamanmu):**
> *"Karena saat saya tes modulnya, Odoo memunculkan warning bahwa `name_get()` sudah deprecated di versi ini dan digantikan oleh `_compute_display_name()`. Saya sudah me-refactor kodenya dengan benar agar modul kita 'future-proof' (aman untuk masa depan) dan log server kita tetap bersih dari warning."*
