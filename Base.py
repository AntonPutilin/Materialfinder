import streamlit as st

# --- Настройки страницы ---
st.set_page_config(
    page_title="Material finder",
    layout="wide"
)

# --- Кастомный CSS ---
st.markdown("""
<style>
/* Растягиваем поле поиска на всю ширину */
.gsc-control-cse {
    width: 100% !important;
    max-width: 100% !important;
}

.gsc-control-wrapper-cse {
    width: 100% !important;
}

.gsc-input-box,
input.gsc-input {
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box;
    font-size: 16px;
    padding: 6px;
}

/* Кнопка поиска */
.gsc-search-button {
    height: 40px !important;
}

/* Центрирование поиска */
.gcse-search {
    margin: 0 auto;
    width: 100%;
}

/* Делаем адаптивность */
@media (max-width: 768px) {
    .gsc-input-box,
    input.gsc-input {
        font-size: 14px;
    }
}
</style>
""", unsafe_allow_html=True)

# --- Список сайтов ---
sites_list = [
    "www.onlinemetals.com",
    "www.mcmaster.com",
    "www.store.buymetal.com",
    "www.foamorder.com",
    "www.metalsdepot.com",
    "www.myalro.com",
    "www.midweststeelsupply.com",
    "www.rolledalloys.com",
    "www.professionalplastics.com",
    "www.plasticsintl.com",
    "www.boedeker.com",
    "www.dragonplate.com",
    "www.clearwatercomposites.com",
    "www.sequoia-brass-copper.com",
    "www.fastmetals.com",
    "www.curbellplastics.com",
    "www.hudsontoolsteel.com",
    "www.cherokeewood.com",
    "www.ocoochhardwoods.com",
    "www.homedepot.com"
]

# --- Заголовок ---
st.title("🔎 Material search")

# --- Список сайтов ---
with st.expander("View the list of sites being searched"):
    markdown_list = "\n".join(f"{i}. {site}" for i, site in enumerate(sites_list, 1))
    st.markdown(markdown_list)

st.divider()

# --- Блок ссылок ---
col1, col2, col3, col4, col5 = st.columns(5, gap="medium")

with col1:
    st.link_button("Property Material Search", "https://www.matweb.com/search/PropertySearch.aspx")
        
with col2:
    st.link_button("Custom Material Ordered", "https://xometry.looker.com/looks/5286?toggle=fil")

with col3:
    st.link_button("Material cross reference list", "https://www.mitsubishicarbide.net/contents/mmus/enus/manual/material_cross_reference.pdf")

with col4:
    st.link_button("Plastics Tradename Crossing", "https://eagle-plastics.com/tradename-cross-reference/")

with col5:
    st.link_button("Material equivalent searching", "https://www.steelnumber.com/en/search_form_eu.php")

st.divider()

# --- Google CSE поисковая строка ---
search_box_code = """
    <script async src="https://cse.google.com/cse.js?cx=97baf5a535bf14b02"></script>
    <div class="gcse-search"></div>
"""

st.components.v1.html(search_box_code, height=800)
