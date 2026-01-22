import streamlit as st

def visualisasi():
    img_url1 = 'https://github.com/mandalale/UAS_KOMPUTASI_SD/blob/main/vis_distribusi_fpi_pre_post.png?raw=true'
    st.header('1. Visualisasi Distribusi Flood Potential Index (FPI) Sebelum dan Sesudah Pembangunan Tanggul')
    st.image(
        img_url1,
        caption="Distribusi Flood Potential Index Sebelum dan Sesudah Tanggul",
        width= 800, 
        use_container_width=True
        )
    st.markdown(
        """
        <p style="text-align: justify;">
        Distribusi Flood Potential Index pada periode sebelum dan sesudah pembangunan tanggul menunjukkan pola sebaran yang relatif serupa,
        dengan konsentrasi nilai FPI pada rentang rendah hingga menengah. Pada periode pasca pembangunan, distribusi FPI tampak sedikit bergeser
        ke arah nilai yang lebih tinggi dan tetap mempertahankan ekor kanan, yang menandakan bahwa kondisi dengan potensi banjir tinggi masih
        terjadi meskipun infrastruktur pengendalian telah dibangun. Kepadatan distribusi yang lebih besar pada periode pasca tanggul juga dipengaruhi 
        oleh jumlah observasi yang lebih banyak, sehingga perbedaan visual tidak secara langsung merefleksikan peningkatan risiko, melainkan perlu
        ditafsirkan dalam konteks struktur data.
        </p>

        <p style="text-align: justify;">
        Kemiripan bentuk distribusi dan tumpang tindih yang kuat antara kedua periode mengindikasikan bahwa karakteristik potensi banjir pesisir tidak
        mengalami perubahan struktural yang signifikan setelah pembangunan tanggul. Keberadaan nilai FPI tinggi pada kedua periode menunjukkan bahwa
        faktor hidrometeorologi daratan dan atmosfer tetap berperan dominan dalam membentuk potensi banjir. Temuan ini menegaskan bahwa tanggul berfungsi
        sebagai pengendali sebagian kondisi banjir, tetapi efektivitasnya bergantung pada integrasi dengan pengelolaan limpasan darat dan sistem drainase
        perkotaan secara menyeluruh.
        </p>
        """,
        unsafe_allow_html=True)
    
    img_url2 = 'https://github.com/mandalale/UAS_KOMPUTASI_SD/blob/main/vis_fpi_before_after.png?raw=true'
    st.header('2. Visualisasi Perbandingan Flood Potential Index (FPI) Sebelum dan Sesudah Pembangunan Tanggul')
    st.image(
        img_url2,
        caption="Perbandingan Flood Potential Index Sebelum dan Sesudah Tanggul",
        width= 800,
        use_container_width=True
        )
    st.markdown(
        """
        <p style="text-align: justify;">
        Visualisasi Flood Potential Index menunjukkan bahwa potensi banjir pesisir di Jakarta Utara berfluktuasi 
        secara signifikan sepanjang periode pengamatan dan membentuk pola musiman yang konsisten. Meskipun pembangunan
        tanggul pesisir dilakukan pada Oktober 2014, tren rata rata FPI 30 harian tidak memperlihatkan penurunan yang tajam
        dan berkelanjutan setelah periode tersebut. Hal ini mengindikasikan bahwa dinamika potensi banjir masih sangat
        dipengaruhi oleh faktor hidrometeorologi daratan, terutama curah hujan dan kejenuhan tanah, yang tidak secara langsung
        dikendalikan oleh infrastruktur tanggul.
        </p>

        <p style="text-align: justify;">
        Sebaran kejadian ekstrem yang ditandai oleh nilai FPI pada kuantil 95 persen muncul baik sebelum maupun sesudah pembangunan tanggul.
        Temuan ini menunjukkan bahwa keberadaan tanggul belum sepenuhnya menurunkan intensitas kejadian potensi banjir ekstrem, melainkan lebih
        berperan sebagai pengendali limpasan laut. Dengan demikian, pengurangan potensi banjir pesisir di Jakarta Utara memerlukan pendekatan yang
        lebih terintegrasi, termasuk pengelolaan limpasan darat dan sistem drainase perkotaan, selain pembangunan infrastruktur pesisir.
        </p>
        """,
        unsafe_allow_html=True
    )

    img_url3 = 'https://github.com/mandalale/UAS_KOMPUTASI_SD/blob/main/vis_calendar_heatmap_fpi.png?raw=true'
    st.header('3. Visualisasi Kalender Heatmap Flood Potential Index (FPI) Sebelum dan Sesudah Pembangunan Tanggul')
    st.image(
        img_url3,
        caption="Kalender Heatmap Flood Potential Index Sebelum dan Sesudah Tanggul",
        width= 800,
        use_container_width=True
        )
    st.markdown(
        """
        <p style="text-align: justify;">
        Visualisasi heatmap digunakan untuk mengidentifikasi pola temporal dan variasi musiman secara jelas melalui representasi 
        warna, sehingga memudahkan analisis perubahan Flood Potential Index (FPI) dari waktu ke waktu. Heatmap ini menunjukkan 
        rata-rata nilai FPI tiap bulan selama periode 2010–2025 di wilayah studi. Hasil visualisasi memperlihatkan pola musiman 
        yang konsisten, di mana nilai FPI cenderung lebih tinggi pada awal dan akhir tahun, khususnya pada bulan Januari–Maret serta 
        November–Desember yang ditandai dengan warna merah hingga oranye. Kondisi tersebut berkaitan dengan musim hujan di Indonesia,
        ketika curah hujan meningkat dan tingkat kejenuhan tanah lebih tinggi, sehingga potensi terjadinya genangan atau banjir menjadi 
        lebih besar.
        </p>

        <p style="text-align: justify;">
        Sebaliknya, nilai FPI terendah terjadi pada pertengahan tahun, terutama pada bulan Juli–September, yang ditunjukkan oleh warna biru.
        Periode ini bertepatan dengan musim kemarau, di mana curah hujan relatif rendah dan kondisi tanah lebih kering, sehingga potensi banjir 
        menurun. Pola ini muncul hampir di setiap tahun, menandakan bahwa variabilitas FPI lebih dipengaruhi oleh faktor musiman dibandingkan 
        fluktuasi antar tahun.
        </p>

        <p style="text-align: justify;">
        Secara temporal, heatmap juga menunjukkan bahwa tidak ada perubahan pola ekstrem yang tiba-tiba antar tahun, termasuk setelah 
        pembangunan tanggul. Hal ini mengindikasikan bahwa tanggul tidak menghilangkan siklus musiman banjir, tetapi lebih berperan dalam 
        mengendalikan dampak banjir, bukan menghapus potensi hidrometeorologinya. Dengan demikian, FPI efektif digunakan sebagai indikator
        kondisi lingkungan yang merefleksikan interaksi hujan, kelembapan tanah, dan angin secara periodik sepanjang tahun.
        </p>
        """, unsafe_allow_html=True)