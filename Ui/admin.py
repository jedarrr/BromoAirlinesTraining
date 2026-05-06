    # -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 514)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.topbar = QFrame(self.centralwidget)
        self.topbar.setObjectName(u"topbar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.topbar.sizePolicy().hasHeightForWidth())
        self.topbar.setSizePolicy(sizePolicy1)
        self.topbar.setMaximumSize(QSize(16777215, 100))
        self.topbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.topbar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.topbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_6 = QPushButton(self.topbar)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon = QIcon()
        icon.addFile(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/menu-alt-72.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.label = QLabel(self.topbar)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addWidget(self.topbar, 0, 0, 1, 3)

        self.sidebar_big = QWidget(self.centralwidget)
        self.sidebar_big.setObjectName(u"sidebar_big")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sidebar_big.sizePolicy().hasHeightForWidth())
        self.sidebar_big.setSizePolicy(sizePolicy2)
        self.sidebar_big.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.sidebar_big)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.master_bandara_big = QPushButton(self.sidebar_big)
        self.master_bandara_big.setObjectName(u"master_bandara_big")

        self.verticalLayout.addWidget(self.master_bandara_big)

        self.masterMaskapai_big = QPushButton(self.sidebar_big)
        self.masterMaskapai_big.setObjectName(u"masterMaskapai_big")

        self.verticalLayout.addWidget(self.masterMaskapai_big)

        self.masterjp_big = QPushButton(self.sidebar_big)
        self.masterjp_big.setObjectName(u"masterjp_big")

        self.verticalLayout.addWidget(self.masterjp_big)

        self.masterkp_big = QPushButton(self.sidebar_big)
        self.masterkp_big.setObjectName(u"masterkp_big")

        self.verticalLayout.addWidget(self.masterkp_big)

        self.ubahsp_big = QPushButton(self.sidebar_big)
        self.ubahsp_big.setObjectName(u"ubahsp_big")

        self.verticalLayout.addWidget(self.ubahsp_big)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.sidebar_big, 1, 1, 2, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setMaximumSize(QSize(2000, 16777215))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.masterbandara = QWidget()
        self.masterbandara.setObjectName(u"masterbandara")
        sizePolicy2.setHeightForWidth(self.masterbandara.sizePolicy().hasHeightForWidth())
        self.masterbandara.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.masterbandara)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.masterbandara)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20px;")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.masterbandara)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.masterBandaratable = QTableWidget(self.masterbandara)
        self.masterBandaratable.setObjectName(u"masterBandaratable")
        self.masterBandaratable.setGridStyle(Qt.PenStyle.SolidLine)
        self.masterBandaratable.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.masterBandaratable)

        self.widget_2 = QWidget(self.masterbandara)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.formLayout = QFormLayout(self.widget_3)
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.inputNama = QLineEdit(self.widget_3)
        self.inputNama.setObjectName(u"inputNama")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.inputNama.sizePolicy().hasHeightForWidth())
        self.inputNama.setSizePolicy(sizePolicy4)
        self.inputNama.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.inputNama)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.inputiata = QLineEdit(self.widget_3)
        self.inputiata.setObjectName(u"inputiata")
        sizePolicy4.setHeightForWidth(self.inputiata.sizePolicy().hasHeightForWidth())
        self.inputiata.setSizePolicy(sizePolicy4)
        self.inputiata.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.inputiata)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.inputKota = QLineEdit(self.widget_3)
        self.inputKota.setObjectName(u"inputKota")
        sizePolicy4.setHeightForWidth(self.inputKota.sizePolicy().hasHeightForWidth())
        self.inputKota.setSizePolicy(sizePolicy4)
        self.inputKota.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.inputKota)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.comboBox_2 = QComboBox(self.widget_3)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.comboBox_2)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.inputAlamat = QTextEdit(self.widget_4)
        self.inputAlamat.setObjectName(u"inputAlamat")

        self.gridLayout_4.addWidget(self.inputAlamat, 2, 1, 1, 1)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        sizePolicy5.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)

        self.terminalDropdown = QSpinBox(self.widget_4)
        self.terminalDropdown.setObjectName(u"terminalDropdown")
        self.terminalDropdown.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_4.addWidget(self.terminalDropdown, 1, 1, 1, 1)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.simpanmb = QPushButton(self.widget_5)
        self.simpanmb.setObjectName(u"simpanmb")

        self.gridLayout_5.addWidget(self.simpanmb, 0, 0, 1, 1)

        self.batalmb = QPushButton(self.widget_5)
        self.batalmb.setObjectName(u"batalmb")

        self.gridLayout_5.addWidget(self.batalmb, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_5, 3, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_4)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.masterbandara)
        self.mastermaskapai = QWidget()
        self.mastermaskapai.setObjectName(u"mastermaskapai")
        self.verticalLayout_4 = QVBoxLayout(self.mastermaskapai)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_24 = QLabel(self.mastermaskapai)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;")

        self.verticalLayout_4.addWidget(self.label_24)

        self.label_25 = QLabel(self.mastermaskapai)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_4.addWidget(self.label_25)

        self.tableWidget_2 = QTableWidget(self.mastermaskapai)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_4.addWidget(self.tableWidget_2)

        self.widget_6 = QWidget(self.mastermaskapai)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.formLayout_3 = QFormLayout(self.widget_8)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.lineEdit_4 = QLineEdit(self.widget_8)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy6)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_4)

        self.label_10 = QLabel(self.widget_8)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.lineEdit_5 = QLineEdit(self.widget_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy6.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy6)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_5)

        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.spinBox_3 = QSpinBox(self.widget_8)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        self.spinBox_3.setMaximumSize(QSize(120, 16777215))

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinBox_3)


        self.horizontalLayout_3.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_7)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_7.addWidget(self.pushButton_3, 1, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_7)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_7.addWidget(self.pushButton_4, 1, 2, 1, 1)

        self.textEdit_2 = QTextEdit(self.widget_7)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_7.addWidget(self.textEdit_2, 0, 1, 1, 2)


        self.horizontalLayout_3.addWidget(self.widget_7)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.mastermaskapai)
        self.masterjp = QWidget()
        self.masterjp.setObjectName(u"masterjp")
        self.verticalLayout_5 = QVBoxLayout(self.masterjp)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_22 = QLabel(self.masterjp)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font-size: 20px;\n"
