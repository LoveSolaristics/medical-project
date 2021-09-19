import streamlit as st


def visualization():
    st.markdown('# Определение степени дегидратации')
    st.markdown('Шкала клинической оценки степени дегидратации.')

    a_keys = ['Нормальный',
              'Жажда, беспокойство, раздражительность',
              'Сонный, вялый, слабый']
    a = st.selectbox('Внешний вид', a_keys)

    b_keys = ['Нормальные', 'Слегка запавшие', 'Очень запавшие']
    b = st.selectbox('Глаза', b_keys)

    c_keys = ['Влажные', 'Липкие', 'Сухие']
    c = st.selectbox('Слизистые', c_keys)

    d_keys = ['Есть', 'Мало', 'Отстутствуют']
    d = st.selectbox('Слезы', d_keys)

    result = st.button('Рассчитать')
    if result:
        points = a_keys.index(a) + \
                 b_keys.index(b) + \
                 c_keys.index(c) + \
                 d_keys.index(d)

        if points == 0 or points > 5:
            st.warning(f'{points} баллов')
        elif points == 1:
            st.warning(f'{points} балл')
        else:
            st.warning(f'{points} балла')

        if points == 0:
            st.info('Дегидратация отстутстует')
        elif points <= 4:
            st.info('Легкая дегидратация')
        else:
            st.info('Дегидратация средней и тяжелой степени')
