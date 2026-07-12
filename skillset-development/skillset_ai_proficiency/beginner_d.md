# AI Proficiency - Beginner (Poin D)

**Poin D:**
> *"Implements basic function calling and tool usage in simple, well-scoped cases."*
> (Mengimplementasikan pemanggilan fungsi (*function calling*) dan penggunaan *tools* AI dasar dalam kasus yang sederhana dan terukur.)

Ini adalah poin yang **paling teknikal** di level Beginner. Di sini kamu tidak lagi sekadar *chatting* dengan ChatGPT, melainkan kamu menulis program di mana kodemu memberikan "tangan dan mata" kepada AI untuk mengambil aksi.

---

## 1. Apa itu Function Calling / Tool Usage?

Biasanya, saat kamu bertanya pada AI: *"Berapa sisa cuti Budi?"*, AI akan menjawab: *"Maaf, saya hanyalah AI bahasa dan tidak punya akses ke databasemu."*

**Function Calling** adalah fitur (di API OpenAI, Anthropic, Gemini) yang memungkinkan kita memberi tahu AI: *"Hei AI, saya memberimu sebuah alat (tool) bernama `cek_sisa_cuti`. Kalau ada *user* nanya soal cuti, jangan mengarang jawaban! Instruksikan saya untuk menjalankan fungsi itu."*

**Alur Kerjanya:**
1. **User (via Prompt):** *"Berapa sisa cuti Budi?"*
2. **AI menganalisis & merespons:** Alih-alih membalas teks biasa, AI membalas dengan format JSON internal: `{"nama_fungsi": "cek_sisa_cuti", "parameter": {"nama": "Budi"}}`.
3. **Kode Python-mu (Eksekusi Lokal):** Membaca JSON dari AI tersebut, lalu kodemu yang betulan menjalankan fungsi `cek_sisa_cuti("Budi")` ke database Odoo. Hasilnya misal: `12`.
4. **Kode Python-mu (Kirim Balik):** Mengirim angka `12` itu kembali ke AI.
5. **AI (Balasan Akhir):** *"Sisa cuti Budi saat ini adalah 12 hari."*

---

## 2. Apa yang Perlu Dilakukan? (Action Plan)

1. **Pahami JSON Schema:** Untuk memberi tahu AI fungsi apa saja yang kamu punya, kamu harus mendefinisikannya dalam bentuk JSON.
2. **Buat Skrip Eksperimen (Wajib):** Poin ini tidak bisa hanya "diklaim paham". Kamu harus pernah membuat minimal satu skrip Python yang melakukan pemanggilan API LLM menggunakan parameter `tools` atau `functions`.

---

## 🎯 Cara Membuktikan ke Lead/Reviewer (Achievement Poin D)

Karena poin ini berbunyi *"Implements..."* (Mengimplementasikan), kamu butuh **Bukti Konkret (Commit di Git)**.

1. Buka file `demo_poin_d_function_calling.py` yang saya buatkan di folder ini.
2. Pelajari alur kodenya. Di situ saya membuat simulasi sederhana bagaimana AI memanggil fungsi Python lokal.
3. Jalankan skrip tersebut, atau buat ulang dengan versimu sendiri.
4. Lakukan **Commit & Push** skrip eksperimenmu ini ke *repository* (misal di folder `testing_js` atau di modul Odoo eksperimen) dengan pesan commit:
   `feat: implement basic LLM function calling to check employee leave balance`

Jika *Lead* atau *Reviewer*-mu mengecek riwayat kerjamu dan melihat *commit* ini, mereka pasti langsung mencentang **Poin D** ini sebagai "Lulus"!
