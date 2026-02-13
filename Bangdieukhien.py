import json
import os
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from giao_dien_tong_hop import Ui_MainWindow 

class ThuVienApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 1. KẾT NỐI SỰ KIỆN BẤM NÚT (SIDEBAR)
        # Khi nhấn nút Bảng điều khiển trên Menu
        self.ui.btn_dashboard.clicked.connect(self.hien_thi_dashboard)
        
        # Kết nối thanh tìm kiếm
        self.ui.btn_search.clicked.connect(self.xu_ly_tim_kiem)
        self.ui.txt_search.returnPressed.connect(self.xu_ly_tim_kiem)

        # self.hien_thi_dashboard(): để test

    # --- ĐOẠN CODE BẢNG ĐIỀU KHIỂN ---
    def hien_thi_dashboard(self):
        """Hàm này để anh Tú làm Đăng nhập gọi sau khi check user thành công"""
        # Chuyển sang trang Dashboard (thường là Index 1 nếu Index 0 là Login)
        self.ui.stackedWidget.setCurrentIndex(1)
        
        # Cập nhật số liệu mới nhất từ file JSON
        self.doc_du_lieu_va_hien_thi()
        print("Trang Dashboard đã được cập nhật số liệu thật!")

    def doc_du_lieu_va_hien_thi(self):
        try:
            # Đường dẫn đến folder data
            data_dir = 'data'
            
            # Đọc Sách
            with open(os.path.join(data_dir, 'books.json'), 'r', encoding='utf-8') as f:
                books = json.load(f)['books']
            
            # Đọc Sinh viên
            with open(os.path.join(data_dir, 'students.json'), 'r', encoding='utf-8') as f:
                students = json.load(f)['students']
                
            # Đọc Hồ sơ mượn
            with open(os.path.join(data_dir, 'borrow_record.json'), 'r', encoding='utf-8') as f:
                borrows = json.load(f)['borrow_record']

            # --- LOGIC TÍNH TOÁN ---
            total_books = sum(b['total_quantity'] for b in books) # Kết quả: 33
            total_students = len(students) # Kết quả: 5
            
            # Đếm theo trạng thái trong file borrow_record.json
            borrowing_count = len([r for r in borrows if r['status'] == 'borrowing'])
            overdue_count = len([r for r in borrows if r['status'] == 'overdue'])

            # --- ĐỔ VÀO GIAO DIỆN ---
            # (ObjectName tương ứng giao diện)
            self.ui.lbl_total_books.setText(str(total_books))
            self.ui.lbl_total_students.setText(str(total_students))
            self.ui.lbl_borrowing.setText(str(borrowing_count))
            self.ui.lbl_overdue.setText(str(overdue_count))

        except Exception as e:
            QMessageBox.critical(self, "Lỗi dữ liệu", f"Không thể đọc file JSON: {str(e)}")

    def xu_ly_tim_kiem(self):
        query = self.ui.txt_search.text().strip().lower()
        if not query:
            return

        with open('data/books.json', 'r', encoding='utf-8') as f:
            books = json.load(f)['books']
        
        # Tìm kiếm theo tên hoặc mã sách
        results = [b['title'] for b in books if query in b['title'].lower() or query in b['code'].lower()]
        
        if results:
            QMessageBox.information(self, "Kết quả", f"Tìm thấy: {', '.join(results)}")
        else:
            QMessageBox.warning(self, "Thông báo", "Không tìm thấy nội dung yêu cầu.")

# --- KHỞI CHẠY ---
if __name__ == "__main__":
    app = QApplication([])
    window = ThuVienApp()
    window.show()
    app.exec()