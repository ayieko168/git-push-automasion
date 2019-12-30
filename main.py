from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from MainDesign import *
from cridentialsDialog import *
import os, threading
# import requests

class LoggingWidget(QWidget):

    def __init__(self):

        super().__init__()
        self.logUi = Ui_Form()
        self.logUi.setupUi(self)
    
    def run(self):

        self.show()
        # self.exec_()
    
    def update(self, text):

        pass

    



class CridentialsApp(QDialog):

    def __init__(self):

        super().__init__()
        self.crUi = Ui_Dialog()
        self.crUi.setupUi(self)
        

        self.crUi.showButton.clicked.connect(self.showPass)
        self.crUi.doneButton.clicked.connect(self.doneCMD)

    def showPass(self):

        print("show pass")
        self.crUi.passwordEntry.setEchoMode(QtGui.QLineEdit.Normal)

        print(self.crUi.passwordEntry.echoMode())

    def getCridentials(self):

        credentials = []

        u = self.crUi.userNameEntry.text()
        p = self.crUi.passwordEntry.text()
        credentials.append(u)
        credentials.append(p)

        return credentials
    
    def run(self):

        self.show()
        self.exec_()

    def doneCMD(self):

        self.getCridentials()
        self.close()


class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.searchDirecory.clicked.connect(self.searchDirectoryCMD)
        self.ui.commitAndPushButton.clicked.connect(self.commitAndPushButtonCMD)


    def searchDirectoryCMD(self):

        foundDirPath = QFileDialog.getExistingDirectory()
        dircetoryName = foundDirPath.split("\\")[-1].title().replace(" ", "-")

        # AUTO FILL FIELDS
        self.ui.directoryEntry.setText(foundDirPath)


    def commitAndPushButtonCMD(self):

        # Get the credentials for github login...
        print("getting credentials...")
        # crid = CridentialsApp()
        # crid.run()
        # u, p = crid.getCridentials()

        # get repoDetails ie name, commit massage etc
        print("getting repo Deatails...")
        commitMess = self.ui.plainTextEdit.toPlainText()
        repoPath = self.ui.directoryEntry.text()
        print("repoPath = ", repoPath)

        # Commit and push all the repo files
        # command1 = "cd \"{}\" && git config --global user.name "your username""
        command = "cd \"{}\" && git add -A && git commit -m \"{}\" && git push".format(repoPath, commitMess)
        
        os.system(command)
        
        
        print("")
        print("done.")




if __name__ == "__main__":
    
    w = QApplication([])
    app = App()
    app.show()
    w.exec_()
















