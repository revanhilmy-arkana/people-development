# AI Proficiency - Beginner (Poin A)

**Poin A:** 
> *"Understands LLM basics (token, context window, temperature) and their practical implications."*
> (Memahami konsep dasar LLM seperti token, context window, temperature, dan dampak praktisnya saat digunakan.)

Untuk menguasai poin ini, kamu harus memahami 3 konsep dasar mesin AI (LLM) beserta **Dampak Praktisnya (Practical Implications)** terhadap caramu *coding* atau *prompting*.

---

## 1. Token (Satuan Baca AI)

**Apa itu Token?**
AI tidak membaca teks per "kata" atau per "huruf" seperti manusia. AI memotong-motong teks menjadi kepingan yang disebut *Token*. 
Sebagai gambaran, 1 token kira-kira sama dengan 4 karakter (atau 3/4 kata). 
- Kata singkat seperti "Odoo" mungkin dihitung 1 token.
- Kata bahasa Indonesia yang kompleks seperti "mengimplementasikan" bisa dipecah AI menjadi 3-4 token.

**Dampak Praktis (Kenapa kamu harus peduli?):**
* **Biaya (Cost):** Semua layanan AI (OpenAI API, Anthropic, dll) ditagih berdasarkan jumlah token (Token Masuk/Prompt & Token Keluar/Completion). Kalau kamu boros kata-kata, biaya API akan membengkak.
* **Batasan Efisiensi:** Ketika kamu mem-paste log error Odoo, jangan copas dari baris pertama sampai ribuan baris terakhir. Itu menghabiskan ribuan token tanpa guna. Ambil bagian `Traceback` yang error saja.

**Cara Membuktikan Kamu Paham:**
Gunakan [OpenAI Tokenizer](https://platform.openai.com/tokenizer) dan masukkan teks di sana. Kamu akan melihat bahwa teks bahasa Indonesia seringkali memakan *token* yang lebih banyak dibanding bahasa Inggris. Ini melatihmu untuk lebih efisien saat menyusun perintah.

---

## 2. Context Window (Batas Ingatan Jangka Pendek AI)

**Apa itu Context Window?**
Setiap AI punya batas maksimal jumlah *Token* yang bisa dia "ingat" dalam satu sesi percakapan. 
Misalnya, model GPT lama batasnya 4.096 token (sekitar 3.000 kata). Model terbaru seperti GPT-4o atau Gemini punya batas di atas 128.000 token.

**Dampak Praktis (Kenapa kamu harus peduli?):**
* **Amnesia AI (Lupa Konteks):** Pernahkah kamu ngobrol panjang dengan AI, lalu tiba-tiba AI memberikan jawaban yang melenceng atau melupakan aturan di awal obrolan? Itu karena percakapanmu sudah melampaui batas *Context Window*. Token terlama (pesan pertamamu) "terdorong" keluar dan dilupakan oleh mesin.
* **Mengurangi Halusinasi:** Kalau kamu mengunggah file `models.py` yang ukurannya raksasa ke dalam chat AI, AI bisa "mabuk" karena otaknya (context window) penuh, dan mulai menciptakan fungsi ORM yang tidak pernah ada di Odoo.

**Cara Membuktikan Kamu Paham:**
Kamu harus sadar kapan harus memulai **"New Chat"** (Percakapan Baru). Jika konteks masalah yang sedang kamu *debug* sudah berubah, atau chat sudah terlalu panjang dan AI mulai "ngaco", langsung buka chat baru dengan konteks (prompt) yang lebih segar.

---

## 3. Temperature (Tingkat Kreativitas AI)

**Apa itu Temperature?**
Ini adalah parameter pengatur (biasanya angka dari 0.0 sampai 2.0) yang mengontrol seberapa "acak" atau "kreatif" jawaban AI.

**Dampak Praktis (Kenapa kamu harus peduli?):**
* **Temperature Rendah (0.0 - 0.3):** Hasilnya deterministik (pasti), analitis, dan rasional. Jawaban AI akan kaku tapi akurat.
* **Temperature Tinggi (0.7 - 1.0+):** Hasilnya sangat variatif, kreatif, tapi rawan mengarang fakta (*halusinasi*).
* **Aturan Mainnya:** Saat kamu menggunakan AI untuk **coding Odoo**, menemukan *bug*, atau melakukan integrasi logika matematika, kamu **WAJIB** meminta jawaban dengan temperature rendah (atau mensettingnya ke `0.0` jika membuat skrip API) agar kode yang dihasilkan logis. Tetapi jika kamu meminta AI membuat *deskripsi fitur modul* untuk user, kamu bisa pakai temperature `0.7` agar bahasanya luwes.

---

## 🎯 Cara Membuktikan ke Lead/Reviewer (Achievement Poin A)

Jika Reviewer / Lead-mu bertanya, *"Apa yang kamu pahami tentang LLM Basics?"*, kamu cukup menjelaskan dengan sudut pandang *Developer*:

> *"Sebagai developer, saya paham bahwa men-generate kode AI butuh **Temperature** rendah (seperti 0.1) agar kodenya logis dan AI tidak berhalusinasi membuat ORM Odoo palsu. Saya juga tidak akan melakukan copy-paste file `.py` ribuan baris ke dalam chat AI, karena selain membuang-buang **Token** (biaya membengkak), itu bisa memenuhi batas **Context Window** yang akan membuat memori jangka pendek AI penuh dan tiba-tiba lupa instruksi awal saya."*
