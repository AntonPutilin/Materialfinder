import streamlit as st
import urllib.parse

# --- 1. Настройки страницы ---
# Устанавливаем широкий макет, чтобы все элементы, включая поле ввода,
# занимали максимальную доступную ширину.
st.set_page_config(
    page_title="Material Finder",
    layout="wide"
)

# --- 2. Стили (только для кнопок) ---
st.markdown("""
<style>
div[data-testid="stLinkButton"] > a {
    display: block;
    width: 100%;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- 3. Данные и интерфейс ---
sites_list = [
    "onlinemetals.com", "mcmaster.com", "store.buymetal.com", "foamorder.com",
    "metalsdepot.com", "myalro.com", "midweststeelsupply.com", "rolledalloys.com",
    "professionalplastics.com", "plasticsintl.com", "boedeker.com", "dragonplate.com",
    "clearwatercomposites.com", "sequoia-brass-copper.com", "fastmetals.com",
    "curbellplastics.com", "hudsontoolsteel.com", "cherokeewood.com",
    "ocoochhardwoods.com", "homedepot.com"
]

st.title("🔎 Material Search")

with st.expander("View the list of sites being searched"):
    st.markdown("\n".join([f"{i}. {site}" for i, site in enumerate(sites_list, 1)]))

st.divider()

# Полезные ссылки
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

# --- 4. БЛОК ПОИСКА ---
st.header("Search Across Supplier Websites")

# --- ЭТО ВАША ШИРОКАЯ СТРОКА ПОИСКА ---
# В режиме layout="wide" этот элемент автоматически растягивается.
query = st.text_input(
    "Enter your search query:",
    placeholder="e.g., '6061 T6 aluminum sheet 0.25 inch'"
)

# Если пользователь ввел запрос
if query:
    # Формируем поисковый запрос для Google
    search_sites_string = " OR ".join([f"site:{site}" for site in sites_list])
    full_query = f"{query} {search_sites_string}"
    
    # Кодируем запрос для URL
    encoded_query = urllib.parse.quote_plus(full_query)
    
    # Создаем финальную ссылку на Google
    # ИСПРАВЛЕННАЯ СТРОКА:
    Google Search_url = f"https://www.google.com/search?q={encoded_query}"
    
    # --- ЭТО ВАШЕ ШИРОКОЕ ОКНО РЕЗУЛЬТАТОВ ---
    # Кнопка откроет новую вкладку браузера, которая и будет вашим
    # окном результатов на всю ширину экрана.
    st.link_button("Click here to see search results in a new tab", Google Search_url)
    st.info("A new browser tab will open with the search results.")

