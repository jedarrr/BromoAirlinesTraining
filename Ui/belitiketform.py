# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'belitiketform.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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
        self.widget_4.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font-weight: bold; font-size: 20px;")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.widget_6)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMaximumSize(QSize(400, 16777215))

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 2)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_2 = QGridLayout(self.widget_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.widget_8)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.widget_8)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.widget_8)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 1, 1, 2)


        self.verticalLayout_4.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_3 = QGridLayout(self.widget_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.widget_7)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.comboBox_3, 1, 1, 1, 1)

        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 1, 1, 2)


        self.verticalLayout_4.addWidget(self.widget_7)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.widget_3.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_9 = QWidget(self.widget_3)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_6 = QVBoxLayout(self.widget_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_12 = QLabel(self.widget_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_6.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget_9)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_6.addWidget(self.label_13)


        self.verticalLayout_5.addWidget(self.widget_9)

        self.widget_14 = QWidget(self.widget_3)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_5 = QGridLayout(self.widget_14)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_17 = QLabel(self.widget_14)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMaximumSize(QSize(24, 24))
        self.label_17.setPixmap(QPixmap(u"../../../../../../Documents/SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/calendar-unselected-72.png"))
        self.label_17.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_14 = QLabel(self.widget_14)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.widget_14)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMaximumSize(QSize(24, 24))
        self.label_15.setPixmap(QPixmap(u"../../../../../../Documents/SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/time-five-regular-72.png"))
        self.label_15.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_15, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.label_22 = QLabel(self.widget_14)
        self.label_22.setObjectName(u"label_22")
        sizePolicy3.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy3)

        self.gridLayout_5.addWidget(self.label_22, 2, 1, 1, 1)

        self.label_16 = QLabel(self.widget_14)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setMaximumSize(QSize(24, 24))
        self.label_16.setPixmap(QPixmap(u"../../../../../../Documents/SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/group-regular-72.png"))
        self.label_16.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_16, 3, 0, 1, 1)

        self.label_21 = QLabel(self.widget_14)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)

        self.gridLayout_5.addWidget(self.label_21, 1, 1, 1, 1)

        self.label_23 = QLabel(self.widget_14)
        self.label_23.setObjectName(u"label_23")
        sizePolicy3.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy3)

        self.gridLayout_5.addWidget(self.label_23, 3, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_14)

        self.widget_13 = QWidget(self.widget_3)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_4 = QGridLayout(self.widget_13)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_4 = QLineEdit(self.widget_13)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_4.addWidget(self.lineEdit_4, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.widget_13)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 1, 1, 1, 1)

        self.label_18 = QLabel(self.widget_13)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_13)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy5)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_19 = QLabel(self.widget_10)
        self.label_19.setObjectName(u"label_19")
        sizePolicy5.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy5)
        self.label_19.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.label_19)

        self.label_20 = QLabel(self.widget_10)
        self.label_20.setObjectName(u"label_20")
        sizePolicy5.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy5)
        self.label_20.setStyleSheet(u"font-weight: bold; font-size: 20px;")

        self.horizontalLayout_2.addWidget(self.label_20)


        self.verticalLayout_5.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy5.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy5)
        self.verticalLayout_8 = QVBoxLayout(self.widget_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_2 = QPushButton(self.widget_11)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_8.addWidget(self.pushButton_2)


        self.verticalLayout_5.addWidget(self.widget_11)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Detail Penumpang", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mohon mengisi semua data penumpang", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nama Lengkap", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TItel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Penumpang #1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nama Lengkap", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Penumpang #2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Titel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nama Lengkap", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Titel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Penumpang #3", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Penerbangan", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Detail Penerbangan", None))
        self.label_15.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Pakai", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Kode Promo", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Total Pembayaran", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Konfirmasi Pembayaran", None))
    # retranslateUi

