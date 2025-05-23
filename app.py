import streamlit as st
import pandas as pd

# โหลดข้อมูล
df = pd.read_csv("visit_counts_for_streamlit.csv", parse_dates=["Date"])

# ตัวเลือกวันที่
st.title("📊 Dashboard: จำนวนผู้ป่วยรายวัน")
start_date = st.date_input("📅 วันที่เริ่ม", df["Date"].min().date())
end_date = st.date_input("📅 วันที่สิ้นสุด", df["Date"].max().date())

# กรองข้อมูล
filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]

# แสดงกราฟ
st.line_chart(filtered_df.set_index("Date")["VisitCount"])
