# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listpenerbangan.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"font-weight: bold; font-size: 20px;")

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.checkBox = QCheckBox(self.widget_4)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.widget_4)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.widget_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.widget_4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout.addWidget(self.checkBox_4)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_5 = QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.comboBox = QComboBox(self.widget_7)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_5.addWidget(self.comboBox)


        self.horizontalLayout_2.addWidget(self.widget_7)

        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.tableWidget)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"List Penerbangan", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"FIlter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Waktu Keberangkatan", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"00:00 - 06:00", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"06:00 - 12:00", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"12:00 - 18:00", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"18:00 - 24:00", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Urutkan Beradasarkan", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

