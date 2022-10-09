import streamlit as st
import pandas as pd
import sqlite3
import numpy as np

st.title('Dev Club Visualize')

st.header("Dev Club Database")
st.markdown("นี่เป็น visualize สำหรับการแข่งขัน dev_mountain hackathon season 2 โดยการจัดการข้อมูล python เป็นหลัก และแสดงผลโดยใช้ streamlit", unsafe_allow_html=False)

st.subheader("Dev Club Data")
@st.cache
def load_data():
    props = ["EMPID", "PASSPORT", "FIRSTNAME", "LASTNAME", "GENDER", "BIRTHDAY",
             "NATIONALITY", "HIRED", "DEPT", "POSITION", "STATUS", "REGION"]
    conn = sqlite3.connect('devclub.db')
    c = conn.cursor()
    c.execute("SELECT * FROM devclub")
    data = c.fetchall()
    result = pd.DataFrame(data,columns=props)
    return result

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")


st.dataframe(data)

st.markdown("โดยสามารถแสดงผลลัพธ์ที่น่าสนใจได้ต่างๆนาๆ ดังนี้", unsafe_allow_html=False)

st.subheader("Region")
st.bar_chart(data['REGION'].value_counts())

st.subheader("NATIONALITY")
st.bar_chart(data['NATIONALITY'].value_counts())