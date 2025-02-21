# app.py

import streamlit as st
import requests

# Judul aplikasi
st.title("FAQ AI Sederhana dengan Groq")

# Input API Key Groq
api_key = st.text_input("Masukkan API Key Groq Anda:", type="password")

# Input pertanyaan dari pengguna
pertanyaan = st.text_area("Masukkan pertanyaan Anda:")

# Tombol untuk mengirim pertanyaan
if st.button("Kirim Pertanyaan"):
    if not api_key:
        st.error("Silakan masukkan API Key Groq terlebih dahulu.")
    elif not pertanyaan:
        st.error("Silakan masukkan pertanyaan terlebih dahulu.")
    else:
        # Endpoint API Groq
        url = "https://api.groq.com/openai/v1/chat/completions"  # Ganti dengan endpoint yang sesuai
        
        # Header untuk autentikasi
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Payload untuk permintaan API
        payload = {
            "prompt": pertanyaan,
            "max_tokens": 100,  # Batas panjang jawaban
            "temperature": 0.7  # Tingkat kreativitas model
        }
        
        # Mengirim permintaan ke API Groq
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Memastikan tidak ada error HTTP
            
            # Mengambil jawaban dari respons API
            data = response.json()
            jawaban = data.get("choices", [{}])[0].get("text", "").strip()
            
            if jawaban:
                st.success("Jawaban:")
                st.write(jawaban)
            else:
                st.warning("Tidak ada jawaban yang diterima dari API.")
        
        except requests.exceptions.RequestException as e:
            st.error(f"Terjadi kesalahan saat memanggil API: {e}")
