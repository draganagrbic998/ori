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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        #MainWindow.setMinimumSize(QSize(1024, 720))
        #MainWindow.setMaximumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setStyleSheet(u"background-color: rgb(179, 179, 179);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PretragaBezProtivnika = QPushButton(self.frame_2)
        self.PretragaBezProtivnika.setObjectName(u"PretragaBezProtivnika")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PretragaBezProtivnika.sizePolicy().hasHeightForWidth())
        self.PretragaBezProtivnika.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.PretragaSaProtivnikom.sizePolicy().hasHeightForWidth())
        self.PretragaSaProtivnikom.setSizePolicy(sizePolicy2)
        self.PretragaSaProtivnikom.setMinimumSize(QSize(200, 75))
        self.PretragaSaProtivnikom.setFont(font)
        self.PretragaSaProtivnikom.setStyleSheet(u"background-color: rgba(125, 125, 125, 155);")

        self.horizontalLayout.addWidget(self.PretragaSaProtivnikom)

        self.QLearning = QPushButton(self.frame_2)
        self.QLearning.setObjectName(u"QLearning")
        sizePolicy2.setHeightForWidth(self.QLearning.sizePolicy().hasHeightForWidth())
        self.QLearning.setSizePolicy(sizePolicy2)
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
        sizePolicy.setHeightForWidth(self.SlagalicaFrame.sizePolicy().hasHeightForWidth())
        self.SlagalicaFrame.setSizePolicy(sizePolicy)
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

        self.gridLayout_6.addWidget(self.SlagalicaContainer, 1, 0, 1, 1)

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
        self.Obavestenje = QLabel(self.frame_5)
        self.Obavestenje.setObjectName(u"Obavestenje")
        self.Obavestenje.setFont(font)
        self.Obavestenje.setLayoutDirection(Qt.LeftToRight)
        self.Obavestenje.setAutoFillBackground(True)
        self.Obavestenje.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_9.addWidget(self.Obavestenje, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_5, 2, 0, 1, 1)


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
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.VelicinaBezPicker = QComboBox(self.PretragaBezFrame)
        self.VelicinaBezPicker.addItem("")
        self.VelicinaBezPicker.addItem("")
        self.VelicinaBezPicker.setObjectName(u"VelicinaBezPicker")
        sizePolicy2.setHeightForWidth(self.VelicinaBezPicker.sizePolicy().hasHeightForWidth())
        self.VelicinaBezPicker.setSizePolicy(sizePolicy2)
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

        self.ResiBezButton = QPushButton(self.PretragaBezFrame)
        self.ResiBezButton.setObjectName(u"ResiBezButton")
        sizePolicy2.setHeightForWidth(self.ResiBezButton.sizePolicy().hasHeightForWidth())
        self.ResiBezButton.setSizePolicy(sizePolicy2)
        self.ResiBezButton.setMinimumSize(QSize(150, 50))
        self.ResiBezButton.setMaximumSize(QSize(150, 50))
        self.ResiBezButton.setFont(font)
        self.ResiBezButton.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_4.addWidget(self.ResiBezButton, 1, 0, 1, 1)

        self.ResetPuzzle1 = QPushButton(self.PretragaBezFrame)
        self.ResetPuzzle1.setObjectName(u"ResetPuzzle1")
        sizePolicy2.setHeightForWidth(self.ResetPuzzle1.sizePolicy().hasHeightForWidth())
        self.ResetPuzzle1.setSizePolicy(sizePolicy2)
        self.ResetPuzzle1.setMinimumSize(QSize(150, 50))
        self.ResetPuzzle1.setMaximumSize(QSize(150, 50))
        self.ResetPuzzle1.setFont(font)
        self.ResetPuzzle1.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_4.addWidget(self.ResetPuzzle1, 1, 1, 1, 1)


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
        self.AgentPicker = QComboBox(self.PretragaSaFrame)
        self.AgentPicker.addItem("")
        self.AgentPicker.addItem("")
        self.AgentPicker.setObjectName(u"AgentPicker")
        sizePolicy2.setHeightForWidth(self.AgentPicker.sizePolicy().hasHeightForWidth())
        self.AgentPicker.setSizePolicy(sizePolicy2)
        self.AgentPicker.setMinimumSize(QSize(150, 30))
        self.AgentPicker.setMaximumSize(QSize(150, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.AgentPicker.setFont(font2)
        self.AgentPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.AgentPicker, 2, 1, 1, 1)

        self.label_3 = QLabel(self.PretragaSaFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)

        self.IterNumSaPicker = QSpinBox(self.PretragaSaFrame)
        self.IterNumSaPicker.setObjectName(u"IterNumSaPicker")
        sizePolicy2.setHeightForWidth(self.IterNumSaPicker.sizePolicy().hasHeightForWidth())
        self.IterNumSaPicker.setSizePolicy(sizePolicy2)
        self.IterNumSaPicker.setMinimumSize(QSize(100, 30))
        self.IterNumSaPicker.setMaximumSize(QSize(100, 30))
        self.IterNumSaPicker.setFont(font1)
        self.IterNumSaPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.IterNumSaPicker.setMinimum(10)
        self.IterNumSaPicker.setMaximum(1000)
        self.IterNumSaPicker.setValue(20)

        self.gridLayout_7.addWidget(self.IterNumSaPicker, 0, 1, 1, 1)

        self.label_6 = QLabel(self.PretragaSaFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_7.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_4 = QLabel(self.PretragaSaFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_7.addWidget(self.label_4, 2, 0, 1, 1)

        self.DepthPicker = QSpinBox(self.PretragaSaFrame)
        self.DepthPicker.setObjectName(u"DepthPicker")
        sizePolicy2.setHeightForWidth(self.DepthPicker.sizePolicy().hasHeightForWidth())
        self.DepthPicker.setSizePolicy(sizePolicy2)
        self.DepthPicker.setMinimumSize(QSize(100, 30))
        self.DepthPicker.setMaximumSize(QSize(100, 30))
        self.DepthPicker.setFont(font1)
        self.DepthPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.DepthPicker.setMinimum(1)
        self.DepthPicker.setMaximum(5)
        self.DepthPicker.setValue(3)

        self.gridLayout_7.addWidget(self.DepthPicker, 1, 1, 1, 1)

        self.ResetPuzzle2 = QPushButton(self.PretragaSaFrame)
        self.ResetPuzzle2.setObjectName(u"ResetPuzzle2")
        sizePolicy2.setHeightForWidth(self.ResetPuzzle2.sizePolicy().hasHeightForWidth())
        self.ResetPuzzle2.setSizePolicy(sizePolicy2)
        self.ResetPuzzle2.setMinimumSize(QSize(150, 50))
        self.ResetPuzzle2.setMaximumSize(QSize(150, 50))
        self.ResetPuzzle2.setFont(font)
        self.ResetPuzzle2.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_7.addWidget(self.ResetPuzzle2, 3, 1, 1, 1)

        self.ResiSaButton = QPushButton(self.PretragaSaFrame)
        self.ResiSaButton.setObjectName(u"ResiSaButton")
        sizePolicy2.setHeightForWidth(self.ResiSaButton.sizePolicy().hasHeightForWidth())
        self.ResiSaButton.setSizePolicy(sizePolicy2)
        self.ResiSaButton.setMinimumSize(QSize(150, 50))
        self.ResiSaButton.setMaximumSize(QSize(150, 50))
        self.ResiSaButton.setFont(font)
        self.ResiSaButton.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_7.addWidget(self.ResiSaButton, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.PretragaSaFrame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.PreatragaSaPage)
        self.QLearningPage = QWidget()
        self.QLearningPage.setObjectName(u"QLearningPage")
        self.gridLayout_3 = QGridLayout(self.QLearningPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.QLearningFrame = QFrame(self.QLearningPage)
        self.QLearningFrame.setObjectName(u"QLearningFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.QLearningFrame.sizePolicy().hasHeightForWidth())
        self.QLearningFrame.setSizePolicy(sizePolicy4)
        self.QLearningFrame.setFont(font)
        self.QLearningFrame.setAutoFillBackground(False)
        self.QLearningFrame.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.QLearningFrame.setFrameShape(QFrame.StyledPanel)
        self.QLearningFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.QLearningFrame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setVerticalSpacing(0)
        self.alpha = QDoubleSpinBox(self.QLearningFrame)
        self.alpha.setObjectName(u"alpha")
        sizePolicy2.setHeightForWidth(self.alpha.sizePolicy().hasHeightForWidth())
        self.alpha.setSizePolicy(sizePolicy2)
        self.alpha.setMinimumSize(QSize(100, 30))
        self.alpha.setMaximumSize(QSize(100, 30))
        self.alpha.setFont(font2)
        self.alpha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.alpha.setMinimum(0.100000000000000)
        self.alpha.setMaximum(0.900000000000000)
        self.alpha.setValue(0.200000000000000)

        self.gridLayout_11.addWidget(self.alpha, 1, 3, 1, 1)

        self.label_8 = QLabel(self.QLearningFrame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font)

        self.gridLayout_11.addWidget(self.label_8, 2, 0, 1, 1)

        self.discount = QDoubleSpinBox(self.QLearningFrame)
        self.discount.setObjectName(u"discount")
        sizePolicy2.setHeightForWidth(self.discount.sizePolicy().hasHeightForWidth())
        self.discount.setSizePolicy(sizePolicy2)
        self.discount.setMinimumSize(QSize(100, 30))
        self.discount.setMaximumSize(QSize(100, 30))
        self.discount.setFont(font2)
        self.discount.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.discount.setMinimum(0.100000000000000)
        self.discount.setMaximum(1.000000000000000)
        self.discount.setValue(0.800000000000000)

        self.gridLayout_11.addWidget(self.discount, 2, 3, 1, 1)

        self.label_7 = QLabel(self.QLearningFrame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font)

        self.gridLayout_11.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_5 = QLabel(self.QLearningFrame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font)

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1)

        self.IterNumQPicker = QSpinBox(self.QLearningFrame)
        self.IterNumQPicker.setObjectName(u"IterNumQPicker")
        sizePolicy2.setHeightForWidth(self.IterNumQPicker.sizePolicy().hasHeightForWidth())
        self.IterNumQPicker.setSizePolicy(sizePolicy2)
        self.IterNumQPicker.setMinimumSize(QSize(100, 30))
        self.IterNumQPicker.setMaximumSize(QSize(100, 30))
        self.IterNumQPicker.setFont(font2)
        self.IterNumQPicker.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.IterNumQPicker.setMinimum(1)
        self.IterNumQPicker.setMaximum(5)
        self.IterNumQPicker.setSingleStep(1)
        self.IterNumQPicker.setValue(3)

        self.gridLayout_11.addWidget(self.IterNumQPicker, 0, 3, 1, 1)

        self.ResetPuzzle3 = QPushButton(self.QLearningFrame)
        self.ResetPuzzle3.setObjectName(u"ResetPuzzle3")
        sizePolicy2.setHeightForWidth(self.ResetPuzzle3.sizePolicy().hasHeightForWidth())
        self.ResetPuzzle3.setSizePolicy(sizePolicy2)
        self.ResetPuzzle3.setMinimumSize(QSize(150, 50))
        self.ResetPuzzle3.setMaximumSize(QSize(150, 50))
        self.ResetPuzzle3.setFont(font)
        self.ResetPuzzle3.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_11.addWidget(self.ResetPuzzle3, 6, 3, 1, 1)

        self.ResiQLButton = QPushButton(self.QLearningFrame)
        self.ResiQLButton.setObjectName(u"ResiQLButton")
        sizePolicy2.setHeightForWidth(self.ResiQLButton.sizePolicy().hasHeightForWidth())
        self.ResiQLButton.setSizePolicy(sizePolicy2)
        self.ResiQLButton.setMinimumSize(QSize(150, 50))
        self.ResiQLButton.setMaximumSize(QSize(150, 50))
        self.ResiQLButton.setFont(font)
        self.ResiQLButton.setStyleSheet(u"background-color: rgb(212, 212, 212);")

        self.gridLayout_11.addWidget(self.ResiQLButton, 6, 0, 1, 1)


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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Slagalica", None))
        self.PretragaBezProtivnika.setText(QCoreApplication.translate("MainWindow", u"A* Search", None))
        self.PretragaSaProtivnikom.setText(QCoreApplication.translate("MainWindow", u"Expectimax", None))
        self.QLearning.setText(QCoreApplication.translate("MainWindow", u"Q-Learning", None))
        self.Obavestenje.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Puzzle size:", None))
        self.VelicinaBezPicker.setItemText(0, QCoreApplication.translate("MainWindow", u"3x3", None))
        self.VelicinaBezPicker.setItemText(1, QCoreApplication.translate("MainWindow", u"4x4", None))

        self.ResiBezButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.ResetPuzzle1.setText(QCoreApplication.translate("MainWindow", u"Reset puzzle", None))
        self.AgentPicker.setItemText(0, QCoreApplication.translate("MainWindow", u"Expectimax", None))
        self.AgentPicker.setItemText(1, QCoreApplication.translate("MainWindow", u"Minimax", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Iteration number:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Depth:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Agent:", None))
        self.ResetPuzzle2.setText(QCoreApplication.translate("MainWindow", u"Reset puzzle", None))
        self.ResiSaButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Discount:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Alpha: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Iteration number:", None))
        self.ResetPuzzle3.setText(QCoreApplication.translate("MainWindow", u"Reset puzzle", None))
        self.ResiQLButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

