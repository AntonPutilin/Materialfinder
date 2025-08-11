import streamlit as st

# --- Настройки страницы ---
st.set_page_config(
    page_title="Material finder",
    layout="wide"
)

# --- CSS для полной ширины поиска ---
st.markdown("""
<style>
/* Контейнер поиска */
.gsc-control-cse {
    width: 100% !important;
    max-width: 100% !important;
}

/* Обертка формы */
.gsc-control-wrapper-cse {
    width: 100% !important;
}

/* Таблица поиска, которую Google вставляет */
table.gsc-search-box {
    width: 100% !important;
}

/* Ячейки таблицы */
td.gsc-input {
    width: 100% !important;
}

/* Само поле ввода */
input.gsc-input {
    width: 100% !important;
    max-width: 100% !important;
    font-size: 16px;
    box-sizing: border-box;
}

/* Кнопка поиска */
.gsc-search-button {
    height: 40px !important;
}
</style>
""", unsafe_allow_html=True)

# --- HTML Google CSE ---
search_box_code = """
    <script async src="https://cse.google.com/cse.js?cx=97baf5a535bf14b02"></script>
    <div class="gcse-search"></div>
"""

# --- Отображение поиска ---
st.components.v1.html(search_box_code, height=100)
