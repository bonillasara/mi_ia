import streamlit as st
import google.generativeai as genai
from PIL import Image

# actualizacion

# Pega tu API Key aquí
api_key = "AIzaSyDHudr4qxWfZe-SrQGmaq7n6E4T6gi4Yvk"

genai.configure(api_key=api_key)
modelo = genai.GenerativeModel('gemini-2.5-flash')

st.set_page_config(page_title="Geo-Bot", page_icon="📐")
st.title("📐 Geo-Bot: Resuelve tu tarea")

st.info("Escribe aquí tu problema:")
texto_usuario = st.text_area("Ejemplo: área de un círculo con radio 5")

st.write("---")

st.info("O sube una imagen:")
imagen_input = st.file_uploader("Sube una imagen", type=["jpg", "png", "jpeg"])
imagen = None

if imagen_input:
    imagen = Image.open(imagen_input)

if st.button("Resolver"):
    if not texto_usuario and not imagen:
        st.warning("Escribe algo o sube una imagen")
    else:
        with st.spinner("Pensando..."):
            try:
                prompt = "Eres un profesor de geometría. Explica paso a paso."

                contenido = [prompt]

                if texto_usuario:
                    contenido.append(texto_usuario)

                if imagen:
                    st.image(imagen)
                    contenido.append(imagen)

                respuesta = modelo.generate_content(contenido)

                st.success("Resultado:")
                st.write(respuesta.text)

            except Exception as e:
                st.error(f"Error: {e}")
