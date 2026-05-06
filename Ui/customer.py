# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

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
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QSize(16777215, 120))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMaximumSize(QSize(300, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setPixmap(QPixmap(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Logo - With Padding/Logo Alt.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/airplane-ticket.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(36, 36))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/log-out-alt-72.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(36, 36))

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy4.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy4)
        self.lineEdit_2.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.dateEdit = QDateEdit(self.widget_6)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy4.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy4)
        self.dateEdit.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.dateEdit, 3, 0, 1, 1)

        self.spinBox = QSpinBox(self.widget_6)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy4.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy4)
        self.spinBox.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.spinBox, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_6)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.widget_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")

        self.horizontalLayout_5.addWidget(self.widget_7)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_7.setPixmap(QPixmap(u"../SOAL LKS 25/SOAL LKS 25/IT SOFTWARE SOLUTION/Resources/Icons/mountain.png"))

        self.verticalLayout.addWidget(self.label_7)

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
        self.label_6.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Berangkat Dari", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tujuan ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tanggal Berangkat", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Jumlah Penumpang", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Cari Penerbangan", None))
        self.label_7.setText("")
    # retranslateUi

