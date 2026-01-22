import streamlit as st

def about_dataset():
    link = "https://img.antaranews.com/cache/1200x800/2022/07/13/tanggul-muara-baru-2.jpg.webp"
    st.image(
    link,
    caption="Tanggul Beton Jakarta Utara",
    use_container_width=True
    )

    st.markdown(
    """
    <p style="text-align: justify;">
    Wilayah pesisir Jakarta Utara secara konsisten menghadapi permasalahan banjir 
    pesisir dan banjir rob yang dipicu oleh interaksi antara curah hujan, kondisi
    daratan, dan dinamika atmosfer pesisir. Pembangunan tanggul pesisir yang dimulai 
    pada tahun 2014 ditujukan untuk mengurangi dampak banjir, namun hingga saat ini 
    evaluasi kuantitatif terhadap efektivitas infrastruktur tersebut masih terbatas 
    dan umumnya bergantung pada data kejadian banjir yang tidak terstandarisasi.
    </p>

    <p style="text-align: justify;">
    Penelitian ini bertujuan untuk mengevaluasi perubahan potensi banjir pesisir 
    di Jakarta Utara sebelum dan sesudah pembangunan tanggul menggunakan pendekatan 
    berbasis data hidrometeorologi. Analisis difokuskan pada pembentukan Flood Potential
    Index sebagai indikator kuantitatif yang merepresentasikan kondisi potensi banjir secara 
    temporal. Melalui pendekatan ini, penelitian berupaya memberikan gambaran objektif mengenai
    efektivitas kebijakan pengendalian banjir pesisir.
    </p>

    
    <p style="text-align: justify;">
    Metode yang digunakan mencakup pemanfaatan data 
    <a href="https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land-timeseries?tab=download" target="_blank">
    <b>reanalysis ERA5-Land</b></a>
    yang diolah menjadi data harian dan digunakan untuk membentuk Flood Potential Index berbasis 
    Principal Component Analysis. PCA diterapkan
    untuk menggabungkan variabel curah hujan, kelembapan tanah permukaan, dan kecepatan angin secara objektif 
    berdasarkan struktur variansi data. Analisis dibedakan ke dalam dua periode, yaitu periode sebelum pembangunan 
    tanggul pesisir yang didefinisikan hingga 9 Oktober 2014 dan periode setelah pembangunan tanggul yang dimulai sejak
    tanggal tersebut. Selanjutnya, perbedaan kondisi potensi banjir antara kedua periode dianalisis menggunakan pendekatan
    statistik komparatif untuk menilai signifikansi perubahan yang terjadi.
    </p>
    """,
    unsafe_allow_html=True
    )
    # variabel TP
    st.header("Variabel yang Digunakan")
    st.subheader("1. Total Precipitation (TP)")

    st.markdown(
        """
        <p style='text-align: justify;'>
        <strong>Jenis variabel:</strong> Hidrometeorologi (Curah hujan).
        </p>

        <p style='text-align: justify;'>
        Total Precipitation (TP) merepresentasikan jumlah akumulasi curah hujan yang turun pada suatu wilayah dalam periode 
        waktu tertentu. Variabel ini menjadi indikator utama ketersediaan air permukaan karena hujan yang tinggi dapat meningkatkan 
        limpasan (runoff) ketika kapasitas infiltrasi tanah terlampaui. Oleh karena itu, TP memiliki peran signifikan dalam memicu 
        kejadian banjir, terutama pada wilayah dengan sistem drainase yang terbatas <sup>[1][3]</sup>.
        </p>
        """,
        unsafe_allow_html=True
    )

    # VARIABEL SWVL1
    st.subheader('2. Soil Water Volume Layer 1 (SWVL1)')
    st.markdown("""
    <p style='text-align: justify;'>
    <strong>Jenis variabel:</strong> Hidrologi tanah (Kelembapan tanah lapisan atas)
    </p>
    <p style='text-align: justify;'>
    Soil Water Volume Layer 1 (SWVL1) menunjukkan kandungan air pada lapisan tanah paling atas yang berinteraksi langsung dengan curah hujan. 
    Nilai kelembapan tanah yang tinggi menandakan tanah berada dalam kondisi jenuh sehingga kemampuan menyerap air tambahan menjadi rendah. 
    Kondisi ini meningkatkan potensi terjadinya limpasan permukaan dan berkontribusi terhadap risiko banjir <sup>[2]</sup>.
    </p>""",    
    unsafe_allow_html=True)
    
    # VARIABEL WINDSPEED 
    st.subheader('3. Wind Speed')
    st.markdown("""
    <p style='text-align: justify;'>
    <strong>Jenis variabel:</strong> Meteorologi (Kecepatan angin)
    </p>
    <p style='text-align: justify;'>
    Wind speed menggambarkan kecepatan pergerakan massa udara di dekat permukaan bumi yang memengaruhi dinamika sistem cuaca. Kecepatan angin dapat 
    memperkuat proses pembentukan dan pergerakan awan hujan, sehingga berperan secara tidak langsung terhadap intensitas dan distribusi curah hujan.
    Dalam konteks banjir, wind speed berfungsi sebagai faktor pendukung yang memengaruhi pola hujan ekstrem di suatu wilayah <sup>[3]</sup>.
    </p>""",    
    unsafe_allow_html=True)

    # DAFTAR PUSTAKA
    st.subheader("📚 Daftar Pustaka")

    st.write("""
    **[1]** John, T. J., & Nagaraj, R. (2023).  
    *Prediction of floods using improved PCA with one-dimensional convolutional neural network.*  
    International Journal of Intelligent Networks, 4, 122–129.  
    https://doi.org/10.1016/j.ijin.2023.05.004
    """)

    st.write("""
    **[2]** Nied, M., Hundecha, Y., & Merz, B. (2013).  
    *Flood-initiating catchment conditions: a spatio-temporal analysis of large-scale soil moisture patterns.*  
    Hydrology and Earth System Sciences, 17(4), 1401–1414.  
    https://doi.org/10.5194/hess-17-1401-2013
    """)

    st.write("""
    **[3]** Agustina, L. A., Lubis, A. M., & Pranowo, W. S. (2025).  
    *Analisis Kejadian Banjir ROB di Provinsi Bengkulu Periode 2022–2024.*  
    Jurnal Kelautan Tropis, 28(1), 25–34.  
    https://doi.org/10.14710/jkt.v28i1.25833
    """)
