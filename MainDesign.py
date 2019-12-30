# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/git-push-automater/MainDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 245)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.directoryEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.directoryEntry.setGeometry(QtCore.QRect(10, 10, 551, 21))
        self.directoryEntry.setObjectName("directoryEntry")
        self.searchDirecory = QtWidgets.QToolButton(self.centralwidget)
        self.searchDirecory.setGeometry(QtCore.QRect(570, 10, 25, 19))
        self.searchDirecory.setObjectName("searchDirecory")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 581, 141))
        self.groupBox.setObjectName("groupBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 561, 111))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.commitAndPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.commitAndPushButton.setGeometry(QtCore.QRect(484, 200, 101, 23))
        self.commitAndPushButton.setObjectName("commitAndPushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.directoryEntry.setPlaceholderText(_translate("MainWindow", "   DIR"))
        self.searchDirecory.setText(_translate("MainWindow", "..."))
        self.groupBox.setTitle(_translate("MainWindow", "Commit Message : "))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Commit."))
        self.commitAndPushButton.setText(_translate("MainWindow", "Commit and Push"))
