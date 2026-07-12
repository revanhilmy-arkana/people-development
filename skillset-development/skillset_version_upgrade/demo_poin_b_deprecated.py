# ==============================================================================
# CONTOH PRAKTIS (DEMO) POIN B: FIXING DEPRECATED METHODS
# ==============================================================================

from odoo import models, fields, api

# ---------------------------------------------------------
# ❌ KODE VERSI LAMA (Misal modul dari Odoo 14-16)
# ---------------------------------------------------------
class CustomEmployeeOld(models.Model):
    _inherit = 'hr.employee'
    
    # Dulu, untuk mengubah format nama yang muncul di dropdown (misal "Budi - IT"),
    # kita wajib meng-override fungsi bawaan `name_get()`.
    
    def name_get(self):
        result = []
        for record in self:
            # Menggabungkan nama karyawan dan nama departemennya
            name = f"{record.name} - {record.department_id.name}"
            result.append((record.id, name))
        return result

# ---------------------------------------------------------
# ✅ KODE VERSI BARU (Odoo 17/18/19) -> HASIL REFACTOR UPGRADE KITA
# ---------------------------------------------------------
# Jika kamu membawa kode di atas ke Odoo versi baru, log server akan teriak: 
# WARNING: name_get() is deprecated!
# 
# Sebagai Beginner yang menguasai Poin B, kamu harus mencari tahu fungsi penggantinya,
# dan mengubah KESELURUHAN logikanya dengan BENAR seperti di bawah ini:

class CustomEmployeeNew(models.Model):
    _inherit = 'hr.employee'
    
    # Di versi baru, Odoo membuang name_get() dan menggantinya dengan mekanisme compute
    # pada field `display_name`. Pendekatan ini jauh lebih cepat (dioptimasi oleh cache ORM).
    
    @api.depends('name', 'department_id.name')
    def _compute_display_name(self):
        for record in self:
            if record.department_id:
                record.display_name = f"{record.name} - {record.department_id.name}"
            else:
                record.display_name = record.name

# ==============================================================================
# KESIMPULAN:
# "Fixes deprecated methods correctly" artinya kamu:
# 1. Tahu dan peka bahwa fungsi lama sudah tidak boleh dipakai (lewat log terminal).
# 2. Mau riset / bertanya untuk mencari fungsi pengganti resminya.
# 3. Mampu merombak total struktur logikanya (seperti contoh di atas: dari 
#    me-return sebuah List of Tuples di `name_get`, menjadi mekanisme assignment
#    variabel biasa di `_compute_display_name`) agar 100% mematuhi aturan versi baru!
