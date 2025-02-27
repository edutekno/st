OPENROUTER_API_KEY = "sk-or-v1-"
BASE_URL = "https://openrouter.ai/api/v1"  # Base URL untuk OpenRouter
MODEL = "mistralai/pixtral-12b"  # Model default untuk image-to-text
HTTP_REFERER = ""  # Opsional: URL situs Anda
X_TITLE = ""  # Opsional: Nama situs Anda

import streamlit as st
import openai
import base64
from PIL import Image
import io

# Konfigurasi OpenAI Client
openai.api_base = BASE_URL
openai.api_key = OPENROUTER_API_KEY

# Judul aplikasi
st.title("Aplikasi Image-to-Text")

# Deskripsi aplikasi
st.write("""
    Selamat datang di aplikasi Image-to-Text! 
    Unggah gambar, tuliskan instruksi Anda, dan AI akan menafsirkan isi gambar sesuai dengan instruksi tersebut.
""")

# Input pengguna untuk unggah gambar
uploaded_file = st.file_uploader("Unggah Gambar", type=["jpg", "jpeg", "png"])

# Input teks untuk prompt instruksi
user_prompt = st.text_input("Tuliskan instruksi untuk memproses gambar (contoh: 'Jelaskan apa yang ada di gambar ini')", 
                            value="Jelaskan apa yang ada di gambar ini")

# Fungsi untuk mengonversi gambar menjadi Base64
def image_to_base64(image_file):
    try:
        # Baca file gambar dan konversi ke Base64
        image_bytes = image_file.read()
        base64_encoded = base64.b64encode(image_bytes).decode("utf-8")
        return f"data:image/jpeg;base64,{base64_encoded}"
    except Exception as e:
        st.error(f"Error saat mengonversi gambar ke Base64: {str(e)}")
        return None

# Fungsi untuk mendapatkan interpretasi dari AI
def get_image_interpretation(image_url, prompt):
    try:
        completion = openai.ChatCompletion.create(
            headers={
                "HTTP-Referer": HTTP_REFERER,  # Opsional: URL situs Anda
                "X-Title": X_TITLE,  # Opsional: Nama situs Anda
            },
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt  # Gunakan prompt yang dimasukkan oleh pengguna
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        }
                    ]
                }
            ]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Tombol untuk memproses gambar
if uploaded_file is not None:
    st.image(uploaded_file, caption="Gambar yang Diunggah", use_column_width=True)
    if st.button("Submit"):
        with st.spinner("Memproses gambar..."):
            # Konversi gambar ke Base64
            image_url = image_to_base64(uploaded_file)
            if image_url:
                # Dapatkan interpretasi dari AI menggunakan prompt pengguna
                interpretation = get_image_interpretation(image_url, user_prompt)
                st.success("Interpretasi dari AI:")
                st.write(interpretation)
