# ==============================================================================
# CONTOH PRAKTIS (DEMO) POIN C: VALIDASI OUTPUT AI
# File ini bisa dibuka di VS Code untuk dipelajari
# ==============================================================================

# Skenario: 
# Kamu meminta AI membuat fungsi untuk menghapus semua karyawan
# yang statusnya 'resign' di Odoo.

# ---------------------------------------------------------
# ❌ KODE ASLI HASIL GENERATE AI (YANG HARAM DICOPAS BUTA)
# ---------------------------------------------------------
# AI seringkali berpikir seperti Python Engineer biasa, bukan Odoo Engineer.
# AI mungkin memberikan kode seperti ini:

"""
def delete_resigned_employees(self):
    # AI menyarankan SQL Raw karena dianggap lebih efisien
    self.env.cr.execute("DELETE FROM hr_employee WHERE status = 'resign'")
"""

# TANYA PADA DIRIMU: MENGAPA KODE DI ATAS BURUK (BUTUH VALIDASI)?
# 1. Bypass ORM: Menghapus data langsung dari SQL (`cr.execute`) akan melewati 
#    aturan keamanan (ir.rule) dan sistem hak akses (Access Rights) Odoo.
# 2. Tidak Memicu Trigger: Menghapus lewat SQL tidak akan memicu metode `unlink()` 
#    bawaan model, yang berarti data berelasi (seperti kontrak, absensi) bisa 
#    mengalami 'orphan record' (data nyangkut) dan memicu fatal error di masa depan.

# ---------------------------------------------------------
# ✅ KODE SETELAH DIVALIDASI & DIPERBAIKI OLEH DEVELOPER
# ---------------------------------------------------------
# Sebagai developer yang paham Poin C, kamu membaca kode AI,
# menyadari kesalahannya yang berbahaya, dan mengubahnya menjadi "The Odoo Way":

from odoo import models, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    def delete_resigned_employees(self):
        # 1. Validasi 1: Gunakan ORM Odoo search() agar record mematuhi Access Rights
        resigned_employees = self.search([('status', '=', 'resign')])
        
        # 2. Validasi 2: Gunakan metode bawaan ORM yaitu unlink()
        if resigned_employees:
            resigned_employees.unlink()
            
# ==============================================================================
# PEMBUKTIAN EXPLAINABILITY (KEMAMPUAN MENJELASKAN SECARA TEKNIS)
# ==============================================================================
#
# JIKA DITANYA LEAD SAAT CODE REVIEW: 
# "Kenapa kamu pakai ORM search dan unlink, padahal cr.execute bisa 1 baris beres?"
#
# JAWABANMU (Mencerminkan Poin C): 
# "Karena execute akan me-bypass aturan keamanan (ir.rule) Odoo. Jika memakai 
# unlink() dari ORM, sistem akan memastikan semua dependensi atau fungsi bawaan 
# ter-trigger dengan aman tanpa membuat data menjadi 'orphan'."
# 
# (Inilah bukti nyata pencapaian Poin C: Can explain technically why it works!)
