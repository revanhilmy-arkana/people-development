# AI Proficiency - Beginner (Poin B)

**Poin B:**
> *"Writes structured prompts with clear intent, not random questioning."*
> (Menulis prompt terstruktur dengan tujuan yang jelas, bukan sekadar bertanya secara acak.)

Untuk menguasai poin ini, kamu harus merubah kebiasaan dari sekadar "ngobrol" dengan AI menjadi "memberi instruksi" (Prompt Engineering) kepada AI.

---

## 1. Apa yang Perlu Dipelajari? (Structured Prompting)

Kamu perlu mempelajari cara menyusun kerangka prompt (*Prompt Framework*). Salah satu framework yang paling populer untuk developer adalah **CTF (Context, Task, Format)** atau **R-T-F (Role, Task, Format)**.

*   **Role / Context (Peran & Konteks):** Beri tahu AI siapa dia dan apa lingkungan kerjanya. *(Misal: "Bertindaklah sebagai Senior Odoo Developer. Saya menggunakan Odoo 19.")*
*   **Task (Tugas Utama):** Jelaskan masalahnya secara spesifik. *(Misal: "Bantu saya membuat method compute untuk menghitung total cuti yang terpakai.")*
*   **Format / Constraint (Batasan & Aturan):** Berikan aturan teknis yang tidak boleh dilanggar. *(Misal: "Gunakan `@api.depends`, jangan jalankan `env.cr.execute` (SQL Raw), dan outputnya format Markdown.")*

**Mengapa ini penting?**
Jika kamu bertanya secara acak (*random questioning*) seperti: *"Kenapa kodingan absenku error?"*, AI akan menebak-nebak (halusinasi). AI tidak tahu Odoo versi berapa, modul apa, dan struktur databasenya seperti apa.

---

## 2. Apa yang Perlu Dilakukan? (Action Plan)

1.  **Stop Bertanya 1 Baris:** Jangan pernah mengirim pesan 1 kalimat ke AI saat debugging. Selalu gunakan format *multi-line* terstruktur.
2.  **Sertakan 3 Elemen Wajib Odoo:** Saat bertanya tentang *bug* atau fitur Odoo, selalu tuliskan:
    *   Versi Odoo (Odoo 18 / 19).
    *   Konteks Model (potongan nama `_name` dan *fields* yang relevan).
    *   *Traceback Error* (Log Error lengkap dari terminal).
3.  **Biasakan Pakai Template Prompt:** Simpan sebuah *template prompt* di VS Code atau catatanmu (contohnya ada di file `demo_poin_b_prompts.md` yang saya buatkan).

---

## 🎯 Cara Membuktikan ke Lead/Reviewer (Achievement Poin B)

Kamu bisa membuktikan bahwa kamu menguasai poin ini dengan menunjukkan riwayat percakapan ChatGPT / Claude / Gemini-mu kepada reviewer, sambil menjelaskan:

> *"Saat menghadapi bug, saya tidak lagi bertanya secara acak. Saya selalu menggunakan **Prompt Terstruktur**. Saya menyebutkan konteks (versi Odoo 19), menyertakan batasan (contoh: harus menggunakan standar ORM bukan Python bawaan), dan melampirkan log error seperlunya. Ini membuat jawaban AI jauh lebih presisi dan menghemat token."*
