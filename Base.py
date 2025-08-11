import streamlit as st

# --- 1. Настройки страницы ---
st.set_page_config(
    page_title="Material Finder",
    layout="wide"
)

# --- 2. CSS для максимальной ширины и адаптивности ---
st.markdown("""
<style>
/* Главный контейнер Streamlit */
.stApp {
    max-width: 100% !important;
}

/* Контейнер поиска */
.gcse-search {
    width: 100% !important;
    max-width: 100% !important;
}

/* Основной блок Google */
.gsc-control-cse, .gsc-control-cse-en {
    width: 100% !important;
    max-width: 100% !important;
    padding: 0 !important;
    border: none !important;
    background-color: transparent !important;
}

/* Таблица поиска */
table.gsc-search-box {
    width: 100% !important;
    margin-bottom: 0 !important;
}

/* Ячейки */
td.gsc-input {
    width: 100% !important;
    padding-right: 12px !important;
}
td.gsc-search-button {
    width: auto !important;
}

/* Поле ввода */
input.gsc-input {
    box-sizing: border-box !important;
    width: 100% !important;
    height: 40px !important;
    padding: 10px !important;
    border: 1px solid #dfe1e5 !important;
    font-size: 16px !important;
}

/* Кнопка поиска */
.gsc-search-button {
    height: 40px !important;
}

/* Стили для кнопок-ссылок */
div[data-testid="stLinkButton"] > a {
    display: block;
    width: 100%;
    text-align: center;
}

/* Адаптивность для мобильных */
@media (max-width: 600px) {
    input.gsc-input {
        font-size: 14px !important;
        height: 36px !important;
        padding: 6px !important;
    }
    .gsc-search-button {
        height: 36px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# --- 3. Список сайтов ---
sites_list = [
    "www.onlinemetals.com", "www.mcmaster.com", "www.store.buymetal.com",
    "www.foamorder.com", "www.metalsdepot.com", "www.myalro.com",
    "www.midweststeelsupply.com", "www.rolledalloys.com",
    "www.professionalplastics.com", "www.plasticsintl.com", "www.boedeker.com",
    "www.dragonplate.com", "www.clearwatercomposites.com", "www.sequoia-brass-copper.com",
    "www.fastmetals.com", "www.curbellplastics.com", "www.hudsontoolsteel.com",
    "www.cherokeewood.com", "www.ocoochhardwoods.com", "www.homedepot.com"
]

# --- 4. Заголовок и список сайтов ---
st.title("🔎 Material Search")

with st.expander("View the list of sites being searched"):
    st.markdown("\n".join([f"{i}. {site}" for i, site in enumerate(sites_list, 1)]))

st.divider()

# --- 5. Полезные ссылки ---
col1, col2, col3, col4, col5 = st.columns(5, gap="medium")
with col1:
    st.link_button("Property Material Search", "https://www.matweb.com/search/PropertySearch.aspx")
with col2:
    st.link_button("Custom Material Ordered", "https://xometry.looker.com/looks/5286?toggle=fil")
with col3:
    st.link_button("Material Cross Reference", "https://www.mitsubishicarbide.net/contents/mmus/enus/manual/material_cross_reference.pdf")
with col4:
    st.link_button("Plastics Tradename Crossing", "https://eagle-plastics.com/tradename-cross-reference/")
with col5:
    st.link_button("Material Equivalent Searching", "https://www.steelnumber.com/en/search_form_eu.php")

st.divider()

# --- 6. Google Search ---
search_box_code = """
    <script async src="https://cse.google.com/cse.js?cx=97baf5a535bf14b02"></script>
    <div class="gcse-search"></div>
"""

st.components.v1.html(search_box_code, height=150)
