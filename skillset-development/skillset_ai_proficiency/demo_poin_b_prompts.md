# CONTOH PRAKTIS (DEMO) POIN B: STRUCTURED PROMPTS

Berikut adalah perbandingan antara prompt acak (Buruk) vs prompt terstruktur (Baik) saat mendevelop Odoo. Kamu bisa *copy-paste* template yang Baik untuk keperluan pekerjaan sehari-harimu!

---

## ❌ CONTOH 1: Prompt Acak (Random Questioning) - JANGAN DILAKUKAN
> "Tolong benerin error ini dong: `ValueError: Expected singleton` di model absen."

*Kenapa Buruk?*
- AI tidak tahu struktur model absenmu (field-nya apa saja, nama modelnya apa).
- AI tidak tahu Odoo versi berapa (ORM Odoo 14 vs 19 bisa berbeda).
- AI tidak tahu potongan kode mana yang memicu error tersebut. 
- **Akibatnya:** AI akan membalas dengan penjelasan teoritis yang sangat panjang untuk menebak-nebak, membuang *token*, dan belum tentu menyelesaikan masalahmu.

---

## ✅ CONTOH 2: Prompt Terstruktur (Structured Prompt) - STANDAR BEGINNER POIN B

Kamu bisa menyimpan dan menggunakan *template* di bawah ini setiap kali meminta bantuan AI untuk Odoo:

```text
[CONTEXT / ROLE]
Bertindaklah sebagai Senior Odoo Developer. Saya sedang mendevelop modul Custom HR untuk Odoo 19.

[TASK]
Tolong bantu saya memperbaiki error `ValueError: Expected singleton` pada method `_compute_total_lembur()`. 
Tujuan method ini adalah menjumlahkan jam lembur dari relasi `One2many`.

[CODE / STRUCTURE]
Ini adalah potongan kode saya saat ini:
class HrLembur(models.Model):
    _name = 'hr.lembur'
    
    employee_id = fields.Many2one('hr.employee')
    lembur_line_ids = fields.One2many('hr.lembur.line', 'lembur_id')
    total_jam = fields.Float(compute='_compute_total_lembur')
    
    @api.depends('lembur_line_ids.jam')
    def _compute_total_lembur(self):
        # Error terjadi di baris bawah ini
        self.total_jam = sum(self.lembur_line_ids.mapped('jam'))

[ERROR LOG]
Traceback (most recent call last):
  File ".../models.py", line 12, in _compute_total_lembur
ValueError: Expected singleton: hr.lembur(1, 2)

[CONSTRAINTS / FORMAT]
1. Pastikan perbaikan tetap menggunakan standar ORM Odoo.
2. Jelaskan di mana letak kesalahan singleton saya (berkaitan dengan looping `for record in self`).
3. Berikan perbaikan kodenya saja secara ringkas.
```

---

## 🛠️ Cara Mencoba (Testing):
1. Buka AI favoritmu (ChatGPT / Claude / Copilot).
2. *Copy* isi template di **CONTOH 2** dan *Paste* ke kolom chat AI.
3. *Send* dan perhatikan jawabannya!
4. Bandingkan jika kamu hanya mengirimkan **CONTOH 1**. 

Kamu akan melihat bahwa prompt terstruktur membuat AI **langsung** menuju inti masalah, langsung menyuruhmu menaruh `for record in self:`, tanpa banyak berasumsi. Inilah yang disebut "Structured Prompting dengan Clear Intent"!
