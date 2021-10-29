import streamlit as st

def visualization():
    st.markdown(f"""
    # Определение физической потребности в жидкости""")

    selected = [
        '7 дней - 1 месяц',
        '1 - 3 месяца',
        '4 - 6 месяцев',
        '7 - 9 месяцев',
        '10 - 12 месяцев',
        '1 - 3 года',
        '4 - 6 лет',
        '7 - 9 лет',
        '10 - 12 лет',
        '13 - 15 лет',
    ]

    years = st.selectbox('Выберите возраст', selected)
    weight = st.number_input('Введите вес (в килограммах)', step=1.)

    click = st.button('Рассчитать')

    if years == selected[0]:
        min_value = 100
        max_value = 150
    elif years == selected[1]:
        min_value = 140
        max_value = 160
    elif years == selected[2]:
        min_value = 130
        max_value = 155
    elif years == selected[3]:
        min_value = 125
        max_value = 150
    elif years == selected[4]:
        min_value = 120
        max_value = 135
    elif years == selected[5]:
        min_value = 110
        max_value = 135
    elif years == selected[6]:
        min_value = 90
        max_value = 110
    elif years == selected[7]:
        min_value = 75
        max_value = 90
    elif years == selected[8]:
        min_value = 65
        max_value = 85
    elif years == selected[9]:
        min_value = 40
        max_value = 65

    if click:
        st.info(f'Суточная потреность в жидкости: '
                f'{min(min_value * weight, 2400):.2f} - {min(max_value * weight, 2400):.2f} мл/сутки')