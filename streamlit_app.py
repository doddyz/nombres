# Reflexionar papel/lapiz en formas posibles por la factorizacion en primos del numero n elegido

from nombres import *
import streamlit as st


st.set_page_config(page_title='Nombres Aléatoires', page_icon=':game_die:', layout="wide", initial_sidebar_state="auto", menu_items=None)

st.markdown('# Nombres :game_die:')

n = st.sidebar.number_input('Max', min_value=2, value=100, step=10)

columns = st.columns(2)

refresh_button = st.sidebar.button('Rafraîchir')

if refresh_button:
    html_header = '<h1 style="font-size:150px">' + str(generate_random_num(n)) + '</h1>'
    st.markdown(html_header, unsafe_allow_html=True)
  

            







