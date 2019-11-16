# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ayieko/Projects And  Research/PycharmProjects/git-push-automater/MainDesign.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(599, 245)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.directoryEntry = QtGui.QLineEdit(self.centralwidget)
        self.directoryEntry.setGeometry(QtCore.QRect(10, 10, 551, 21))
        self.directoryEntry.setObjectName(_fromUtf8("directoryEntry"))
        self.searchDirecory = QtGui.QToolButton(self.centralwidget)
        self.searchDirecory.setGeometry(QtCore.QRect(570, 10, 25, 19))
        self.searchDirecory.setObjectName(_fromUtf8("searchDirecory"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 581, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 561, 111))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.commitAndPushButton = QtGui.QPushButton(self.centralwidget)
        self.commitAndPushButton.setGeometry(QtCore.QRect(484, 200, 101, 23))
        self.commitAndPushButton.setObjectName(_fromUtf8("commitAndPushButton"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.directoryEntry.setPlaceholderText(_translate("MainWindow", "   DIR", None))
        self.searchDirecory.setText(_translate("MainWindow", "...", None))
        self.groupBox.setTitle(_translate("MainWindow", "Commit Message : ", None))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Commit.", None))
        self.commitAndPushButton.setText(_translate("MainWindow", "Commit and Push", None))

