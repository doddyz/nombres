# Ajustar logica para de verdad reflejar calculo por digito/cifra (papel/lapiz primero)
# Anadir relevador de resultado con un expander justo debajo de la suma

from nombres import *
import streamlit as st


st.set_page_config(page_title='Nombres Aléatoires', page_icon=':game_die:', layout="wide", initial_sidebar_state="auto", menu_items=None)

st.markdown('# Nombres :game_die:')

columns = st.columns([2, 10])

with columns[0]:
    digits = st.number_input('# Chiffres', min_value=1, max_value=4, step=1)
    refresh_button = st.button('Rafraîchir')

if refresh_button:

    left_operand = str(generate_random_num_digits(digits))
    right_operand = str(generate_random_num_digits(digits))
    
    
    with columns[1]:
        st.latex('\Huge' + left_operand + '*' + right_operand)        
  

            







