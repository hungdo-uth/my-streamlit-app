import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title("Bảng Điểm Sinh Viên")

# 1. Tạo DataFrame (đã sửa lỗi xuống dòng trong tên)
du_lieu = {
    "Họ và tên" : ["Lê Công Tuấn Anh", "Trần Ngọc Anh", "Đỗ Xuân Anh", "Lê Nguyễn Quốc Bảo", "Đỗ Huy Cường", "Hoàng Nguyễn Thế Công", "Tống Đăng Dương", "Tống Đăng Duy", "Vũ Đình Trường Giang", "Đỗ Thiên Hưng" ],
    "Chuyên cần" : [9, 8, 9, 10, 8, 9, 7, 7.8, 9, 9],
    "Giữa kỳ" : [8, 7.5, 8.5, 6.5, 5.5, 10, 8, 9, 7.5, 8.5 ],
    "Cuối kỳ" : [7.5, 8, 8.5, 9, 7, 8, 7.7, 8, 9, 8],
}
df = pd.DataFrame(du_lieu)

# 2. Tính điểm tổng kết
df["Tổng kết"] = 0.2*df["Chuyên cần"] + 0.3*df["Giữa kỳ"] + 0.5*df["Cuối kỳ"]

# 3. Xếp loại sinh viên
def xep_loai(diem_tong_ket):
    if diem_tong_ket >= 8.5:
        return "Giỏi"
    elif diem_tong_ket >= 7:
        return "Khá"
    elif diem_tong_ket >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# Hiển thị bảng dữ liệu lên giao diện
st.subheader("1. Bảng điểm chi tiết")
st.dataframe(df)

# 4. Thống kê
st.subheader("2. Thống kê chung")
diem = df["Tổng kết"].tolist()
trung_binh = sum(diem) / len(diem)
so_sinh_vien_dat = sum(1 for i in diem if i >= 5)

# Chia cột để hiển thị các chỉ số thống kê
col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm trung bình", round(trung_binh, 2))
col2.metric("Điểm cao nhất", max(diem))
col3.metric("Điểm thấp nhất", min(diem))
col4.metric("Số sinh viên đạt", so_sinh_vien_dat)

# 5. Trực quan hóa
st.subheader("3. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Họ và tên"], df["Tổng kết"], color='royalblue')
ax.set_xlabel("Tên sinh viên")
ax.set_ylabel("Điểm")
ax.set_title("Điểm tổng kết của 10 sinh viên")
plt.xticks(rotation=45, ha='right')
ax.set_ylim(0, 10)
plt.tight_layout()

# Đưa biểu đồ lên Streamlit
st.pyplot(fig)
