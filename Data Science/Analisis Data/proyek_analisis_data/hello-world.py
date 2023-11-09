import streamlit as st
import pandas as pd

st.title('Belajar Analisis Data')

st.header('Pengembangan Dashboard')

st.subheader('Pengembangan Dashboard')

st.caption('Copyright ()')

st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))
