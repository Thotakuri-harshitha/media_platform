import streamlit as st
from db_c import conn, cursor

# TITLE
st.title("Media Platform")

# TABS
login, signup = st.tabs(["Login", "Signup"])

# ---------------- LOGIN ---------------- #

with login:

    st.header("Login")

    with st.form("Login_Form"):

        email = st.text_input("Email")

        password = st.text_input("Password", type="password")

        btn = st.form_submit_button("Login")

        if btn:

            cursor.execute("""
            SELECT * FROM users
            WHERE email=%s AND password=%s
            """, (email, password))

            user = cursor.fetchone()

            if user:

                st.success("Login Successful")

                st.write("Welcome", user["name"])

            else:

                st.error("Invalid Email or Password")

# ---------------- SIGNUP ---------------- #

with signup:

    st.header("Signup")

    with st.form("SignUp_Form"):

        name = st.text_input("Name")

        email = st.text_input("Email")

        password = st.text_input("Password", type="password")

        btn = st.form_submit_button("SignUp")

        if btn:

            try:

                cursor.execute("""
                INSERT INTO users(name,email,password)
                VALUES(%s,%s,%s)
                """, (name, email, password))

                conn.commit()

                st.success("Account Created Successfully")

            except:

                st.error("Email Already Exists")