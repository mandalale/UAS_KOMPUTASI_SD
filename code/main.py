import streamlit as st

st.header('Analisis Potensi Banjir Pesisir Jakarta Utara Menggunakan Flood Potential Index Berbasis PCA')
st.write('**Ujian Akhir Semester** - S1 Sains Data')
st.write('Universitas Muhammadiyah Semarang')

tab1, tab2, tab3, tab4, tab5 = st.tabs([
                            'About Dataset', 
                            'Data Exploration', 
                            'Preprocessing',
                            'Statistical Test',
                            'Meet Our Team'])

with tab1:
    import about_dataset
    about_dataset.about_dataset()

with tab2:
    import visualisasi
    visualisasi.visualisasi()

with tab3:
    import preprocessing
    preprocessing.preprocessing()

with tab4:
    import uji_statistik
    uji_statistik.uji_statistik()

with tab5:
    import contact_us
    contact_us.team_member()

