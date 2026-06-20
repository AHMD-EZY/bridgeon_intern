import streamlit as st
name = st.text_input("Name")
age=st.number_input("enter age:")
city=st.selectbox("select city=>",["mlp","tvm","ekm"])
st.write(city)
accept=st.checkbox("terms and conditions")
date=st.date_input("input date")
st.write(date)