# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainapp2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import assets_rc

class Ui_main2(object):
    def setupUi(self, main2):
        if not main2.objectName():
            main2.setObjectName(u"main2")
        main2.resize(680, 400)
        self.centralwidget = QWidget(main2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: rgba(255, 255, 255, .15);\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-10, -10, 91, 61))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(460, 0, 201, 41))
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.emailbox = QLineEdit(self.dropShadowFrame)
        self.emailbox.setObjectName(u"emailbox")
        self.emailbox.setGeometry(QRect(230, 150, 171, 20))
        self.changelog = QLabel(self.dropShadowFrame)
        self.changelog.setObjectName(u"changelog")
        self.changelog.setGeometry(QRect(10, 50, 221, 201))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(20)
        self.changelog.setFont(font1)
        self.changelog.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.changelog.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.changelog_2 = QLabel(self.dropShadowFrame)
        self.changelog_2.setObjectName(u"changelog_2")
        self.changelog_2.setGeometry(QRect(10, 260, 221, 81))
        self.changelog_2.setFont(font1)
        self.changelog_2.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.changelog_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.github = QPushButton(self.dropShadowFrame)
        self.github.setObjectName(u"github")
        self.github.setGeometry(QRect(10, 350, 75, 23))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        self.github.setFont(font2)
        self.github.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.label_credits_2 = QLabel(self.dropShadowFrame)
        self.label_credits_2.setObjectName(u"label_credits_2")
        self.label_credits_2.setGeometry(QRect(230, 120, 111, 21))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        self.label_credits_2.setFont(font3)
        self.label_credits_2.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_credits_3 = QLabel(self.dropShadowFrame)
        self.label_credits_3.setObjectName(u"label_credits_3")
        self.label_credits_3.setGeometry(QRect(230, 10, 141, 21))
        self.label_credits_3.setFont(font3)
        self.label_credits_3.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.registerButton = QPushButton(self.dropShadowFrame)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(230, 240, 75, 23))
        self.registerButton.setFont(font2)
        self.registerButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.changelog_3 = QLabel(self.dropShadowFrame)
        self.changelog_3.setObjectName(u"changelog_3")
        self.changelog_3.setGeometry(QRect(410, 50, 241, 231))
        self.changelog_3.setFont(font1)
        self.changelog_3.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.changelog_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.loginButton = QPushButton(self.dropShadowFrame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(410, 300, 75, 23))
        self.loginButton.setFont(font2)
        self.loginButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.exitButton = QPushButton(self.dropShadowFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(500, 300, 75, 23))
        self.exitButton.setFont(font2)
        self.exitButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.response = QLabel(self.dropShadowFrame)
        self.response.setObjectName(u"response")
        self.response.setGeometry(QRect(230, 190, 171, 41))
        self.response.setFont(font3)
        self.response.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.response.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        main2.setCentralWidget(self.centralwidget)

        self.retranslateUi(main2)

        QMetaObject.connectSlotsByName(main2)
    # setupUi

    def retranslateUi(self, main2):
        main2.setWindowTitle(QCoreApplication.translate("main2", u"SoarGuide", None))
        self.label_title.setText(QCoreApplication.translate("main2", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Tsar</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("main2", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Created</span><span style=\" font-size:12pt;\">: enigmapr0ject</span></p></body></html>", None))
        self.changelog.setText(QCoreApplication.translate("main2", u"<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline;\">1.0:</span></p><p><span style=\" font-size:10pt;\">-Added 2 Factor Authentication<br/>-Password resets use 2FA</span></p><p><span style=\" font-size:10pt;\">-Brand new GUI<br/>-Windows native support</span></p><p><span style=\" font-size:10pt; text-decoration: underline;\">To Come:</span></p><p><span style=\" font-size:10pt;\">-UNIX support</span></p><p><span style=\" font-size:10pt;\">-Additional functionality</span></p></body></html>", None))
        self.changelog_2.setText(QCoreApplication.translate("main2", u"<html><head/><body><p><span style=\" font-size:10pt;\">To keep up to date with</span></p><p><span style=\" font-size:10pt;\">all latest news and features,</span></p><p><span style=\" font-size:10pt;\">head to our GitHub!</span></p></body></html>", None))
        self.github.setText(QCoreApplication.translate("main2", u"GitHub", None))
        self.label_credits_2.setText(QCoreApplication.translate("main2", u"<html><head/><body><p>Email</p></body></html>", None))
        self.label_credits_3.setText(QCoreApplication.translate("main2", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Register</span></p></body></html>", None))
        self.registerButton.setText(QCoreApplication.translate("main2", u"Register", None))
        self.changelog_3.setText(QCoreApplication.translate("main2", u"<html><head/><body><p><img src=\":/icon/iconfile.ico\"/></p></body></html>", None))
        self.loginButton.setText(QCoreApplication.translate("main2", u"Log In", None))
        self.exitButton.setText(QCoreApplication.translate("main2", u"Exit", None))
        self.response.setText(QCoreApplication.translate("main2", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

