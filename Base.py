import streamlit as st
import streamlit.components.v1 as components

# --- 1. Настройки страницы (ОДИН РАЗ В САМОМ НАЧАЛЕ) ---
st.set_page_config(
    page_title="Multi-Search Tool",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. Глобальный CSS для Streamlit (кнопки, отступы) ---
st.markdown("""
<style>
/* Стили для кнопок-ссылок */
div[data-testid="stLinkButton"] > a {
    display: block;
    width: 100%;
    text-align: center;
    font-weight: bold;
    border: 1px solid #e0e0e0;
}

/* Убираем лишние отступы сверху страницы */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# --- 3. Функция генерации HTML для Google Search ---
def get_search_html(cx_id):
    """
    Создает изолированный HTML-код для Google Custom Search.
    Стили внутри <style> применяются ТОЛЬКО к поиску внутри iframe.
    """
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0; 
            padding: 0;
            background-color: transparent;
        }}
        /* Агрессивное растягивание контейнеров */
        .gcse-search, .gsc-control-cse {{
            width: 100% !important;
            padding: 0 !important;
            border: none !important;
            background-color: transparent !important;
        }}
        
        /* Поле ввода */
        input.gsc-input {{
            width: 100% !important;
            padding: 12px 15px !important;
            border: 1px solid #dfe1e5 !important;
            border-radius: 24px !important; /* Закругленные углы */
            font-size: 16px !important;
            outline: none !important;
            background: #fff !important;
            box-sizing: border-box !important;
            height: 45px !important;
        }}
        
        /* Фокус на поле ввода */
        input.gsc-input:focus {{
            box-shadow: 0 1px 6px rgba(32,33,36,0.28) !important;
            border-color: rgba(223,225,229,0) !important;
        }}

        /* Кнопка поиска (лупа) */
        button.gsc-search-button {{
            background-color: transparent !important;
            border: none !important;
            margin-left: -40px !important; /* Сдвигаем внутрь поля */
            z-index: 10;
            cursor: pointer;
        }}
        
        /* Убираем лишние отступы таблицы */
        table.gsc-search-box {{
            margin-bottom: 20px !important;
        }}
        td.gsc-input {{
            padding-right: 0 !important;
        }}
        
        /* Результаты поиска */
        .gsc-webResult.gsc-result {{
            padding: 10px 0 !important;
            border-bottom: 1px solid #eee !important;
        }}
    </style>
    </head>
    <body>
        <script async src="https://cse.google.com/cse.js?cx={cx_id}"></script>
        <div class="gcse-search"></div>
    </body>
    </html>
    """

# --- 4. Основной контент страницы ---

# Список сайтов
sites_list = [
    "www.onlinemetals.com", "www.mcmaster.com", "www.store.buymetal.com",
    "www.foamorder.com", "www.metalsdepot.com", "www.myalro.com",
    "www.midweststeelsupply.com", "www.rolledalloys.com",
    "www.professionalplastics.com", "www.plasticsintl.com", "www.boedeker.com",
    "www.dragonplate.com", "www.clearwatercomposites.com", "www.sequoia-brass-copper.com",
    "www.fastmetals.com", "www.curbellplastics.com", "www.hudsontoolsteel.com",
    "www.cherokeewood.com", "www.ocoochhardwoods.com", "www.homedepot.com"
]

st.title("🔎 Universal Search Tool")

# Expander со списком
with st.expander("ℹ️ View searched websites list"):
    st.markdown("\n".join([f"{i}. {site}" for i, site in enumerate(sites_list, 1)]))

st.divider()

# Панель быстрых ссылок
col1, col2, col3, col4, col5, col6 = st.columns(6, gap="small")

with col1:
    st.link_button("📊 Properties", "https://www.matweb.com/search/PropertySearch.aspx")
with col2:
    st.link_button("📦 Custom Order", "https://xometry.looker.com/looks/5286?toggle=fil")
with col3:
    st.link_button("🔄 Cross Ref", "https://www.mitsubishicarbide.net/contents/mmus/enus/manual/material_cross_reference.pdf")
with col4:
    st.link_button("🏷️ Tradenames", "https://eagle-plastics.com/tradename-cross-reference/")
with col5:
    st.link_button("⚖️ Equivalent", "https://www.steelnumber.com/en/search_form_eu.php")
with col6:
    st.link_button("🤖 ChatGPT", "https://chat.openai.com/")

st.divider()

# --- 5. Вкладки с поисковиками ---

# Создаем табы
tab1, tab2 = st.tabs(["🏗️ US Search", "🎡 EU Search"])

# ID поисковиков
CX_MATERIAL = "97baf5a535bf14b02"
CX_PLAYGROUND = "07c6ce5e72f9a46af"

with tab1:
    st.caption("Поиск по базе поставщиков материалов")
    html_code = get_search_html(CX_MATERIAL)
    # scrolling=True важно для длинных результатов
    components.html(html_code, height=900, scrolling=True)

with tab2:
    st.caption("Поиск по Playground базе")
    html_code = get_search_html(CX_PLAYGROUND)
    components.html(html_code, height=900, scrolling=True)







