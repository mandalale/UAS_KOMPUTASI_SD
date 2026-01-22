import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def preprocessing():
    st.subheader("📥 Pemanggilan dan Seleksi Data")

    st.info(
    "Data ERA5-Land dimuat dan dilakukan seleksi variabel dengan menghapus suhu udara (t2m) "
    "dan tekanan permukaan (sp) karena tidak digunakan dalam pembentukan Flood Potential Index."
    )

    df = pd.read_csv("https://raw.githubusercontent.com/mandalale/UAS_KOMPUTASI_SD/refs/heads/main/DATA2010_2025%20(unprocessed).csv")
    st.write("Contoh data awal:")
    st.dataframe(df.head(), use_container_width=True)

    # Drop variabel yang tidak digunakan
    df = df.drop(columns=["t2m", "sp"])

    # konversi ke datetime dan set index
    st.subheader("🗓️ Konversi Variabel Waktu dan Penetapan Indeks")
    df["valid_time"] = pd.to_datetime(df["valid_time"])
    df = df.set_index("valid_time")

    st.info(
    "Variabel waktu dikonversi ke format datetime dan dijadikan sebagai indeks untuk "
    "memungkinkan proses agregasi temporal secara konsisten."
    )

    # Pembentukan variabel wind speed
    st.subheader("🌬️ Pembentukan Variabel wind_speed")
    st.info(
        "Kecepatan angin dihitung dari komponen angin zonal (u10) dan meridional (v10) "
        "menggunakan pendekatan vektor. Variabel wind_speed digunakan sebagai representasi "
        "intensitas angin permukaan yang memengaruhi dinamika pesisir."
    )

    st.markdown("**Rumus perhitungan kecepatan angin:**")
    st.latex(r"""
    \text{wind\_speed} = \sqrt{u_{10}^{2} + v_{10}^{2}}
    """)


    df["wind_speed"] = np.sqrt(df["u10"]**2 + df["v10"]**2)

    st.write("Data setelah pembentukan wind speed:")
    st.dataframe(df[["u10", "v10", "wind_speed"]].head(), use_container_width=True)



    # resampeling ke harian
    st.subheader("📅 Agregasi Data ke Skala Harian")
    df_daily = df.resample("D").agg({
    "tp": "sum",
    "swvl1": "mean",
    "wind_speed": "mean"
    })

    st.info(
    "Agregasi harian dilakukan untuk menyesuaikan skala analisis banjir. "
    "Curah hujan (tp) dijumlahkan karena bersifat akumulatif, sedangkan "
    "kelembapan tanah (swvl1) dan kecepatan angin dirata-ratakan karena "
    "mewakili kondisi rata-rata harian."
    )

    st.write("Data setelah agregasi harian:")
    st.dataframe(df_daily.head(), use_container_width=True)


    # PCA
    st.subheader("📊 Principal Component Analysis (PCA)")

    X = df_daily[["tp", "swvl1", "wind_speed"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=3)
    PC = pca.fit_transform(X_scaled)

    eigen_df = pd.DataFrame({
        "Komponen": ["PC1", "PC2", "PC3"],
        "Eigenvalue": pca.explained_variance_,
        "Explained Variance Ratio": pca.explained_variance_ratio_
    })

    # visualisasi scree plot
    pc_numbers = np.arange(1, 4)

    fig = px.line(
        x=pc_numbers,
        y=pca.explained_variance_,
        markers=True,
        labels={"x": "Komponen Utama", "y": "Eigenvalue"},
        title="Scree Plot PCA"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(eigen_df, use_container_width=True)
    st.info(
        "Eigenvalue menunjukkan besarnya variansi yang dijelaskan oleh masing-masing "
        "komponen utama. PC1 memiliki kontribusi terbesar sehingga dipilih sebagai "
        "representasi utama Flood Potential Index."
    )


    loadings = pd.DataFrame(
        pca.components_.T,
        index=["tp", "swvl1", "wind_speed"],
        columns=["PC1", "PC2", "PC3"]
    )

    st.write("Bobot (loading) PCA:")
    st.info(
        "Bobot PCA (loading) merepresentasikan kontribusi relatif masing-masing variabel "
        "terhadap komponen utama. Nilai absolut yang lebih besar menunjukkan pengaruh yang lebih kuat."
    )
    st.dataframe(loadings, use_container_width=True)
    
    pc1_eq = " + ".join(
        [f"{pca.components_[0][i]:.4f} × Z({var})"
        for i, var in enumerate(["tp", "swvl1", "wind_speed"])]
    )

    st.info(
        "PC1 dibentuk sebagai kombinasi linier dari variabel terstandarisasi, "
        "yang selanjutnya digunakan sebagai Flood Potential Index."
    )
    st.code(f"PC1 = {pc1_eq}")


    # Flood Potential Index
    st.subheader("🌊 Pembentukan Flood Potential Index (FPI)")

    df_daily["FPI"] = PC[:, 0]

    # Pastikan arah indeks
    if loadings["PC1"].sum() < 0:
        df_daily["FPI"] = -df_daily["FPI"]

    df_daily["FPI_norm"] = (
        (df_daily["FPI"] - df_daily["FPI"].min()) /
        (df_daily["FPI"].max() - df_daily["FPI"].min())
    )

    
    st.markdown("""
    <p style="text-align: justify;">
    Flood Potential Index (FPI) dibentuk menggunakan komponen utama pertama (PC1) dari Principal Component Analysis, 
    yang merepresentasikan variasi dominan dari variabel curah hujan, kelembapan tanah permukaan, dan kecepatan angin. 
    FPI awal merupakan skor indeks relatif yang menggambarkan tingkat potensi banjir berdasarkan struktur variansi data, 
    namun masih berada pada skala asli PCA sehingga belum memiliki batas interpretasi yang baku. Oleh karena itu, FPI berfungsi 
    sebagai representasi awal kondisi hidrometeorologi yang berkontribusi terhadap potensi banjir.
    </p>

    <p style="text-align: justify;">
    Selanjutnya, FPI dinormalisasi ke dalam rentang 0 hingga 1 menggunakan metode Min–Max scaling dan disimpan sebagai FPI_norm. 
    Proses normalisasi ini bertujuan untuk menyeragamkan skala indeks agar lebih mudah diinterpretasikan, dibandingkan secara temporal,
    serta digunakan dalam analisis statistik dan visualisasi. Dalam penelitian ini, nilai FPI_norm digunakan sebagai indikator utama 
    potensi banjir, di mana nilai yang lebih besar menunjukkan tingkat potensi banjir yang lebih tinggi, sementara variabel FPI asli 
    tidak digunakan dalam tahap analisis lanjutan.
    </p>
    """, unsafe_allow_html=True)

    st.success("FPI_norm digunakan sebagai indikator utama potensi banjir dalam seluruh analisis.")

    st.dataframe(df_daily.head(), use_container_width=True)

    st.markdown(
        """
        **Ringkasan Preprocessing:**
        - Data diolah secara temporal menjadi skala harian  
        - Variabel kecepatan angin (wind_speed) dibentuk dari variabel u10 dan v10 
        - PCA digunakan untuk membangun indeks banjir secara objektif  
        - FPI berbasis PC1 merepresentasikan variansi dominan sistem hidrometeorologi
        """
    )

    df_daily = df_daily.drop(columns=["FPI"])
    st.subheader("📎 Dataset Setelah Tahap Preprocessing")

    st.caption(
        "Dataset ini merupakan hasil pengolahan data ERA5-Land yang telah melalui "
        "tahap pembersihan, agregasi harian, pembentukan variabel turunan, serta "
        "normalisasi Flood Potential Index (FPI_norm)."
    )

    st.download_button(
        label="⬇️ Unduh Dataset (CSV)",
        data=df_daily.to_csv(index=True),
        file_name="ERA5Land_FPI_Preprocessed.csv",
        mime="text/csv"
    )

        











