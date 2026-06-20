import streamlit as st
st.title("user form")
with st.form("user form"):
    name=st.text_input("enter name:")
    email=st.text_input("enter email:")
    age=st.number_input("enter age",min_value=0)
    submit=st.form_submit_button("submit")
if submit:
    if age<0:
        st.error("age must be a valid number")
    if "@" not in email:
        st.error("invalid email1")
    else:
        st.success("form verified successfully")
        st.write("name:",name)
        st.write("email:",email)
        st.write("age:",age)
