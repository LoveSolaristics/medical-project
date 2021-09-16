import streamlit as st
import pages.page_1 as p1
import pages.page_2 as p2

from pathlib import Path
import base64


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


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

    st.markdown("## Ресурсы")

    st.markdown(
        """[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>]\
        (https://www.python.org) <small>Python 3.9.7 | Sep 2021</small>""".format(
            img_to_bytes("source/python-logo.png")
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        """[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>]\
        (https://streamlit.io) <small>Streamlit 0.88.0 | Sep 2021</small>""".format(
            img_to_bytes("source/streamlit-logo.png")
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ## Прочее
        [<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>]\
        (https://vk.com/lovesolaristics) <small>Вопросы и предложения</small>""".format(
            img_to_bytes("source/brain.png")
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        [<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>]\
        (https://github.com/LoveSolaristics/medical-project) <small>Исходный код</small>""".format(
            img_to_bytes("source/github-logo.png")
        ),
        unsafe_allow_html=True,
    )

if page == page_names[0]:
    visualization()

elif page == page_names[1]:
    p1.visualization()

elif page == page_names[2]:
    p2.visualization()
