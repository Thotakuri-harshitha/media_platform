import mysql.connector
import streamlit as st

# DATABASE CONNECTION
conn = mysql.connector.connect(
    host=st.secrets["MYSQL_HOST"],
    port=int(st.secrets["MYSQL_PORT"]),
    user=st.secrets["MYSQL_USER"],
    password=st.secrets["MYSQL_PASSWORD"],
    database=st.secrets["MYSQL_DB"]
)

# CURSOR
cursor = conn.cursor(dictionary=True)

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
)
""")

conn.commit()

print("Database Connected Successfully")