# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Slagalica.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1024, 720))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setStyleSheet(u"background-color: rgb(179, 179, 179);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PretragaBezProtivnika = QPushButton(self.frame_2)
        self.PretragaBezProtivnika.setObjectName(u"PretragaBezProtivnika")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.PretragaBezProtivnika.sizePolicy().hasHeightForWidth())
        self.PretragaBezProtivnika.setSizePolicy(sizePolicy1)
        self.PretragaBezProtivnika.setMinimumSize(QSize(200, 75))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PretragaBezProtivnika.setFont(font)
        self.PretragaBezProtivnika.setStyleSheet(u"background-color: rgba(125, 125, 125, 155);")

        self.horizontalLayout.addWidget(self.PretragaBezProtivnika)

        self.PretragaSaProtivnikom = QPushButton(self.frame_2)
        self.PretragaSaProtivnikom.setObjectName(u"PretragaSaProtivnikom")
        sizePolicy1.setHeightForWidth(self.PretragaSaProtivnikom.sizePolicy().hasHeightForWidth())
        self.PretragaSaProtivnikom.setSizePolicy(sizePolicy1)
        self.PretragaSaProtivnikom.setMinimumSize(QSize(200, 75))
        self.PretragaSaProtivnikom.setFont(font)
        self.PretragaSaProtivnikom.setStyleSheet(u"background-color: rgba(125, 125, 125, 155);")

        self.horizontalLayout.addWidget(self.PretragaSaProtivnikom)

        self.QLearning = QPushButton(self.frame_2)
        self.QLearning.setObjectName(u"QLearning")
        sizePolicy1.setHeightForWidth(self.QLearning.sizePolicy().hasHeightForWidth())
        self.QLearning.setSizePolicy(sizePolicy1)
        self.QLearning.setMinimumSize(QSize(200, 75))
        self.QLearning.setFont(font)
        self.QLearning.setStyleSheet(u"background-color: rgba(125, 125, 125, 155);")

        self.horizontalLayout.addWidget(self.QLearning)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SlagalicaFrame = QFrame(self.frame)
        self.SlagalicaFrame.setObjectName(u"SlagalicaFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SlagalicaFrame.sizePolicy().hasHeightForWidth())
        self.SlagalicaFrame.setSizePolicy(sizePolicy2)
        self.SlagalicaFrame.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.SlagalicaFrame.setFrameShape(QFrame.StyledPanel)
        self.SlagalicaFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.SlagalicaFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.SlagalicaContainer = QFrame(self.SlagalicaFrame)
        self.SlagalicaContainer.setObjectName(u"SlagalicaContainer")
        self.SlagalicaContainer.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.SlagalicaContainer.setFrameShape(QFrame.StyledPanel)
        self.SlagalicaContainer.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.SlagalicaContainer, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.SlagalicaFrame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.SaProtivnikomVrednost = QLabel(self.frame_5)
        self.SaProtivnikomVrednost.setObjectName(u"SaProtivnikomVrednost")
        self.SaProtivnikomVrednost.setFont(font)

        self.gridLayout_9.addWidget(self.SaProtivnikomVrednost, 0, 2, 1, 1)

        self.NapraviSlagalicuButton = QPushButton(self.frame_5)
        self.NapraviSlagalicuButton.setObjectName(u"NapraviSlagalicuButton")
        sizePolicy1.setHeightForWidth(self.NapraviSlagalicuButton.sizePolicy().hasHeightForWidth())
        self.NapraviSlagalicuButton.setSizePolicy(sizePolicy1)
        self.NapraviSlagalicuButton.setMinimumSize(QSize(200, 50))
        self.NapraviSlagalicuButton.setMaximumSize(QSize(200, 50))
        self.NapraviSlagalicuButton.setFont(font)
        self.NapraviSlagalicuButton.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_9.addWidget(self.NapraviSlagalicuButton, 0, 0, 1, 1)

        self.Obavestenje = QLabel(self.frame_5)
        self.Obavestenje.setObjectName(u"Obavestenje")
        self.Obavestenje.setFont(font)
        self.Obavestenje.setLayoutDirection(Qt.LeftToRight)
        self.Obavestenje.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_9.addWidget(self.Obavestenje, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_5, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.SlagalicaFrame)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.PretragaBezPage = QWidget()
        self.PretragaBezPage.setObjectName(u"PretragaBezPage")
        self.gridLayout = QGridLayout(self.PretragaBezPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.PretragaBezFrame = QFrame(self.PretragaBezPage)
        self.PretragaBezFrame.setObjectName(u"PretragaBezFrame")
        self.PretragaBezFrame.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.PretragaBezFrame.setFrameShape(QFrame.StyledPanel)
        self.PretragaBezFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.PretragaBezFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.PretragaBezFrame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.VelicinaBezPicker = QComboBox(self.PretragaBezFrame)
        self.VelicinaBezPicker.addItem("")
        self.VelicinaBezPicker.addItem("")
        self.VelicinaBezPicker.setObjectName(u"VelicinaBezPicker")
        sizePolicy1.setHeightForWidth(self.VelicinaBezPicker.sizePolicy().hasHeightForWidth())
        self.VelicinaBezPicker.setSizePolicy(sizePolicy1)
        self.VelicinaBezPicker.setMinimumSize(QSize(150, 30))
        self.VelicinaBezPicker.setMaximumSize(QSize(150, 30))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.VelicinaBezPicker.setFont(font1)
        self.VelicinaBezPicker.setLayoutDirection(Qt.LeftToRight)
        self.VelicinaBezPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.VelicinaBezPicker, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.PretragaBezFrame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.ResiBezButton = QPushButton(self.frame_3)
        self.ResiBezButton.setObjectName(u"ResiBezButton")
        sizePolicy1.setHeightForWidth(self.ResiBezButton.sizePolicy().hasHeightForWidth())
        self.ResiBezButton.setSizePolicy(sizePolicy1)
        self.ResiBezButton.setMinimumSize(QSize(150, 50))
        self.ResiBezButton.setMaximumSize(QSize(150, 50))
        self.ResiBezButton.setFont(font)
        self.ResiBezButton.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_5.addWidget(self.ResiBezButton, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.PretragaBezFrame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PretragaBezPage)
        self.PreatragaSaPage = QWidget()
        self.PreatragaSaPage.setObjectName(u"PreatragaSaPage")
        self.gridLayout_2 = QGridLayout(self.PreatragaSaPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PretragaSaFrame = QFrame(self.PreatragaSaPage)
        self.PretragaSaFrame.setObjectName(u"PretragaSaFrame")
        self.PretragaSaFrame.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.PretragaSaFrame.setFrameShape(QFrame.StyledPanel)
        self.PretragaSaFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.PretragaSaFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_3 = QLabel(self.PretragaSaFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_7.addWidget(self.label_3, 1, 0, 1, 1)

        self.IterNumSaPicker = QSpinBox(self.PretragaSaFrame)
        self.IterNumSaPicker.setObjectName(u"IterNumSaPicker")
        sizePolicy1.setHeightForWidth(self.IterNumSaPicker.sizePolicy().hasHeightForWidth())
        self.IterNumSaPicker.setSizePolicy(sizePolicy1)
        self.IterNumSaPicker.setMinimumSize(QSize(50, 30))
        self.IterNumSaPicker.setMaximumSize(QSize(50, 30))
        self.IterNumSaPicker.setFont(font1)
        self.IterNumSaPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.IterNumSaPicker.setMinimum(1)
        self.IterNumSaPicker.setMaximum(10000000)

        self.gridLayout_7.addWidget(self.IterNumSaPicker, 1, 1, 1, 1)

        self.AgentPicker = QComboBox(self.PretragaSaFrame)
        self.AgentPicker.addItem("")
        self.AgentPicker.addItem("")
        self.AgentPicker.setObjectName(u"AgentPicker")
        sizePolicy1.setHeightForWidth(self.AgentPicker.sizePolicy().hasHeightForWidth())
        self.AgentPicker.setSizePolicy(sizePolicy1)
        self.AgentPicker.setMinimumSize(QSize(150, 30))
        self.AgentPicker.setMaximumSize(QSize(150, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.AgentPicker.setFont(font2)
        self.AgentPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.AgentPicker, 3, 1, 1, 1)

        self.frame_4 = QFrame(self.PretragaSaFrame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.ResiSaButton = QPushButton(self.frame_4)
        self.ResiSaButton.setObjectName(u"ResiSaButton")
        sizePolicy1.setHeightForWidth(self.ResiSaButton.sizePolicy().hasHeightForWidth())
        self.ResiSaButton.setSizePolicy(sizePolicy1)
        self.ResiSaButton.setMinimumSize(QSize(150, 50))
        self.ResiSaButton.setMaximumSize(QSize(150, 50))
        self.ResiSaButton.setFont(font)
        self.ResiSaButton.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_8.addWidget(self.ResiSaButton, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_4, 5, 0, 1, 2)

        self.VelicinaSaPicker = QComboBox(self.PretragaSaFrame)
        self.VelicinaSaPicker.addItem("")
        self.VelicinaSaPicker.addItem("")
        self.VelicinaSaPicker.setObjectName(u"VelicinaSaPicker")
        sizePolicy1.setHeightForWidth(self.VelicinaSaPicker.sizePolicy().hasHeightForWidth())
        self.VelicinaSaPicker.setSizePolicy(sizePolicy1)
        self.VelicinaSaPicker.setMinimumSize(QSize(150, 30))
        self.VelicinaSaPicker.setMaximumSize(QSize(150, 30))
        self.VelicinaSaPicker.setFont(font2)
        self.VelicinaSaPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.VelicinaSaPicker, 0, 1, 1, 1)

        self.label_4 = QLabel(self.PretragaSaFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_7.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_2 = QLabel(self.PretragaSaFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font)

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_6 = QLabel(self.PretragaSaFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_7.addWidget(self.label_6, 2, 0, 1, 1)

        self.DepthPicker = QSpinBox(self.PretragaSaFrame)
        self.DepthPicker.setObjectName(u"DepthPicker")
        sizePolicy1.setHeightForWidth(self.DepthPicker.sizePolicy().hasHeightForWidth())
        self.DepthPicker.setSizePolicy(sizePolicy1)
        self.DepthPicker.setMinimumSize(QSize(50, 30))
        self.DepthPicker.setMaximumSize(QSize(50, 30))
        self.DepthPicker.setFont(font1)
        self.DepthPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.DepthPicker.setMinimum(1)

        self.gridLayout_7.addWidget(self.DepthPicker, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.PretragaSaFrame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.PreatragaSaPage)
        self.QLearningPage = QWidget()
        self.QLearningPage.setObjectName(u"QLearningPage")
        self.gridLayout_3 = QGridLayout(self.QLearningPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.QLearningFrame = QFrame(self.QLearningPage)
        self.QLearningFrame.setObjectName(u"QLearningFrame")
        self.QLearningFrame.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.QLearningFrame.setFrameShape(QFrame.StyledPanel)
        self.QLearningFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.QLearningFrame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setVerticalSpacing(0)
        self.label_5 = QLabel(self.QLearningFrame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font)

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1)

        self.IterNumQLPicker = QSpinBox(self.QLearningFrame)
        self.IterNumQLPicker.setObjectName(u"IterNumQLPicker")
        sizePolicy1.setHeightForWidth(self.IterNumQLPicker.sizePolicy().hasHeightForWidth())
        self.IterNumQLPicker.setSizePolicy(sizePolicy1)
        self.IterNumQLPicker.setMinimumSize(QSize(125, 30))
        self.IterNumQLPicker.setMaximumSize(QSize(125, 30))
        self.IterNumQLPicker.setFont(font2)
        self.IterNumQLPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.IterNumQLPicker.setMinimum(1)
        self.IterNumQLPicker.setMaximum(10000000)

        self.gridLayout_11.addWidget(self.IterNumQLPicker, 0, 1, 1, 1)

        self.frame_6 = QFrame(self.QLearningFrame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.ResiQLButton = QPushButton(self.frame_6)
        self.ResiQLButton.setObjectName(u"ResiQLButton")
        sizePolicy1.setHeightForWidth(self.ResiQLButton.sizePolicy().hasHeightForWidth())
        self.ResiQLButton.setSizePolicy(sizePolicy1)
        self.ResiQLButton.setMinimumSize(QSize(150, 50))
        self.ResiQLButton.setMaximumSize(QSize(150, 50))
        self.ResiQLButton.setFont(font)
        self.ResiQLButton.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_12.addWidget(self.ResiQLButton, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_6, 1, 0, 1, 2)


        self.gridLayout_3.addWidget(self.QLearningFrame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.QLearningPage)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Slagalica", None))
        self.PretragaBezProtivnika.setText(QCoreApplication.translate("MainWindow", u"Pretraga Bez Protivnika", None))
        self.PretragaSaProtivnikom.setText(QCoreApplication.translate("MainWindow", u"Sa Protivnicima", None))
        self.QLearning.setText(QCoreApplication.translate("MainWindow", u"Q-Learning", None))
        self.SaProtivnikomVrednost.setText("")
        self.NapraviSlagalicuButton.setText(QCoreApplication.translate("MainWindow", u"Napravi Slagalicu", None))
        self.Obavestenje.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Veli\u010dina slagalice:", None))
        self.VelicinaBezPicker.setItemText(0, QCoreApplication.translate("MainWindow", u"3x3", None))
        self.VelicinaBezPicker.setItemText(1, QCoreApplication.translate("MainWindow", u"4x4", None))

        self.ResiBezButton.setText(QCoreApplication.translate("MainWindow", u"Re\u0161i", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Broj iteracija:", None))
        self.AgentPicker.setItemText(0, QCoreApplication.translate("MainWindow", u"Minimax", None))
        self.AgentPicker.setItemText(1, QCoreApplication.translate("MainWindow", u"Expectimax", None))

        self.ResiSaButton.setText(QCoreApplication.translate("MainWindow", u"Re\u0161i", None))
        self.VelicinaSaPicker.setItemText(0, QCoreApplication.translate("MainWindow", u"3x3", None))
        self.VelicinaSaPicker.setItemText(1, QCoreApplication.translate("MainWindow", u"4x4", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Agent igra\u010da:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Veli\u010dina slagalice:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dubina", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Broj iteracija:", None))
        self.ResiQLButton.setText(QCoreApplication.translate("MainWindow", u"Re\u0161i", None))


