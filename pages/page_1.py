import streamlit as st


def input_file():
    infections, codes = [''], {}

    with open('source/mkb.txt', 'r') as f:
        infection = ''
        for line in f:
            line = line.strip()

            if line == '':
                infection = ''
                continue

            if not infection:
                infection = line
                infections.append(infection)
                continue

            if infection not in codes:
                codes[infection] = []

            code, text = line.split(' ', 1)
            codes[infection].append((code, text,))

    return infections, codes


def visualization():
    st.markdown('# Раздел 1')
    st.markdown('Введите название инфекции, а мы выведем её код.')

    infections, codes = input_file()

    user_input = st.selectbox('Инфекция', infections)

    if user_input:
        output = ''
        for code, text in codes[user_input]:
            output += '__' + code + '__ '
            output += text
            output += '\n\n'

        st.markdown(output)
