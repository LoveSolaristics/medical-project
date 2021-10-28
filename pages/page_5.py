import streamlit as st

def visualization():
    st.markdown(f"""
    # Расчет жидкости при обезвоживании""")


    selected_degree = ['I степень (5%)', 'II степень (6-9%)', 'III степень (10%)']
    degree = st.selectbox('Выберите степень обезвоживания', selected_degree)

    selected_age = ['1 месяц - 1 год', '1 - 5 лет', '5 - 10 лет']
    age = st.selectbox('Выберите возраст', selected_age)

    weight = st.number_input('Введите вес', step=1)

    answers_min = [
        150, 120, 75,
        180, 150, 110,
        200, 180, 130
    ]

    answers_max = [
        170, 150, 100,
        200, 170, 110,
        250, 200, 130
    ]

    click = st.button('Рассчитать')
    if click:
        idx_1 = selected_degree.index(degree)
        idx_2 = selected_age.index(age)

        idx = idx_1 + 3 * idx_2
        st.info(f'{answers_min[idx] * weight} - {answers_max[idx] * weight} мл')