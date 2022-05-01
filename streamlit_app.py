# Reflexionar papel/lapiz en formas posibles por la factorizacion en primos del numero n elegido

from nombres import *
import streamlit as st


st.set_page_config(page_title='Nombres Aléatoires', page_icon=':game_die:', layout="wide", initial_sidebar_state="auto", menu_items=None)

st.markdown('# Nombres :game_die:')

columns = st.columns([1.5, 10])

with columns[0]:
    n = st.number_input('Max', min_value=2, value=100, step=10)
    refresh_button = st.button('Rafraîchir')

if refresh_button:
    html_header = '<h1 style="font-size:150px">' + str(generate_random_num(n)) + '</h1>'
    with columns[1]:
        st.markdown(html_header, unsafe_allow_html=True)
  

            







