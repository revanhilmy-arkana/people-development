# ==============================================================================
# CONTOH PRAKTIS (DEMO) POIN D: FUNCTION CALLING
# ==============================================================================
# Skrip ini mendemonstrasikan konsep dasar bagaimana AI bisa "memanggil"
# fungsi Python buatanmu (mirip dengan bagaimana ia akan memanggil ORM Odoo).
# 
# Pre-requisite jika ingin dijalankan betulan: pip install openai
# (Tapi kamu bisa membacanya saja untuk memahami alurnya!)

import json

# ------------------------------------------------------------------------------
# 1. FUNGSI LOKAL KITA (Ini yang nanti akan diganti dengan fungsi ORM Odoo)
# ------------------------------------------------------------------------------
def get_sisa_cuti(nama_karyawan):
    """
    Fungsi dummy yang mensimulasikan pencarian sisa cuti ke database.
    """
    print(f"\n[SYSTEM] Eksekusi fungsi lokal: Mencari data cuti '{nama_karyawan}' ke database...")
    database_dummy = {
        "budi": 12,
        "andi": 5,
        "siti": 0
    }
    sisa = database_dummy.get(nama_karyawan.lower(), "Tidak ditemukan")
    return sisa


# ------------------------------------------------------------------------------
# 2. DEFINISI TOOLS UNTUK AI (JSON Schema)
# ------------------------------------------------------------------------------
# Kita harus memberi tahu AI "Buku Panduan" tentang fungsi apa saja yang kita punya.
tools_untuk_ai = [
    {
        "type": "function",
        "function": {
            "name": "get_sisa_cuti",
            "description": "Ambil jumlah sisa cuti tahunan seorang karyawan berdasarkan namanya.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nama_karyawan": {
                        "type": "string",
                        "description": "Nama depan karyawan, misal: Budi"
                    }
                },
                "required": ["nama_karyawan"]
            }
        }
    }
]

# ------------------------------------------------------------------------------
# 3. ALUR KERJA FUNCTION CALLING (Simulasi)
# ------------------------------------------------------------------------------
def simulasi_function_calling():
    print("USER: 'Tolong cek dong, Budi masih punya sisa cuti berapa hari?'")
    
    # NORMALNYA DI SINI KITA MEMANGGIL API OPENAI:
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": "Tolong cek dong, Budi masih punya sisa cuti berapa hari?"}],
    #     tools=tools_untuk_ai,    <--- KITA KIRIMKAN 'BUKU PANDUAN' TADI KE AI
    # )
    
    # Karena kita mengirimkan 'tools', AI tidak akan menjawab dengan teks, 
    # melainkan AI akan membalas dengan instruksi (JSON) seperti ini:
    ai_response_mock = {
        "tool_calls": [
            {
                "function": {
                    "name": "get_sisa_cuti",
                    "arguments": '{"nama_karyawan": "Budi"}'
                }
            }
        ]
    }
    print(f"\nAI: Saya tidak tahu jawabannya, tapi saya butuh bantuanmu menjalankan fungsi ini:")
    print(json.dumps(ai_response_mock, indent=2))
    
    # 4. KODE KITA MEMBACA INSTRUKSI AI LALU MENGEKSEKUSINYA LOKAL
    tool_call = ai_response_mock["tool_calls"][0]
    nama_fungsi = tool_call["function"]["name"]
    argumen_json = json.loads(tool_call["function"]["arguments"])
    
    if nama_fungsi == "get_sisa_cuti":
        # Jalankan fungsi lokal kita!
        hasil_database = get_sisa_cuti(argumen_json["nama_karyawan"])
        print(f"[SYSTEM] Hasil dari database: {hasil_database}")
        
        # 5. KITA KIRIM KEMBALI HASIL INI KE AI
        print("\n[SYSTEM] Mengirim hasil ini kembali ke AI agar ia bisa merangkai jawaban...")
        
        # Simulasi AI membalas akhir ke user:
        print("\nAI FINAL RESPONSE: 'Berdasarkan data sistem, sisa cuti Budi saat ini adalah 12 hari.'")


if __name__ == "__main__":
    simulasi_function_calling()
    
    print("\n==============================================================")
    print("Dengan memahami skrip ini, kamu sudah menguasai teori Poin D!")
    print("Untuk praktiknya, cobalah membuat skrip asli dengan API Key OpenAI-mu")
    print("lalu commit ke Github/Gitlab agar tercatat sebagai portofolio.")
    print("==============================================================")
