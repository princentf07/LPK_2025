import streamlit as st

st.write("Hello, *MINuS* :sunglasses:")




st.title("This is a title")
st.title(":blue[PENENTUAN BILANGAN GANJIL GENAP] :sunglasses:")
st.title(":orange[coba masukan angkamu]")

number = st.number_input("Insert a number", min_value=0, max_value=1000000000000)
if number%2==1:
  st.write('bilangan', number, 'termasuk bilangan ganjil')
else:
  st.write('bilangan', number, 'termasuk bilangan genap')
