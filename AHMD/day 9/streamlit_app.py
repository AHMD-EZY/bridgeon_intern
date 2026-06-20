import streamlit as st
import requests

if "token" not in st.session_state:
    st.session_state.token = None

if st.session_state.token is None:

    st.title("Login Page")

    with st.form("login_form"):

        email = st.text_input(
            "Email",
            placeholder="Enter email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        submit = st.form_submit_button("Login")

    if submit:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/login",
                json={
                    "email": email,
                    "password": password
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state.token = data["token"]

                st.success("Login Successful")

                st.rerun()

            else:

                st.error(response.json()["detail"])

        except requests.exceptions.ConnectionError:

            st.error("FastAPI server is not running")

else:

    st.title("Dashboard")

    st.success("Logged In")

    st.write("Token:", st.session_state.token)

    if st.button("Logout"):

        st.session_state.token = None

        st.rerun()