# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1390, 921)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setGeometry(QRect(50, 20, 251, 841))
        self.icon_text_widget.setStyleSheet(u"background-color: rgb(0, 0, 167);\n"
"background-color: rgb(59, 59, 59);")
        self.verticalLayout_3 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_3.setSpacing(55)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(19, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(self.icon_text_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/grid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_7 = QPushButton(self.icon_text_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/book-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.icon_text_widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/eye.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.icon_text_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/users.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_10 = QPushButton(self.icon_text_widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/globe.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.pushButton_10)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_12 = QPushButton(self.icon_text_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.icon_text_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_11)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(340, 20, 971, 841))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.layoutWidget1 = QWidget(self.header_widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 20, 344, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(u"pushButton")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(135, 135, 135);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(15)
        self.label.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label)

        self.layoutWidget2 = QWidget(self.header_widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(500, 0, 321, 81))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QlineEdit{\n"
"  padding-left:20px;\n"
"  border:1px-solid gray;\n"
"  border-radius: 20px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.widget = QWidget(self.layoutWidget2)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout_3.addWidget(self.widget)

        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(135, 135, 135);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(135, 135, 135);")
        self.label_4.setPixmap(QPixmap(u":/icons/icons/user.svg"))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.stackedWidget = QStackedWidget(self.header_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-10, 100, 941, 741))
        self.stackedWidget.setMaximumSize(QSize(941, 741))
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setMaximumSize(QSize(841, 741))
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 240, 161, 71))
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMaximumSize(QSize(841, 741))
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(310, 250, 55, 16))
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMaximumSize(QSize(841, 741))
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(350, 280, 55, 16))
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setMaximumSize(QSize(841, 741))
        self.transferTable = QTableWidget(self.page_4)
        if (self.transferTable.columnCount() < 6):
            self.transferTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.transferTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.transferTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.transferTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.transferTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.transferTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.transferTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.transferTable.setObjectName(u"transferTable")
        self.transferTable.setGeometry(QRect(30, 250, 911, 481))
        self.transferTable.setStyleSheet(u"QHeaderView::section{\n"
"    font-weight: bold;\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"    alternate-background-color: #B0EDFB;\n"
"    background-color: #F4F9FA;\n"
"}\n"
"")
        self.label_9 = QLabel(self.page_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(134, 75, 91, 51))
        self.label_9.setPixmap(QPixmap(u":/icons/icons/alert-circle.svg"))
        self.widget_2 = QWidget(self.page_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(40, 70, 221, 101))
        self.widget_2.setStyleSheet(u"background-color: white;\n"
"background-color: rgb(187, 191, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid #dddddd;\n"
"")
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 30, 55, 31))
        self.label_11.setPixmap(QPixmap(u":/icons/icons/clock.svg"))
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(60, 30, 121, 31))
        self.label_14.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.widget_3 = QWidget(self.page_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(300, 70, 221, 101))
        self.widget_3.setStyleSheet(u"background-color: white;\n"
"background-color: rgb(255, 135, 161);\n"
"border-radius: 15px;\n"
"border: 1px solid #dddddd;\n"
"")
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 30, 55, 31))
        self.label_12.setPixmap(QPixmap(u":/icons/icons/alert-circle.svg"))
        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(60, 40, 101, 16))
        self.label_16.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.widget_4 = QWidget(self.page_4)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(550, 70, 221, 101))
        self.widget_4.setStyleSheet(u"background-color: white;\n"
"background-color: rgb(225, 253, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid #dddddd;\n"
"")
        self.label_13 = QLabel(self.widget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 30, 55, 31))
        self.label_13.setPixmap(QPixmap(u":/icons/icons/thumbs-up.svg"))
        self.label_17 = QLabel(self.widget_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 40, 171, 21))
        self.label_17.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setMaximumSize(QSize(841, 741))
        self.label_10 = QLabel(self.page_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(300, 280, 55, 16))
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_4.addWidget(self.header_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.layoutWidget1.raise_()
        self.icon_text_widget.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"      UEL LIBRARY", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Readers", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Community", None))
        self.pushButton_12.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"SIGN OUT", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to your page.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello, Vy !", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search here....", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"dashboard", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"books", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"readers", None))
        ___qtablewidgetitem = self.transferTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.transferTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"student_id", None));
        ___qtablewidgetitem2 = self.transferTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"book_id", None));
        ___qtablewidgetitem3 = self.transferTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"borrow_date", None));
        ___qtablewidgetitem4 = self.transferTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"due_date", None));
        ___qtablewidgetitem5 = self.transferTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"status", None));
        self.label_9.setText("")
        self.label_11.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Borrowing : 3", None))
        self.label_12.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Overdue : 3", None))
        self.label_13.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Already returned : 4", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"community", None))
    # retranslateUi

