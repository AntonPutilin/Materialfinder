import streamlit as st

# --- Настройки страницы (вызывается ОДИН РАЗ в самом начале) ---
st.set_page_config(
    page_title="Material Finder",
    layout="wide"  # Используем широкий макет для всего приложения
)

# --- Кастомный CSS (объединен в один блок для чистоты) ---
st.markdown("""
<style>
/* --- Стили для поисковой строки Google --- */
/* Главный контейнер поиска */
.gcse-search {
    width: 100% !important;
    max-width: 100% !important;
}
/* Контейнер поля ввода */
.gsc-control-cse, .gsc-control-cse-en {
    width: 100% !important;
    max-width: 100% !important;
    padding: 0 !important;
}
/* Сам блок ввода */
.gsc-input-box {
    width: 100% !important;
    max-width: 100% !important;
}
/* Поле для текста */
input.gsc-input, .gsc-input-box, .gsc-input-box-hover, .gsc-input-box-focus {
    box-sizing: border-box;
    width: 100% !important;
}

/* --- Стили для кнопок-ссылок --- */
div[data-testid="stLinkButton"] > a {
    display: block;
    width: 100%;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- Список сайтов для поиска (для информации) ---
sites_list = [
    "www.onlinemetals.com", "www.mcmaster.com", "www.store.buymetal.com",
    "www.foamorder.com", "www.metalsdepot.com", "www.myalro.com",
    "www.midweststeelsupply.com", "www.rolledalloys.com",
    "www.professionalplastics.com", "www.plasticsintl.com", "www.boedeker.com",
    "www.dragonplate.com", "www.clearwatercomposites.com", "www.sequoia-brass-copper.com",
    "www.fastmetals.com", "www.curbellplastics.com", "www.hudsontoolsteel.com",
    "www.cherokeewood.com", "www.ocoochhardwoods.com", "www.homedepot.com"
]

# --- Заголовок и информационные блоки ---
st.title("🔎 Material Search")

with st.expander("View the list of sites being searched"):
    st.markdown("\n".join([f"{i}. {site}" for i, site in enumerate(sites_list, 1)]))

st.divider()

# --- Полезные ссылки ---
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

# --- Блок поиска Google ---
search_box_code = """
    <script async src="https://cse.google.com/cse.js?cx=97baf5a535bf14b02"></script>
    <div class="gcse-search"></div>
"""

st.components.v1.html(search_box_code, height=800, scrolling=True)


