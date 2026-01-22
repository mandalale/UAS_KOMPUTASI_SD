import streamlit as st

def team_member():
    # ===================== Anggota 1 =====================
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(
            "https://github.com/mandalale/UAS_KOMPUTASI_SD/blob/665995d8be52cb3177044d437736839233b4072e/foto_mandala.png?raw=true",
            width=250
        )

    with col2:
        st.markdown(
            """
            **Nama**: Mandala Adikara Sencoko   
            **NIM**: 12222420002    
            **Program Studi**: S1 Sains Data  
            **LinkedIn**: [Mandala Sencoko](https://www.linkedin.com/in/mandalasencoko/)
            """
        )

    st.markdown("---")

    # ===================== Anggota 2 =====================
    col3, col4 = st.columns([1, 3])

    with col3:
        st.image(
            "https://github.com/mandalale/UAS_KOMPUTASI_SD/blob/665995d8be52cb3177044d437736839233b4072e/foto_tifa.jpeg?raw=true",
            width=250
        )

    with col4:
        st.markdown(
            """
            **Nama**: Syahdila Tifa Nirmala Sari  
            **NIM**: 12222420006    
            **Program Studi**: S1 Sains Data  
            """
        )

    st.markdown("---")

    # ===================== Anggota 3 =====================
    col5, col6 = st.columns([1, 3])

    with col5:
        st.image(
            "https://github.com/mandalale/UAS_KOMPUTASI_SD/blob/5e8a5354045925df9a75b76fb3890b11b2b6a2e8/foto_asti.jpeg?raw=true",
            width=250
        )

    with col6:
        st.markdown(
            """
            **Nama**: Hanasti Miftahul Jannah    
            **NIM**: 12222420013    
            **Program Studi**: S1 Sains Data  
            """ 
        )

