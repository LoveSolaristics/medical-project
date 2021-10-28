import streamlit as st

def visualization():
    st.markdown('# Коррекция электролитов')

    elements = ['Кальций', 'Калий', 'Магний']

    option = st.radio('Выберите нужный элемент:', elements)

    if option == elements[0]:
        st.markdown(f"""
        ## Коррекция кальция
        """)
        years =st.number_input(label='Введите возраст ребенка', min_value=1, max_value=17,
                               help='Ребенком считается человек не старше 17 лет')

        click_1 = st.button('Рассчитать')
        if click_1:
            min_doze = 0.1 * years
            max_doze = 0.5 * years

            st.info(f'Ввводим десятипроцентный раствор\n\n'
                    f'${min(min_doze, 10):.1f} (СаCl) - {min(max_doze, 10):.1f}$ мл/сут ($Са$ глюк.) за $1-2$ введения')

        st.markdown(f"""
        ### Справочная информация
        
        Кальций ФП$=0.1-0.5$ ммоль/кг/сут\n
        (у новорожденных, недоношенных $1-3$ ммоль/кг/сут)\n
        $Ca$ хлорид $10%=1$мл$=1$ ммоль\n
        $Ca$ глюконат $10%=1$ мл $= 0.25$\n""")
    elif option == elements[1]:
        st.markdown("""
        ## Коррекция калия
        """)

        weight = st.number_input(label='Введите вес', min_value=1)
        click_2 = st.button('Рассчитать')

        min_7 = weight
        max_7 = 2 * weight

        min_4 = 2 * weight
        max_4 = 4 * weight

        if click_2:
            st.info(f'Ввводим \n\n'
                    f'7.5% раствор: ${min_7}-{max_7}$ мл/сут\n\n'
                    f'4% раствор: ${min_4}-{max_4}$ мл/сут ')

        st.markdown(f"""
        ### Справочная информация
        
        Калий ФП $= 1,0-2,0$ ммоль/кг/сут\n
        Скорость введения $К$ не должна превышать $0,5$ ммоль/кг/час\n
        Вводим:\n
        - в растворе глюкозы
        - при наличии диуреза
        - суточную дозу делим на $2$ введения
        - концентрация К в растворе не более $1%$
        $7.5%$ р-р $= 1$ мл $= 1$ ммоль\n
        $4%$ р-р $= 1$ мл $= 0.5$ ммоль\n
        Вводим\n
        $7.5%$ р-р $1-2$ мл/кг/сут\n
        $4%$ р-р $2-4$ мл/кг/сут
        """)
    elif option == elements[2]:
        st.markdown("""
        ## Коррекция магния
        """)
        weight = st.number_input(label='Введите вес', min_value=1)
        min_doze = 0.5 * weight
        max_doze = weight

        click_3 = st.button('Рассчитать')
        if click_3:
            st.info(f"""
            Вводим в растворе глюкозы\n
            {min_doze:.1f}-{max_doze:.1f} мл/сут (не более 20 мл за 2 раза)""")

        st.markdown(f"""
        Справочная информация
        
        Магний ФП $= 0.1-0.7$ ммоль/кг/сут\n
        $25% = 1$ мл $= 2$ ммоль\n
        """)

