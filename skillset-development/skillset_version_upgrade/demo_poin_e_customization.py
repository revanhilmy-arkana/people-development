# ==============================================================================
# CONTOH PRAKTIS (DEMO) POIN E: AVOIDING DEEP CUSTOMIZATION
# File Python ini dapat dipelajari (dibaca) langsung di VS Code.
# ==============================================================================

# Skenario: 
# Klien meminta agar setiap kali ada Data Karyawan baru yang di-input, 
# namanya harus otomatis dikonversi menjadi HURUF KAPITAL (Uppercase).

# ---------------------------------------------------------
# ❌ KODE BURUK: KUSTOMISASI MENDALAM (Nightmare for Upgrade)
# ---------------------------------------------------------
from odoo import models, api

class HrEmployeeBad(models.Model):
    _inherit = 'hr.employee'
    
    # Si Developer Awam memilih cara brutal dengan meng-override fungsi 
    # inti database Odoo yaitu create() dan write(). Ini adalah "Deep Customization".
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'name' in vals:
                vals['name'] = vals['name'].upper()
        # BAHAYA: Jika Odoo versi baru mengubah susunan parameter 'vals_list' 
        # pada fungsi create(), kode di bawah ini akan HANCUR TOTAL (Crash).
        return super(HrEmployeeBad, self).create(vals_list)

    def write(self, vals):
        if 'name' in vals:
            vals['name'] = vals['name'].upper()
        # BAHAYA: Sangat rawan bentrok (konflik) dengan modul Odoo lain 
        # yang juga tidak sengaja meng-override fungsi write() ini.
        return super(HrEmployeeBad, self).write(vals)


# ---------------------------------------------------------
# ✅ KODE BAIK: THE ODOO WAY (Upgrade-Safe) -> POIN E ACHIEVED
# ---------------------------------------------------------
# Developer yang menguasai Poin E akan memutar otak untuk menghindari 
# memodifikasi fungsi inti database. Ia akan menggunakan fitur "Onchange" 
# standar Odoo yang sangat ringan, terisolasi, dan aman.

class HrEmployeeGood(models.Model):
    _inherit = 'hr.employee'

    # Solusi Brilian: Hanya dengan 3 baris kode!
    # - Tidak perlu menyentuh fungsi inti database (create/write).
    # - 100% AMAN (Upgrade-Safe) jika Odoo berubah versi ke depan.
    # - Lebih ramah user (UX) karena nama akan langsung berubah kapital 
    #   di layar (User Interface) seketika saat user selesai mengetik.
    
    @api.onchange('name')
    def _onchange_name_uppercase(self):
        if self.name:
            self.name = self.name.upper()


# ==============================================================================
# KESIMPULAN POIN E:
# Kode yang HEBAT bukanlah kode yang sangat panjang dan terlihat rumit.
# Kode yang HEBAT adalah kode yang menyelesaikan masalah klien dengan baris 
# paling sedikit, paling menempel pada standar (The Odoo Way), dan paling aman 
# (Upgrade-Safe) untuk dikembangkan di masa depan.
