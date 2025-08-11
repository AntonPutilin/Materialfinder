import streamlit as st

st.set_page_config(page_title="Material Finder", layout="wide")

# Агрессивный CSS для растяжения контейнера Google CSE
st.markdown("""
<style>
/* Растягиваем контейнер с поиском */
.gcse-search {
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 auto;
}

/* Главный контейнер поиска */
.gsc-control-cse {
    width: 100% !important;
    max-width: 100% !important;
}

/* Растягиваем таблицу поиска */
table.gsc-search-box {
    width: 100% !important;
}

/* Растягиваем поле ввода */
input.gsc-input {
    width: 100% !important;
    box-sizing: border-box;
}

/* Центрируем кнопку поиска и делаем её адекватного размера */
.gsc-search-button {
    height: 38px !important;
    padding: 0 10px !important;
}
</style>
""", unsafe_allow_html=True)

# Вставка кода Google Programmable Search
search_box_code = """
<script async src="https://cse.google.com/cse.js?cx=97baf5a535bf14b02"></script>
<div class="gcse-search"></div>
"""

st.components.v1.html(search_box_code, height=150)

