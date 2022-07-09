# Reflexionar papel/lapiz en formas posibles por la factorizacion en primos del numero n elegido

from nombres import *
import streamlit as st


st.set_page_config(page_title='Nombres Aléatoires', page_icon=':game_die:', layout="wide", initial_sidebar_state="auto", menu_items=None)

st.markdown('# Nombres :game_die:')

columns = st.columns([2, 10])

with columns[0]:
    digits = st.number_input('# Chiffres', min_value=1, value=1, step=1)
    refresh_button = st.button('Rafraîchir')

if refresh_button:

    left_operand = str(generate_random_num_digits(digits))
    right_operand = str(generate_random_num_digits(digits))
    
    
    with columns[1]:
        st.latex('\Huge' + left_operand + '+' + right_operand)
        # st.markdown(html_header, unsafe_allow_html=True)
        # st.markdown('# {str(generate_random_num(n))} :x:')
        
  

            







