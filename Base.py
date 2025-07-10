import streamlit as st

# --- Настройки страницы ---
st.set_page_config(
    page_title="Material finder",
    layout="centered"
)

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
st.title("🔎 Material Search")

st.write(
    "Use it like Google search "
)

# HTML/JavaScript код от Google с вашим идентификатором (cx)
search_box_code = """
    <script async src="https://cse.google.com/cse.js?cx=97baf5a535bf14b02"></script>
    <div class="gcse-search"></div>
"""

# Встраиваем HTML-компонент в приложение Streamlit
st.components.v1.html(search_box_code, height=120)

st.info(
    "Enter your search query in the box above and press Enter "
)

# --- Выпадающий список с сайтами ---
with st.expander("View the list of sites being searched"):
    # Создаем форматированную строку Markdown с нумерацией
    markdown_list = ""
    for i, site in enumerate(sites_list, 1):
        markdown_list += f"{i}. {site}\n"
    
    st.markdown(markdown_list)