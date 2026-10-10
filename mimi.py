import streamlit as st

st.title("Qui est ton ame soeur?")
st.header('Hello Toky')
nom = st.text_input("Quel est le prénom de la fille de tes dreams?")
if st.button('Verifier zoky e'):
  if nom.strip().lower() == "miora":
    st.success('Bravo Bebou')
  else:
    st.error('Non, réessaie !')



