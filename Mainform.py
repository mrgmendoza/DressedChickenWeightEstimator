# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import cv2, numpy
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(840, 668)
        MainForm.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainForm.setAnimated(False)
        MainForm.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainForm.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.uploadImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uploadImageBtn.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.uploadImageBtn.setObjectName("uploadImageBtn")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(10, 530, 141, 31))
        self.resetBtn.setObjectName("resetBtn")
        self.imagePanelGV = QtWidgets.QGraphicsView(self.centralwidget)
        self.imagePanelGV.setGeometry(QtCore.QRect(170, 20, 651, 541))
        self.imagePanelGV.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imagePanelGV.setObjectName("imagePanelGV")
        self.weightEstimateLcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.weightEstimateLcdNumber.setGeometry(QtCore.QRect(710, 570, 111, 41))
        self.weightEstimateLcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.weightEstimateLcdNumber.setLineWidth(1)
        self.weightEstimateLcdNumber.setSmallDecimalPoint(False)
        self.weightEstimateLcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.weightEstimateLcdNumber.setObjectName("weightEstimateLcdNumber")
        self.weightLbl = QtWidgets.QLabel(self.centralwidget)
        self.weightLbl.setGeometry(QtCore.QRect(600, 580, 111, 21))
        self.weightLbl.setObjectName("weightLbl")
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    ################ MY CODE  ################

        #self.uploadImageBtn.clicked.connect(self.imageFileDialog)

        self.uploadImageBtn.clicked.connect(self.imageFileDialog)

        #### end of my code


    def imageFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, temp = QtWidgets.QFileDialog.getOpenFileName(None, 'Save File', 'C:/Users/jara/PycharmProjects')
        print(fileName)

        if fileName != "":
            uploadImage = cv2.imread(fileName)
            cv2.imshow("Image", uploadImage)
            cv2.waitKey(0)

            dimensions = uploadImage.shape
            print(dimensions[0])
            print(dimensions[1])

            row = dimensions[0]
            col = dimensions[1]
            i = 0
            j = 0

            while i < row:
                while j < col:
                    #print(i)
                    #print(j)
                    blue = uploadImage[i, j, 0]
                    red = uploadImage[i, j, 1]
                    green = uploadImage[i, j, 2]
                    print(str(i)+','+str(j)+'-->R:'+str(blue)+'  G:'+str(red)+'  B:'+str(green))
                    j += 1
                i += 1
                j = 0




        #self.uploadImageBtn.setText(fname[0])



    ################ MY CODE  ################


    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Dressed Chicken Weight Estimator"))
        self.uploadImageBtn.setText(_translate("MainForm", "Upload Image"))
        self.resetBtn.setText(_translate("MainForm", "Reset"))
        self.weightLbl.setText(_translate("MainForm", "ESTIMATED WEIGHT:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())

