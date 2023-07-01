import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title = 'EDA',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

def run():

    col1, col2, col3 = st.columns([1, 5, 1])
    with col1:
        st.write("")
    with col2:
        st.title('Exploratory Data Analysis (EDA)')
        st.subheader('EDA Komposisi-Kekuatan Beton')
        st.write('Dibuat Oleh: **Mangara Haposan Immanuel Siagian**')
        image = Image.open('deployment/concrete.jpg')
        st.image(image, caption=' ')
    with col3:
        st.write("")

    st.markdown('---')

    st.write('### Defenisi')
    st.write('Dalam konstruksi, beton adalah sebuah bahan bangunan komposit yang terbuat dari kombinasi aggregat dan pengikat semen. Bentuk paling umum dari beton adalah beton semen Portland, yang terdiri dari agregat mineral (biasanya kerikil dan pasir), semen dan air.')
    st.write('[Referensi](https://id.wikipedia.org/wiki/Beton)')

    st.markdown('---')

    data_m = pd.read_csv('deployment/h8dsft_P1M2_Mangara_Siagian.csv')
    data123 = data_m.dropna()
    data = data123.drop_duplicates()

    # Menampilkan dataset
    st.write('### Data')
    st.write(data.head())

    # Menampilkan ringkasan statistik dataset
    st.write('### Statistik')
    st.write(data.describe())

    # Menampilkan visualisasi distribusi data
    st.write('### Visualisasi Distribusi Data')
    column = st.selectbox('Pilih kolom', data.columns)
    fig, ax = plt.subplots()
    sns.histplot(data[column], kde=True)
    st.pyplot(fig)

    # Menampilkan korelasi antar fitur
    st.write('### Korelasi Antar Fitur')
    corr_method = st.radio('Metode Korelasi', ('Pearson', 'Spearman'))
    fig, ax = plt.subplots()
    if corr_method == 'Pearson':
        corr_matrix = data.corr(method='pearson')
    else:
        corr_matrix = data.corr(method='spearman')
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    st.pyplot(fig)

    # Menampilkan visualisasi data lainnya
    st.write('### Visualisasi Antar Data')
    plot_type = st.selectbox('Pilih jenis visualisasi', ('Barplot', 'Boxplot', 'Scatterplot'))
    if plot_type == 'Barplot':
        x_col = st.selectbox('Pilih kolom x', data.columns)
        y_col = st.selectbox('Pilih kolom y', data.columns)
        fig, ax = plt.subplots()
        sns.barplot(x=data[x_col], y=data[y_col])
        st.pyplot(fig)
    elif plot_type == 'Boxplot':
        x_col = st.selectbox('Pilih kolom x', data.columns)
        y_col = st.selectbox('Pilih kolom y', data.columns)
        fig, ax = plt.subplots()
        sns.boxplot(x=data[x_col], y=data[y_col])
        st.pyplot(fig)
    elif plot_type == 'Scatterplot':
        x_col = st.selectbox('Pilih kolom x', data.columns)
        y_col = st.selectbox('Pilih kolom y', data.columns)
        fig, ax = plt.subplots()
        sns.scatterplot(x=data[x_col], y=data[y_col])
        st.pyplot(fig)

if __name__ == '__main__':
    run()