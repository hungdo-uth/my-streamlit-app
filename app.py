import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Tạo DataFrame dữ liệu
du_lieu = {
    "Họ và tên" : ["Lê Công Tuấn Anh", "Trần Ngọc Anh", "Đỗ Xuân Anh", "Lê Nguyễn Quốc Bảo", "Đỗ Huy Cường", "Hoàng Nguyễn Thế Công", "Tống Đăng Dương", "Tống Đăng Duy", "Vũ Đình Trường Giang", "Đỗ Thiên Hưng" ],
    "Chuyên cần" : [9, 8, 9, 10, 8, 9, 7, 7.8, 9, 9],
    "Giữa kỳ" : [8, 7.5, 8.5, 6.5, 5.5, 10, 8, 9, 7.5, 8.5 ],
    "Cuối kỳ" : [7.5, 8, 8.5, 9, 7, 8, 7.7, 8, 9, 8],
}
df = pd.DataFrame(du_lieu)

# Tính điểm tổng kết
df["Tổng kết"] = 0.2*df["Chuyên cần"] + 0.3*df["Giữa kỳ"] + 0.5*df["Cuối kỳ"]

# Hàm Xếp loại
def xep_loai(diem):
    if diem >= 8.5: return "Giỏi"
    elif diem >= 7: return "Khá"
    elif diem >= 5: return "Trung bình"
    else: return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 2. Hiển thị bảng điểm
st.subheader("1. Bảng điểm chi tiết")
st.dataframe(df)

# 3, 4, 5. Thống kê
st.subheader("2. Thống kê lớp học")
diem_tb = df["Tổng kết"].mean()
so_sv_dat = len(df[df["Tổng kết"] >= 5])

# Tìm sinh viên cao điểm nhất và thấp điểm nhất
max_diem = df["Tổng kết"].max()
min_diem = df["Tổng kết"].min()
sv_cao_nhat = ", ".join(df[df["Tổng kết"] == max_diem]["Họ và tên"].tolist())
sv_thap_nhat = ", ".join(df[df["Tổng kết"] == min_diem]["Họ và tên"].tolist())

st.write(f"- **Điểm trung bình của lớp:** {diem_tb:.2f}")
st.write(f"- **Sinh viên cao điểm nhất:** {sv_cao_nhat} ({max_diem} điểm)")
st.write(f"- **Sinh viên thấp điểm nhất:** {sv_thap_nhat} ({min_diem} điểm)")
st.write(f"- **Số sinh viên đạt (>= 5.0):** {so_sv_dat}")

# 6, 7. Tra cứu điểm sinh viên bằng Selectbox
st.subheader("3. Tra cứu thông tin")
ten_sv = st.selectbox("Chọn một sinh viên để xem điểm:", df["Họ và tên"])

# Lấy thông tin sinh viên được chọn
thong_tin_sv = df[df["Họ và tên"] == ten_sv].iloc[0]

# Hiển thị thông tin
st.write(f"**Chuyên cần:** {thong_tin_sv['Chuyên cần']} | **Giữa kỳ:** {thong_tin_sv['Giữa kỳ']} | **Cuối kỳ:** {thong_tin_sv['Cuối kỳ']}")
st.write(f"**Điểm tổng kết:** {thong_tin_sv['Tổng kết']:.2f} | **Xếp loại:** {thong_tin_sv['Xếp loại']}")

# 8. Hiển thị biểu đồ cột
st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Họ và tên"], df["Tổng kết"], color='royalblue')
ax.set_xlabel("Tên sinh viên")
ax.set_ylabel("Điểm")
ax.set_title("Điểm tổng kết của 10 sinh viên")
plt.xticks(rotation=45, ha='right')
ax.set_ylim(0, 10)
plt.tight_layout()

st.pyplot(fig)

# 9. Hiển thị thông tin người tạo ở cuối trang
st.markdown("---")
st.caption("Người tạo ứng dụng: [Đỗ Thiên Hưng] - MSSV: [045208005880]")
