# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daftar.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20px;\n"
"")

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.formLayout = QFormLayout(self.widget_5)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.lineEdit = QLineEdit(self.widget_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_2)

        self.lineEdit_4 = QLineEdit(self.widget_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.widget_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit_5)

        self.dateEdit = QDateEdit(self.widget_5)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateEdit)

        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.pushButton)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setPixmap(QPixmap(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Logo - With Padding/Logo Rect Alt - Without Tagline.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_8)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 797, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Daftar Akun", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"daftarkan diri disini untuk menggunakan Bromo Airlines", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nama", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tanggal Lahir", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nomor Telepon", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Daftar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sudah Punya Akun?", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_8.setText("")
    # retranslateUi

