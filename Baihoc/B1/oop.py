# tao class HinhChuNhat
class Hinh_chu_nhat:
    # thuoc tinh: chieu dai, chieu rong
    def __init__(self, chieu_dai, chieu_rong):
        # chuyen thuoc tinh ve dang private
        self.__chieu_dai = chieu_dai
        self.__chieu_rong = chieu_rong

    # phuong thuc: tinhChuVi, tinhDienTich
    def tinh_chu_vi(self):
        return 2 * (self.__chieu_dai + self.__chieu_rong)

    def tinh_dien_tich(self):
        return self.__chieu_dai * self.__chieu_rong


# tao doi tuong hinh chu nhat
hinh_1 = Hinh_chu_nhat(12, 3)
# sua lai gia tri cho thuoc tinh
# hinh_1.chieu_dai = "a"
hinh_1.__chieu_dai = 123  # khong hoat dong duoc

# in ra chu vi va dien tich
print(hinh_1.tinh_chu_vi())
print(hinh_1.tinh_dien_tich())
