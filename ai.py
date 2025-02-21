# app.py

import streamlit as st
import requests

# Judul aplikasi
st.title("FAQ AI Sederhana dengan API PHP")

# Input URL API PHP
api_url = st.text_input("Masukkan URL API PHP:", "https://rumahguru.org/api/index.php")

# Input pertanyaan dari pengguna
pertanyaan = st.text_area("Masukkan pertanyaan Anda:")

# Input sistem (opsional)
system_message = st.text_input("Pesan sistem (opsional):", "")

# Tombol untuk mengirim pertanyaan
if st.button("Kirim Pertanyaan"):
    if not api_url:
        st.error("Silakan masukkan URL API PHP terlebih dahulu.")
    elif not pertanyaan:
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
                response = requests.post(api_url, json=payload)
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
