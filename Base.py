import streamlit as st

# --- Настройки страницы ---
st.set_page_config(
    page_title="Material finder",
    layout="wide"
)

# --- Кастомный CSS для растягивания блока поиска ---
st.markdown("""
<style>
.gsc-control-cse {
    width: 100% !important;
    max-width: 100% !important;
}
.gsc-input-box {
    width: 100% !important;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

# --- Список сайтов для поиска ---
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

# --- Заголовок страницы (остается вверху для логики) ---
st.title("🔎 Material search")

# --- Выпадающий список с сайтами (теперь идет первым) ---
with st.expander("View the list of sites being searched"):
    markdown_list = ""
    for i, site in enumerate(sites_list, 1):
        markdown_list += f"{i}. {site}\n"
    st.markdown(markdown_list)

st.set_page_config(layout="centered")

# CSS для стилизации кнопок-ссылок
# Заставляет кнопки занимать всю ширину колонки и центрирует текст
st.markdown("""
<style>
div[data-testid="stLinkButton"] > a {
    display: block;
    width: 100%;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5, gap="medium")

with col1:
    st.link_button("Property Material Search", "https://www.matweb.com/search/PropertySearch.aspx")
        
with col2:
    st.link_button("Custom Material / Finish Ordered", "https://xometry.looker.com/looks/5286?toggle=fil")

with col3:
    st.link_button("Material cross reference list", "https://www.mitsubishicarbide.net/contents/mmus/enus/manual/material_cross_reference.pdf")

with col4:
    st.link_button("Plastics Tradename Cross Reference", "https://eagle-plastics.com/tradename-cross-reference/")

with col5:
    st.link_button("Material equivalent", "https://www.steelnumber.com/en/search_form_eu.php")

# --- Разделитель для визуальной ясности ---
st.divider()

# --- Блок поиска (перенесен вниз) ---
# st.header("Search")
# st.write(
#     "Use it like Google search "
# )

# HTML/JavaScript код от Google
search_box_code = """
    <script async src="https://cse.google.com/cse.js?cx=97baf5a535bf14b02"></script>
    <div class="gcse-search"></div>
"""

# Встраиваем HTML-компонент
st.components.v1.html(search_box_code, height=800)

# st.info(
#     "Введите поисковый запрос в поле выше и нажмите Enter "
#     "или на значок лупы."
# )
