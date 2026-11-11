
import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
import imageio.v2 as imageio
import math
import os

st.set_page_config(
    page_title="Para mi gruñoncito ❤️",
    page_icon="❤️",
    layout="centered"
)

# Crear animación del corazón
def crear_corazon():
    frames = []
    ancho, alto = 500, 350

    for i in range(24):
        escala = 1 + 0.15 * math.sin(i * 2 * math.pi / 24)

        img = Image.new("RGB", (ancho, alto), "#FFF0F5")
        draw = ImageDraw.Draw(img)

        puntos = []
        for t in np.linspace(0, 2 * math.pi, 150):
            x = 16 * math.sin(t)**3
            y = (13 * math.cos(t) - 5 * math.cos(2*t)
                 - 2 * math.cos(3*t) - math.cos(4*t))

            px = ancho/2 + x * 9 * escala
            py = alto/2 - y * 9 * escala
            puntos.append((px, py))

        draw.polygon(puntos, fill="#E91E63")
        frames.append(np.array(img))

    imageio.mimsave(
        "corazon.mp4",
        frames,
        fps=12,
        codec="libx264",
        quality=8
    )

if not os.path.exists("corazon.mp4"):
    crear_corazon()

# Presentación
st.markdown("# ❤️ Hola, mi gruñoncito ❤️")

st.video(
    "corazon.mp4",
    loop=True,
    autoplay=True,
    muted=True
)

st.markdown("""
### 💗 Una dedicatoria para ti

Gracias por ser esa persona maravillosa
que eres.

Diosito no se equivocó en mandarte a este
mundo.

Eres una persona maravillosa y le pido
a Dios que siempre te bendiga.

### ❤️ TE AMO MUCHO ❤️

# MI GRUÑONCITO 💕
""")
