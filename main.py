import streamlit as st
import pages.page_1 as p1
import pages.page_2 as p2
import pages.page_3 as p3
import pages.page_4 as p4
import pages.page_5 as p5

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
    st.markdown(f"""
    # Актуальность
    В настоящее время разработка различных информационных систем и приложений для врачей является актуальной ветвью развития медицины.
    Создание подобных технологических продуктов помогает в принятии обоснованных клинических решений, тем самым улучшая качество оказания медицинской помощи.

    Разрабатываемое нами веб-приложение «Кишечные инфекции» может быть полезно для практикующих врачей, ординаторов, а также студентов мед. учреждений. С его помощью возможно сокращение времени расчетов физиологической потребности в жидкости в зависимости от степени дегидратации у больных с кишечными инфекциями, дозировок электролитов и основных лекарственных средств.
    """)


page_names = ['Вводная страничка', 'Кишечные инфекции (МКБ10)',
              'Определение степени дегидратации',
              'Коррекция электролитов',
              'Определение физической потребности в жидкости',
              'Расчет жидкости при обезвоживании']

with st.sidebar:
    st.markdown('# Кишечные инфекции')
    # st.markdown('(написано гениями)')
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

elif page == page_names[3]:
    p3.visualization()

elif page == page_names[4]:
    p4.visualization()

elif page == page_names[5]:
    p5.visualization()
