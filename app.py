import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#1 Tạo DataFrame
du_lieu = {
    "Họ và tên" : ["Lê Công Tuấn Anh", "Trần Ngọc Anh", "Đỗ Xuân Anh", "Lê Nguyễn Quốc Bảo", "Đỗ Huy Cường ","Hoàng Nguyễn Thế Công ", "Tống Đăng Dương", "Tống Đăng Duy", "Vũ Đình Trường Giang", "Đỗ Thiên Hưng" ],
    "Chuyên cần" : [9, 8, 9, 10, 8, 9, 7, 7.8, 9, 9],
    "Giữa kỳ" : [8, 7.5, 8.5, 6.5, 5.5, 10, 8, 9, 7.5, 8.5 ],
    "Cuối kỳ" : [7.5, 8, 8.5, 9, 7, 8, 7.7, 8, 9, 8],
}
df = pd.DataFrame(du_lieu)

#2 Tính điểm tổng kết
df["Tổng kết"] = 0.2*df["Chuyên cần"] + 0.3*df["Giữa kỳ"] + 0.5*df["Cuối kỳ"]

#3 Xếp loại sinh viên
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
#4 Thống kê
print("\n Bảng thống kê")
diem = df["Tổng kết"].tolist()
trung_binh = sum(diem) / len(diem)
so_sinh_vien_dat = sum(1 for i in diem if i >= 5)

print(f"Điểm trung bình của lớp: {round(trung_binh, 2)}")
print(f"Điểm cao nhất: {max(diem)}")
print(f"Điểm thấp nhất: {min(diem)}")
print(f"Số sinh viên đạt: {so_sinh_vien_dat}")

#5 Trực quan hóa
plt.figure(figsize=(10, 5,))
plt.bar(df["Họ và tên"], df["Tổng kết"], color='royalblue')
plt.xlabel("Tên sinh viên")
plt.ylabel("Điểm")
plt.title("Điểm tổng kết của 10 sinh viên")
plt.xticks(rotation=45,ha='right' )
plt.ylim(0, 10)
plt.tight_layout()
plt.show()
