import streamlit as st
import pages.page_1 as p1
import pages.page_2 as p2

st.set_page_config(
    page_title="СГМУ", page_icon='🔬',
)


def visualization():
    st.markdown("""# Привет\nЭта страничка является вводной. Интересующий 
    раздел можно выбрать в боковом меню.""")


page_names = ['Вводная страничка', 'Раздел 1', 'Раздел 2']

with st.sidebar:
    st.markdown('# Место для названия')
    st.markdown('Место для какого-нибудь текста')
    page = st.selectbox('Выберите раздел', page_names)

if page == page_names[0]:
    visualization()

elif page == page_names[1]:
    p1.visualization()

elif page == page_names[2]:
    p2.visualization()
