# AI Proficiency - Beginner (Poin E)

**Poin E:**
> *"Uses AI for acceleration without bypassing architecture thinking."*
> (Menggunakan AI untuk akselerasi (kecepatan) tanpa mengabaikan pemikiran arsitektural.)

Poin terakhir di level *Beginner* ini adalah murni tentang **Mindset (Pola Pikir)**. AI diciptakan untuk mempercepat pekerjaan pengetikanmu (akselerasi), **bukan** untuk menggantikan peran otakmu sebagai *Software Architect*.

---

## 1. Apa Maksudnya "Bypassing Architecture Thinking"?

Ini adalah kebiasaan buruk (*anti-pattern*) di mana seorang developer langsung membuka ChatGPT begitu mendapat tiket tugas, lalu mengetik: *"Buatkan saya modul Odoo untuk fitur X lengkap dari awal sampai akhir"*, lalu me-*copy-paste* semua kodenya ke *workspace* tanpa memikirkannya.

**Mengapa hal itu sangat berbahaya?**
- AI akan memilih jalan termudah menurutnya (misal: AI akan membuat model baru dari nol, padahal di Odoo jauh lebih elegan jika kita melakukan *Inheritance* `_inherit` pada model yang sudah ada).
- AI tidak tahu *coding guidelines* perusahaanmu (Arkana) dan tidak tahu keterkaitan antar-modul di *workspace*-mu.
- Jika di masa depan ada *bug* atau klien meminta perubahan (*Change Request*), kamu akan kesulitan besar karena fondasi relasi *database*-nya bukan buatanmu sendiri.

---

## 2. Bagaimana "The Right Way" (Jalan yang Benar)?

Gunakan AI murni sebagai **Akselerator (Asisten Sintaks)**. Alur kerja seorang profesional harus seperti ini:

1. **Berpikir Arsitektur (Fase Kamu):** Saat mendapat tugas, jangan sentuh *keyboard* dulu. Pikirkan: *"Saya butuh tabel apa? Relasinya `Many2one` atau `One2many`? Apakah saya harus *inherit* view bawaan atau buat view baru?"*
2. **Delegasi ke AI (Fase Akselerasi):** Setelah desain arsitekturnya tergambar jelas di kepalamu, barulah kamu menyuruh AI mengetikkannya agar cepat. *(Misal: "Saya mau inherit hr.employee, tolong generate boilerplate XML-nya dengan field X dan Y di dalam halaman Notebook.")*
3. **Validasi (Fase Poin C):** Periksa kembali hasil ketikan AI tersebut sebelum di-*commit*.

---

## 🎯 Cara Membuktikan ke Lead/Reviewer (Achievement Poin E)

Kamu bisa membuktikan bahwa kamu menguasai poin ini dengan menunjukkan bahwa kamu selalu mendahulukan **Desain Modul** sebelum mulai menulis kode bersama AI.

Jika Reviewer / Lead bertanya saat evaluasi: *"Bagaimana perlakuanmu terhadap kode buatan AI?"*
Jawaban pamungkasmu:
> *"Saya menjadikan AI sebagai asisten pengetikan (akselerator) agar saya tidak perlu hafal semua *tag* XML Odoo. Namun, untuk keputusan arsitektural seperti kapan harus pakai `_inherit`, kapan harus buat model `_name` baru, atau bagaimana desain relasi databasenya, keputusan itu 100% berasal dari pemikiran saya yang disesuaikan dengan best-practice Odoo. AI hanya mengikuti cetak biru (blueprint) saya."*
