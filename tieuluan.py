import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# CẤU HÌNH TRANG
# ==========================

st.set_page_config(
    page_title="Dashboard sức khỏe",
    page_icon="🏥",
    layout="wide"
)

# ==========================
# ĐỌC DỮ LIỆU
# ==========================

df = pd.read_csv("clean_data.csv")

# ==========================
# TIÊU ĐỀ
# ==========================

st.title("🏥 HEALTH DASHBOARD")

st.write("Dashboard phân tích dữ liệu sức khỏe")

# ==========================
# THÔNG TIN DỮ LIỆU
# ==========================

st.subheader("Thông tin dữ liệu")

st.write("Số dòng và cột:", df.shape)

st.write("Tên các cột:")

st.write(df.columns.tolist())

# ==========================
# HIỂN THỊ DỮ LIỆU
# ==========================

st.subheader("Dữ liệu gốc")

st.dataframe(df)

# ==========================
# THỐNG KÊ MÔ TẢ
# ==========================

st.subheader("Thống kê mô tả")

st.dataframe(df.describe())

# ==========================
# KPI
# ==========================

st.subheader("Chỉ số tổng quan")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Tổng số bản ghi",
        len(df)
    )

with col2:
    st.metric(
        "Tổng số cột",
        len(df.columns)
    )

# ==========================
# CHỌN CỘT ĐỂ VẼ
# ==========================

st.subheader("Biểu đồ")

cot = st.selectbox(
    "Chọn cột",
    df.columns
)

# ==========================
# BIỂU ĐỒ CỘT
# ==========================

if df[cot].dtype == "object":

    thong_ke = (
        df[cot]
        .value_counts()
        .reset_index()
    )

    thong_ke.columns = [cot, "Số lượng"]

    fig = px.bar(
        thong_ke,
        x=cot,
        y="Số lượng",
        color="Số lượng",
        title=f"Phân bố {cot}"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================
# HISTOGRAM
# ==========================

else:

    fig = px.histogram(
        df,
        x=cot,
        nbins=20,
        title=f"Phân bố {cot}"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
