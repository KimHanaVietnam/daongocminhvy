import json
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtGui import QColor
from ui_index import Ui_MainWindow


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("UEL Library")

        # Sidebar navigation
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_10.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        # Load Transfer table
        self.load_transfer_data()

        # Search filter
        self.lineEdit.textChanged.connect(self.search_table)

    # ================= TRANSFER TABLE =================

    def load_transfer_data(self):
        with open("data/borrow_record.json", "r", encoding="utf-8") as f:
            records = json.load(f)["borrow_record"]

        headers = ["id", "student_id", "book_id", "borrow_date", "due_date", "status"]

        self.transferTable.setColumnCount(len(headers))
        self.transferTable.setHorizontalHeaderLabels(headers)
        self.transferTable.setRowCount(len(records))

        for row, record in enumerate(records):
            for col, key in enumerate(headers):
                item = QTableWidgetItem(record[key])

                # Color status
                if key == "status":
                    if record[key] == "overdue":
                        item.setBackground(QColor(255, 150, 150))
                    elif record[key] == "returned":
                        item.setBackground(QColor(150, 255, 150))
                    else:
                        item.setBackground(QColor(255, 255, 180))

                self.transferTable.setItem(row, col, item)

        self.transferTable.resizeColumnsToContents()

    # ================= SEARCH =================

    def search_table(self, text):
        for row in range(self.transferTable.rowCount()):
            match = False
            for col in range(self.transferTable.columnCount()):
                item = self.transferTable.item(row, col)
                if text.lower() in item.text().lower():
                    match = True
                    break
            self.transferTable.setRowHidden(row, not match)

