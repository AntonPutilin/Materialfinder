import streamlit as st

# --- Настройки страницы ---
st.set_page_config(
    page_title="Поиск по базе знаний",
    layout="wide"
)

# --- Кастомный CSS для растягивания блока поиска ---
# Этот код заставляет компонент Google занимать всю доступную ширину.
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

# --- Заголовок с иконкой ---
st.title("🔎 Встроенный поиск")

st.write(
    "Ниже представлен поисковый блок Google, который ищет "
    "только по заданному списку сайтов."
)

# HTML/JavaScript код от Google с вашим идентификатором (cx)
search_box_code = """
    <script async src="https://cse.google.com/cse.js?cx=97baf5a535bf14b02"></script>
    <div class="gcse-search"></div>
"""

# Встраиваем HTML-компонент в приложение Streamlit
st.components.v1.html(search_box_code, height=120)

st.info(
    "Введите поисковый запрос в поле выше и нажмите Enter "
    "или на значок лупы."
)

# --- Выпадающий список с сайтами ---
with st.expander("Посмотреть список сайтов, по которым ведется поиск"):
    # Создаем форматированную строку Markdown с нумерацией
    markdown_list = ""
    for i, site in enumerate(sites_list, 1):
        markdown_list += f"{i}. {site}\n"
    
    st.markdown(markdown_list)
