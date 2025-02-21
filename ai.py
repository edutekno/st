# app.py

import streamlit as st
import requests

# Judul aplikasi
st.title("FAQ AI")

# URL API PHP sebagai konstanta
API_URL = "https://rumahguru.org/api/index.php"

# Input sistem (opsional)
system_message = st.text_input("Pesan sistem (opsional):", "")

# Input pertanyaan dari pengguna
pertanyaan = st.text_area("Masukkan pertanyaan Anda:")

# Tombol untuk mengirim pertanyaan
if st.button("Kirim Pertanyaan"):
    if not pertanyaan:
        st.error("Silakan masukkan pertanyaan terlebih dahulu.")
    else:
        # Payload untuk permintaan POST
        payload = {
            "prompt": pertanyaan
        }
        if system_message:
            payload["system"] = system_message

        try:
            # Menampilkan loading spinner
            with st.spinner("Mengirim permintaan dan menunggu respons..."):
                # Mengirim permintaan POST ke API PHP
                response = requests.post(API_URL, json=payload)
                response.raise_for_status()  # Memastikan tidak ada error HTTP

            # Mengambil jawaban dari respons API
            data = response.json()
            if "text" in data:
                st.success("Jawaban:")
                st.write(data["text"])
            elif "error" in data:
                st.error(f"Error: {data['error']}")
            else:
                st.warning("Respons tidak valid dari API.")

        except requests.exceptions.RequestException as e:
            st.error(f"Terjadi kesalahan saat memanggil API: {e}")
