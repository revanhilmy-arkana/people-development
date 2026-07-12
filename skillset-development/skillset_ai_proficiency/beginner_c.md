# AI Proficiency - Beginner (Poin C)

**Poin C:**
> *"Validates AI output before implementation and can explain technically why it works."*
> (Memvalidasi output AI sebelum diimplementasikan dan bisa menjelaskan secara teknis mengapa kode tersebut berfungsi.)

Poin ini adalah **garis batas tegas** (pembeda) antara "Programmer Profesional" dengan "Tukang Copas". Di sini, tanggung jawab atas kualitas dan keamanan kode sepenuhnya ada di tanganmu, bukan di tangan AI.

---

## 1. Apa yang Perlu Dipelajari? (Konsep Validasi AI)

AI (terutama LLM) memiliki "penyakit" yang disebut halusinasi. AI mungkin memberikan sintaks Python yang benar, namun secara logika bisnis atau framework Odoo itu salah (misal: menyarankan fungsi Python *built-in* padahal Odoo punya ORM sendiri, atau mengabaikan *access rights*).

Kamu perlu menerapkan **3 Level Validasi**:
1.  **Validasi Sintaks & Logika (*Syntax & Logic Check*):** Apakah kodenya memanggil *field* yang benar-benar ada di model (database)? Apakah tipe datanya sesuai?
2.  **Validasi Konteks Odoo (*The Odoo Way Check*):** Apakah AI menyarankan `env.cr.execute` padahal bisa pakai `search()`? Apakah AI memberikan ratusan baris kode kustom padahal Odoo sudah punya *standard feature* untuk itu?
3.  **Kemampuan Menjelaskan (*Explainability*):** Jika Senior, Lead, atau PM-mu menunjuk baris kode tersebut dan bertanya *"Apa fungsi baris ini?"*, kamu harus bisa menjelaskannya dengan logis tanpa alasan *"nggak tau, dapet dari AI"*.

---

## 2. Apa yang Perlu Dilakukan? (Action Plan)

1.  **Haramkan *Blind Copy-Paste*:** Jangan pernah mem-blok seluruh jawaban AI, menekan `Ctrl+C`, lalu `Ctrl+V` ke file `.py` dan langsung menekan tombol *Commit*.
2.  **Review Kode Baris per Baris (*Self Code Review*):** Perlakukan kode hasil generate AI layaknya PR (*Pull Request*) dari anak magang atau rekan junior. Kamu wajib mencurigai dan membaca setiap barisnya.
3.  **Tanya Balik ke AI (*Cross-Questioning*):** Jika AI memberikan kode yang rumit dan ada baris fungsi yang belum pernah kamu lihat (misalnya fungsi `mapped()`, `filtered()`, atau `sudo()`), **JANGAN LANGSUNG DIPAKAI**. Tanyakan balik: *"Jelaskan detail apa fungsi baris `mapped()` pada kodemu tadi, dan apa bedanya dengan `for` loop biasa?"*. Pahami dulu secara teknikal.
4.  **Uji Coba Lokal:** Jalankan server (misal: `localhost:8069`). Buat skenario *error* (*Negative Testing*). Pastikan kode AI tidak merusak fitur lain.

---

## 🎯 Cara Membuktikan ke Lead/Reviewer (Achievement Poin C)

Momen terbaik untuk membuktikan pencapaian Poin C adalah saat sesi *Code Review* (Merge Request). Saat Reviewer membahas kodemu, tunjukkan sikap kepemilikan (*ownership*):

> *"Baris ini awalnya saya pakai AI untuk buat *draft* kasarnya. Tapi saat saya baca, AI malah menyarankan menggunakan `search()` biasa. Karena kita cuma mau ngitung jumlah data, saya **ubah sendiri (validasi)** menggunakan `search_count()` agar *query database*-nya lebih cepat sesuai *best practice* Odoo."*

(Kalimat ajaib di atas membuktikan kamu tidak sekadar copas, tapi memvalidasi performa dan paham teknisnya!).
