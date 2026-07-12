# ==============================================================================
# DEMO AI PROFICIENCY - BEGINNER (POIN A)
# Topik: Memahami Token dan Temperature secara Praktis
# ==============================================================================

import os

try:
    import tiktoken
except ImportError:
    print("Modul 'tiktoken' belum terinstal. Silakan jalankan: pip install tiktoken")
    exit(1)

def demo_tokenizer():
    print("=== 1. DEMO MENGHITUNG TOKEN ===")
    print("Kita akan membandingkan jumlah token antara teks Bahasa Inggris dan Bahasa Indonesia.\n")
    
    # Menggunakan encoding untuk model GPT-3.5/GPT-4 (cl100k_base)
    encoding = tiktoken.get_encoding("cl100k_base")
    
    teks_inggris = "Odoo is an open-source enterprise resource planning software."
    teks_indo = "Odoo adalah perangkat lunak perencanaan sumber daya perusahaan berbasis sumber terbuka."
    
    token_inggris = encoding.encode(teks_inggris)
    token_indo = encoding.encode(teks_indo)
    
    print(f"Teks Inggris  : '{teks_inggris}'")
    print(f"Jumlah Karakter : {len(teks_inggris)}")
    print(f"Jumlah Token  : {len(token_inggris)}")
    print(f"Detail Token  : {token_inggris}\n")
    
    print(f"Teks Indo     : '{teks_indo}'")
    print(f"Jumlah Karakter : {len(teks_indo)}")
    print(f"Jumlah Token  : {len(token_indo)}")
    print(f"Detail Token  : {token_indo}\n")
    
    print("=> Kesimpulan: Teks Bahasa Indonesia (dan bahasa non-Inggris lainnya)")
    print("   biasanya memakan token lebih banyak karena AI dilatih mayoritas")
    print("   menggunakan dataset Bahasa Inggris.\n")


def demo_temperature_concept():
    print("=== 2. DEMO PENGATURAN TEMPERATURE (KONSEP) ===")
    print("Jika kamu menggunakan API OpenAI di Python, beginilah cara menyetel Temperature.")
    print("Ini adalah contoh template fungsi yang biasa dipakai developer:\n")
    
    kode_contoh = """
import openai

def dapatkan_jawaban_ai(prompt, kasus_penggunaan="coding"):
    # Menentukan temperature berdasarkan use case
    if kasus_penggunaan == "coding":
        # Untuk coding / logic, temperature harus 0 agar tidak halusinasi
        suhu = 0.0
    elif kasus_penggunaan == "marketing":
        # Untuk membuat deskripsi produk, temperature dinaikkan agar kreatif
        suhu = 0.7
        
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=suhu,     <--- DI SINI KITA MENGATURNYA
        max_tokens=500        <--- BATAS MAKSIMAL TOKEN BALASAN
    )
    return response.choices[0].message.content
"""
    print(kode_contoh)
    print("=> Kesimpulan: Sebagai developer, kamu memegang kendali atas parameter 'temperature'.")
    print("   Pastikan kamu paham kapan harus memakai 0.0 dan kapan harus memakai 0.7+.")


if __name__ == "__main__":
    demo_tokenizer()
    demo_temperature_concept()
    print("\n--- Selesai ---")
    print("Coba ubah teks di atas dengan copas baris kode Odoo, lalu lihat berapa jumlah tokennya!")
