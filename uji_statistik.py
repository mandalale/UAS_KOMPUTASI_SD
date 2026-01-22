import streamlit as st
import pandas as pd
from scipy import stats
from scipy.stats import mannwhitneyu

def uji_statistik():
    df_daily = pd.read_csv("https://raw.githubusercontent.com/mandalale/UAS_KOMPUTASI_SD/refs/heads/main/ILMULINGKUNGAN_2010_2025%20(processed).csv", index_col=0, parse_dates=True)
    
    cutoff_date = pd.Timestamp("2014-10-09")

    df_daily["period"] = [
        "Pre" if date < cutoff_date else "Post"
        for date in df_daily.index
    ]

    # penentuan periode analisis
    st.subheader("📌 Penentuan Periode Analisis")

    period_count = df_daily["period"].value_counts().reset_index()
    period_count.columns = ["Periode", "Jumlah Data"]

    st.dataframe(period_count, use_container_width=True)

    st.subheader("📐 Uji Asumsi Statistik")

    # Uji Normalitas (Shapiro-Wilk)
    pre = df_daily[df_daily["period"] == "Pre"]["FPI_norm"]
    post = df_daily[df_daily["period"] == "Post"]["FPI_norm"]

    shapiro_pre = stats.shapiro(pre)
    shapiro_post = stats.shapiro(post)

    normality_df = pd.DataFrame({
        "Periode": ["Pre-tanggul", "Post-tanggul"],
        "Statistik Shapiro-Wilk": [shapiro_pre.statistic, shapiro_post.statistic],
        "p-value": [shapiro_pre.pvalue, shapiro_post.pvalue]
    })

    st.markdown("**Uji Normalitas (Shapiro–Wilk)**")
    st.dataframe(normality_df, use_container_width=True)
    
    # Uji Homogenitas Variansi (Levene)
    levene_test = stats.levene(pre, post)
    homogeneity_df = pd.DataFrame({
    "Uji": ["Levene"],
    "Statistik": [levene_test.statistic],
    "p-value": [levene_test.pvalue]
})

    st.markdown("**Uji Homogenitas Variansi (Levene)**")
    st.dataframe(homogeneity_df, use_container_width=True)

    st.info(
    "Hasil uji normalitas menunjukkan bahwa distribusi FPI pada kedua periode tidak normal "
    "(p-value < 0.05), dan uji homogenitas variansi mengindikasikan variansi yang tidak homogen. "
    "Oleh karena itu, analisis perbedaan antara periode sebelum dan sesudah pembangunan tanggul "
    "dilanjutkan menggunakan uji non-parametrik Mann–Whitney U."
)
    
    # MANN WHITNEY U TEST
    # st.subheader("🔍 Uji Mann–Whitney U")
    # u_stat, p_val = mannwhitneyu(pre, post, alternative="two-sided")

    # mw_df = pd.DataFrame({
    #     "Statistik U": [u_stat],
    #     "p-value": [p_val]
    # })

    # st.dataframe(mw_df, use_container_width=True)

    # if p_val < 0.05:
    #     st.success(
    #         "H₀ ditolak. Terdapat perbedaan distribusi Flood Potential Index (FPI) yang signifikan "
    #         "antara periode sebelum dan sesudah pembangunan tanggul pesisir."
    # )
    # else:
    #     st.warning(
    #         "H₀ gagal ditolak. Tidak terdapat perbedaan distribusi Flood Potential Index (FPI) "
    #         "yang signifikan antara kedua periode."
    #     )

    # MANN WHITNEY U TEST
    st.subheader("🔍 Uji Mann–Whitney U")

    st.markdown("""
    **Hipotesis Statistik:**

    - **H₀ (Hipotesis nol):** Tidak terdapat perbedaan distribusi Flood Potential Index (FPI) 
    antara periode sebelum dan sesudah pembangunan tanggul pesisir.

    - **H₁ (Hipotesis alternatif):** Terdapat perbedaan distribusi Flood Potential Index (FPI) 
    antara periode sebelum dan sesudah pembangunan tanggul pesisir.
    """)

    u_stat, p_val = mannwhitneyu(pre, post, alternative="two-sided")

    mw_df = pd.DataFrame({
        "Statistik U": [u_stat],
        "p-value": [p_val]
    })

    st.dataframe(mw_df, use_container_width=True)

    st.markdown(f"""
    **Kriteria Pengambilan Keputusan:**

    - Tolak H₀ jika *p-value* < 0.05  
    - Gagal menolak H₀ jika *p-value* ≥ 0.05  

    **Hasil Uji:**  
    *p-value* = **{p_val:.3e}**
    """)

    if p_val < 0.05:
        st.success(
            "H₀ ditolak. Terdapat perbedaan distribusi Flood Potential Index (FPI) yang signifikan "
            "antara periode sebelum dan sesudah pembangunan tanggul pesisir."
        )
    else:
        st.warning(
            "H₀ gagal ditolak. Tidak terdapat perbedaan distribusi Flood Potential Index (FPI) "
            "yang signifikan antara kedua periode."
        )











