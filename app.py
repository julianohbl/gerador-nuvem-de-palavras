import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height= 800, background_color="white").generate(text)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    image_buffer = io.BytesIO()
    plt.savefig(image_buffer, format="png")
    image_buffer.seek(0)

    return image_buffer

def main():
    st.title("Nuvem de Palavras a partir de Texto")

    uploaded_file = st.file_uploader("Faça o upload de um arquivo de texto", type=["txt"])

    if uploaded_file is not None:
        st.write("Arquivo carregado com sucesso!")

        text = uploaded_file.read().decode("utf-8")

        st.subheader("Texto carregado:")
        st.write(text)

        if st.button("Gerar Nuvem de Palavras"):
            image_buffer = generate_wordcloud(text)

            st.subheader("Nuvem de Palavras Gerada:")
            st.image(image_buffer, use_column_width="True", caption="Nuvem de Palavras")

if __name__ == "__main__":
    main()
    