"font-weight: bold;")

        self.verticalLayout_5.addWidget(self.label_22)

        self.label_23 = QLabel(self.masterjp)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_5.addWidget(self.label_23)

        self.masterJpTable = QTableWidget(self.masterjp)
        self.masterJpTable.setObjectName(u"masterJpTable")

        self.verticalLayout_5.addWidget(self.masterJpTable)

        self.widget_9 = QWidget(self.masterjp)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy3.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy3)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy3.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy3)
        self.formLayout_2 = QFormLayout(self.widget_10)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_14 = QLabel(self.widget_10)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.inputKodepenerbangan = QLineEdit(self.widget_10)
        self.inputKodepenerbangan.setObjectName(u"inputKodepenerbangan")
        sizePolicy5.setHeightForWidth(self.inputKodepenerbangan.sizePolicy().hasHeightForWidth())
        self.inputKodepenerbangan.setSizePolicy(sizePolicy5)
        self.inputKodepenerbangan.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.inputKodepenerbangan)

        self.label_15 = QLabel(self.widget_10)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.label_16 = QLabel(self.widget_10)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_16)

        self.label_17 = QLabel(self.widget_10)
        self.label_17.setObjectName(u"label_17")
        sizePolicy5.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy5)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_17)

        self.cbDari = QComboBox(self.widget_10)
        self.cbDari.setObjectName(u"cbDari")
        self.cbDari.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cbDari)

        self.cbKe = QComboBox(self.widget_10)
        self.cbKe.setObjectName(u"cbKe")
        self.cbKe.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cbKe)

        self.cbMaskapai = QComboBox(self.widget_10)
        self.cbMaskapai.setObjectName(u"cbMaskapai")
        self.cbMaskapai.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cbMaskapai)


        self.horizontalLayout_4.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy3.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy3)
        self.gridLayout_6 = QGridLayout(self.widget_11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_18 = QLabel(self.widget_11)
        self.label_18.setObjectName(u"label_18")
        sizePolicy5.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy5)

        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)

        self.inputTanggal = QDateEdit(self.widget_11)
        self.inputTanggal.setObjectName(u"inputTanggal")
        sizePolicy6.setHeightForWidth(self.inputTanggal.sizePolicy().hasHeightForWidth())
        self.inputTanggal.setSizePolicy(sizePolicy6)
        self.inputTanggal.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.inputTanggal, 0, 1, 1, 1)

        self.label_19 = QLabel(self.widget_11)
        self.label_19.setObjectName(u"label_19")
        sizePolicy5.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy5)

        self.gridLayout_6.addWidget(self.label_19, 1, 0, 1, 1)

        self.waktuKeberangkatan = QTimeEdit(self.widget_11)
        self.waktuKeberangkatan.setObjectName(u"waktuKeberangkatan")
        sizePolicy6.setHeightForWidth(self.waktuKeberangkatan.sizePolicy().hasHeightForWidth())
        self.waktuKeberangkatan.setSizePolicy(sizePolicy6)
        self.waktuKeberangkatan.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.waktuKeberangkatan, 1, 1, 1, 1)

        self.label_20 = QLabel(self.widget_11)
        self.label_20.setObjectName(u"label_20")
        sizePolicy5.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy5)

        self.gridLayout_6.addWidget(self.label_20, 2, 0, 1, 1)

        self.durasiPenerbangan = QTimeEdit(self.widget_11)
        self.durasiPenerbangan.setObjectName(u"durasiPenerbangan")
        sizePolicy6.setHeightForWidth(self.durasiPenerbangan.sizePolicy().hasHeightForWidth())
        self.durasiPenerbangan.setSizePolicy(sizePolicy6)
        self.durasiPenerbangan.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.durasiPenerbangan, 2, 1, 1, 1)

        self.label_21 = QLabel(self.widget_11)
        self.label_21.setObjectName(u"label_21")
        sizePolicy5.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy5)

        self.gridLayout_6.addWidget(self.label_21, 3, 0, 1, 1)

        self.inputHargatiket = QSpinBox(self.widget_11)
        self.inputHargatiket.setObjectName(u"inputHargatiket")
        sizePolicy.setHeightForWidth(self.inputHargatiket.sizePolicy().hasHeightForWidth())
        self.inputHargatiket.setSizePolicy(sizePolicy)
        self.inputHargatiket.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.inputHargatiket, 3, 1, 1, 1)

        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy7)
        self.gridLayout = QGridLayout(self.widget_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_7 = QPushButton(self.widget_12)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy6.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.pushButton_7, 0, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_12)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy6.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_12, 4, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.widget_11)


        self.verticalLayout_5.addWidget(self.widget_9)

        self.stackedWidget.addWidget(self.masterjp)
        self.masterkp = QWidget()
        self.masterkp.setObjectName(u"masterkp")
        self.verticalLayout_6 = QVBoxLayout(self.masterkp)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_31 = QLabel(self.masterkp)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20px;")

        self.verticalLayout_6.addWidget(self.label_31)

        self.label_32 = QLabel(self.masterkp)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_6.addWidget(self.label_32)

        self.tableWidget_4 = QTableWidget(self.masterkp)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.verticalLayout_6.addWidget(self.tableWidget_4)

        self.widget_13 = QWidget(self.masterkp)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy8)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy2.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy2)
        self.formLayout_4 = QFormLayout(self.widget_14)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_26 = QLabel(self.widget_14)
        self.label_26.setObjectName(u"label_26")
        sizePolicy5.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy5)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.lineEdit_7 = QLineEdit(self.widget_14)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy6.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy6)
        self.lineEdit_7.setMaximumSize(QSize(200, 16777215))

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_7)

        self.label_27 = QLabel(self.widget_14)
        self.label_27.setObjectName(u"label_27")
        sizePolicy5.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy5)

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_27)

        self.label_28 = QLabel(self.widget_14)
        self.label_28.setObjectName(u"label_28")
        sizePolicy5.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy5)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_28)

        self.label_29 = QLabel(self.widget_14)
        self.label_29.setObjectName(u"label_29")
        sizePolicy5.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy5)

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_29)

        self.dateEdit_2 = QDateEdit(self.widget_14)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        sizePolicy6.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy6)
        self.dateEdit_2.setMaximumSize(QSize(200, 16777215))

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateEdit_2)

        self.spinBox_8 = QSpinBox(self.widget_14)
        self.spinBox_8.setObjectName(u"spinBox_8")
        sizePolicy6.setHeightForWidth(self.spinBox_8.sizePolicy().hasHeightForWidth())
        self.spinBox_8.setSizePolicy(sizePolicy6)
        self.spinBox_8.setMaximumSize(QSize(200, 16777215))

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinBox_8)

        self.spinBox_9 = QSpinBox(self.widget_14)
        self.spinBox_9.setObjectName(u"spinBox_9")
        sizePolicy6.setHeightForWidth(self.spinBox_9.sizePolicy().hasHeightForWidth())
        self.spinBox_9.setSizePolicy(sizePolicy6)
        self.spinBox_9.setMaximumSize(QSize(200, 16777215))

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinBox_9)


        self.horizontalLayout_5.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_13)
        self.widget_15.setObjectName(u"widget_15")
        self.formLayout_5 = QFormLayout(self.widget_15)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_30 = QLabel(self.widget_15)
        self.label_30.setObjectName(u"label_30")
        sizePolicy5.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy5)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_30)

        self.textEdit_3 = QTextEdit(self.widget_15)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.textEdit_3)

        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_8 = QGridLayout(self.widget_16)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pushButton_8 = QPushButton(self.widget_16)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy6.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy6)

        self.gridLayout_8.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.widget_16)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy6.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy6)

        self.gridLayout_8.addWidget(self.pushButton_9, 0, 1, 1, 1)


        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.widget_16)


        self.horizontalLayout_5.addWidget(self.widget_15)


        self.verticalLayout_6.addWidget(self.widget_13)

        self.stackedWidget.addWidget(self.masterkp)
        self.ubahsp = QWidget()
        self.ubahsp.setObjectName(u"ubahsp")
        self.verticalLayout_7 = QVBoxLayout(self.ubahsp)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_33 = QLabel(self.ubahsp)
        self.label_33.setObjectName(u"label_33")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy9)
        self.label_33.setStyleSheet(u"font-weight: bold; font-size: 20px;")

        self.verticalLayout_7.addWidget(self.label_33)

        self.label_34 = QLabel(self.ubahsp)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_7.addWidget(self.label_34)

        self.tableWidget_5 = QTableWidget(self.ubahsp)
        self.tableWidget_5.setObjectName(u"tableWidget_5")

        self.verticalLayout_7.addWidget(self.tableWidget_5)

        self.widget_17 = QWidget(self.ubahsp)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy3.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy3)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_18 = QWidget(self.widget_17)
        self.widget_18.setObjectName(u"widget_18")
        self.formLayout_6 = QFormLayout(self.widget_18)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_35 = QLabel(self.widget_18)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_35)

        self.comboBox = QComboBox(self.widget_18)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy6.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy6)
        self.comboBox.setMaximumSize(QSize(200, 16777215))

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox)


        self.horizontalLayout_6.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        self.formLayout_7 = QFormLayout(self.widget_19)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_36 = QLabel(self.widget_19)
        self.label_36.setObjectName(u"label_36")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_36)

        self.timeEdit_3 = QTimeEdit(self.widget_19)
        self.timeEdit_3.setObjectName(u"timeEdit_3")
        self.timeEdit_3.setMaximumSize(QSize(200, 16777215))

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.timeEdit_3)

        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        self.gridLayout_9 = QGridLayout(self.widget_20)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_10 = QPushButton(self.widget_20)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy6.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy6)
        self.pushButton_10.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_9.addWidget(self.pushButton_10, 0, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.widget_20)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy6.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy6)
        self.pushButton_11.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_9.addWidget(self.pushButton_11, 0, 1, 1, 1)


        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.FieldRole, self.widget_20)


        self.horizontalLayout_6.addWidget(self.widget_19)


        self.verticalLayout_7.addWidget(self.widget_17)

        self.stackedWidget.addWidget(self.ubahsp)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 1, 2, 1, 1)

        self.sidebar_sm = QWidget(self.centralwidget)
        self.sidebar_sm.setObjectName(u"sidebar_sm")
        sizePolicy2.setHeightForWidth(self.sidebar_sm.sizePolicy().hasHeightForWidth())
        self.sidebar_sm.setSizePolicy(sizePolicy2)
        self.sidebar_sm.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_sm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.masterBandara_sm = QPushButton(self.sidebar_sm)
        self.masterBandara_sm.setObjectName(u"masterBandara_sm")
        icon1 = QIcon()
        icon1.addFile(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/map-unselected-72.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.masterBandara_sm.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.masterBandara_sm)

        self.masterMaskapai_sm = QPushButton(self.sidebar_sm)
        self.masterMaskapai_sm.setObjectName(u"masterMaskapai_sm")
        icon2 = QIcon()
        icon2.addFile(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/plane-take-off-unselected-72.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.masterMaskapai_sm.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.masterMaskapai_sm)

        self.masterjp_sm = QPushButton(self.sidebar_sm)
        self.masterjp_sm.setObjectName(u"masterjp_sm")
        icon3 = QIcon()
        icon3.addFile(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/calendar-unselected-72.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.masterjp_sm.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.masterjp_sm)

        self.masterkp_sm = QPushButton(self.sidebar_sm)
        self.masterkp_sm.setObjectName(u"masterkp_sm")
        icon4 = QIcon()
        icon4.addFile(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/purchase-tag-alt-unselected-72.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.masterkp_sm.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.masterkp_sm)

        self.ubahsp_sm = QPushButton(self.sidebar_sm)
        self.ubahsp_sm.setObjectName(u"ubahsp_sm")
        icon5 = QIcon()
        icon5.addFile(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/notepad-unselected-72.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ubahsp_sm.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.ubahsp_sm)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addWidget(self.sidebar_sm, 1, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 797, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_6.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.master_bandara_big.setText(QCoreApplication.translate("MainWindow", u"Master Bandara", None))
        self.masterMaskapai_big.setText(QCoreApplication.translate("MainWindow", u"Master Maskapai", None))
        self.masterjp_big.setText(QCoreApplication.translate("MainWindow", u"Master Jadwal Penerbangan", None))
        self.masterkp_big.setText(QCoreApplication.translate("MainWindow", u"Master Kode Promo", None))
        self.ubahsp_big.setText(QCoreApplication.translate("MainWindow", u"Ubah Status Penerbangan", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Master Bandara", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Semua Bandara yang terdaftar akan muncul disini", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nama", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Kode IATA", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Kota", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Negara", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Jumlah terminal", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Alamat", None))
        self.simpanmb.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.batalmb.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Master Maskapai", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Semua Maskapai yang terdaftar akan muncul disini", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nama", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Perusahaan", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Jumlah Kru", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Deskripsi", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Master Jadwal Penerbangan", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Semua Jadwal Penerbangan akan muncul disini ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Kode Penerbangan", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Dari", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ke", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Maskapai", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Tanggal", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Waktu Keberangkatan", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Durasi Penerbangan", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Harga Per-Tiket", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Master Kode Promo", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Anda bisa mengubah status jadwal penerbangan disini", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Kode Promo", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Berlaku Sampai", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Presentase Diskon", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Maximum Diskon", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Deskripsi", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Ubah Status Penerbangan", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Anda bisa engubah status jadwal penerbangan disini", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Perkiraan Durasi Delay", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Batal", None))
        self.masterBandara_sm.setText("")
        self.masterMaskapai_sm.setText("")
        self.masterjp_sm.setText("")
        self.masterkp_sm.setText("")
        self.ubahsp_sm.setText("")
    # retranslateUi

