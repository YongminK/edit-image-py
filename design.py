# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui',
# licensing of 'form.ui' applies.
#
# Created: Wed Mar 27 03:01:56 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1105, 1082)
        self.loadImageButton = QtWidgets.QPushButton(Form)
        self.loadImageButton.setGeometry(QtCore.QRect(40, 300, 131, 51))
        self.loadImageButton.setObjectName("loadImageButton")
        self.oneDimButton = QtWidgets.QPushButton(Form)
        self.oneDimButton.setGeometry(QtCore.QRect(380, 300, 131, 51))
        self.oneDimButton.setObjectName("oneDimButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 281, 281))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.labelTwo = QtWidgets.QLabel(Form)
        self.labelTwo.setGeometry(QtCore.QRect(730, 20, 281, 281))
        self.labelTwo.setFrameShape(QtWidgets.QFrame.Box)
        self.labelTwo.setObjectName("labelTwo")
        self.twoDimButton = QtWidgets.QPushButton(Form)
        self.twoDimButton.setGeometry(QtCore.QRect(730, 300, 131, 51))
        self.twoDimButton.setObjectName("twoDimButton")
        self.timeTwoDim = QtWidgets.QTextBrowser(Form)
        self.timeTwoDim.setGeometry(QtCore.QRect(750, 360, 256, 31))
        self.timeTwoDim.setObjectName("timeTwoDim")
        self.labelOne = QtWidgets.QLabel(Form)
        self.labelOne.setGeometry(QtCore.QRect(380, 20, 291, 281))
        self.labelOne.setFrameShape(QtWidgets.QFrame.Box)
        self.labelOne.setObjectName("labelOne")
        self.timeOneDim = QtWidgets.QTextBrowser(Form)
        self.timeOneDim.setGeometry(QtCore.QRect(410, 360, 256, 31))
        self.timeOneDim.setObjectName("timeOneDim")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(340, 510, 681, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.editSize = QtWidgets.QTextEdit(Form)
        self.editSize.setGeometry(QtCore.QRect(90, 420, 141, 31))
        self.editSize.setObjectName("editSize")
        self.editSigma = QtWidgets.QTextEdit(Form)
        self.editSigma.setGeometry(QtCore.QRect(90, 460, 141, 31))
        self.editSigma.setObjectName("editSigma")
        self.editRadius = QtWidgets.QTextEdit(Form)
        self.editRadius.setGeometry(QtCore.QRect(90, 500, 141, 31))
        self.editRadius.setObjectName("editRadius")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 420, 51, 41))
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 450, 71, 51))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 490, 61, 41))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(340, 400, 681, 101))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.editX = QtWidgets.QTextEdit(Form)
        self.editX.setGeometry(QtCore.QRect(60, 570, 51, 41))
        self.editX.setObjectName("editX")
        self.editY = QtWidgets.QTextEdit(Form)
        self.editY.setGeometry(QtCore.QRect(150, 570, 51, 41))
        self.editY.setObjectName("editY")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 580, 16, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(130, 580, 16, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 540, 111, 31))
        self.label_7.setObjectName("label_7")
        self.compareBrightButton = QtWidgets.QPushButton(Form)
        self.compareBrightButton.setGeometry(QtCore.QRect(210, 580, 93, 28))
        self.compareBrightButton.setObjectName("compareBrightButton")
        self.browseBright = QtWidgets.QTextBrowser(Form)
        self.browseBright.setGeometry(QtCore.QRect(60, 620, 256, 71))
        self.browseBright.setObjectName("browseBright")
        self.showHistButton = QtWidgets.QPushButton(Form)
        self.showHistButton.setGeometry(QtCore.QRect(170, 300, 151, 51))
        self.showHistButton.setObjectName("showHistButton")
        self.showHistButton_2 = QtWidgets.QPushButton(Form)
        self.showHistButton_2.setGeometry(QtCore.QRect(510, 300, 151, 51))
        self.showHistButton_2.setObjectName("showHistButton_2")
        self.showHistButton_3 = QtWidgets.QPushButton(Form)
        self.showHistButton_3.setGeometry(QtCore.QRect(850, 300, 151, 51))
        self.showHistButton_3.setObjectName("showHistButton_3")
        self.hist = QtWidgets.QLabel(Form)
        self.hist.setGeometry(QtCore.QRect(50, 800, 281, 281))
        self.hist.setFrameShape(QtWidgets.QFrame.Box)
        self.hist.setObjectName("hist")
        self.hist_3 = QtWidgets.QLabel(Form)
        self.hist_3.setGeometry(QtCore.QRect(740, 800, 281, 281))
        self.hist_3.setFrameShape(QtWidgets.QFrame.Box)
        self.hist_3.setObjectName("hist_3")
        self.hist_2 = QtWidgets.QLabel(Form)
        self.hist_2.setGeometry(QtCore.QRect(390, 800, 291, 281))
        self.hist_2.setFrameShape(QtWidgets.QFrame.Box)
        self.hist_2.setObjectName("hist_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.loadImageButton.setText(QtWidgets.QApplication.translate("Form", "Load", None, -1))
        self.oneDimButton.setText(QtWidgets.QApplication.translate("Form", "One", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Image 1", None, -1))
        self.labelTwo.setText(QtWidgets.QApplication.translate("Form", "Two Dim Image", None, -1))
        self.twoDimButton.setText(QtWidgets.QApplication.translate("Form", "Two", None, -1))
        self.timeTwoDim.setHtml(QtWidgets.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Time: </p></body></html>", None, -1))
        self.labelOne.setText(QtWidgets.QApplication.translate("Form", "One Dim Image", None, -1))
        self.timeOneDim.setHtml(QtWidgets.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Time: </p></body></html>", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Размер матрицы", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Отклонение (сигма)", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Радиус апертуры", None, -1))
        self.editX.setHtml(QtWidgets.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>", None, -1))
        self.editY.setHtml(QtWidgets.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Х</span></p></body></html>", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Y</span></p></body></html>", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Координаты</span></p></body></html>", None, -1))
        self.compareBrightButton.setText(QtWidgets.QApplication.translate("Form", "Сравнить", None, -1))
        self.showHistButton.setText(QtWidgets.QApplication.translate("Form", "Показать гистограмму", None, -1))
        self.showHistButton_2.setText(QtWidgets.QApplication.translate("Form", "Показать гистограмму", None, -1))
        self.showHistButton_3.setText(QtWidgets.QApplication.translate("Form", "Показать гистограмму", None, -1))
        self.hist.setText(QtWidgets.QApplication.translate("Form", "Гистограмма 1", None, -1))
        self.hist_3.setText(QtWidgets.QApplication.translate("Form", "Гистограмма 3", None, -1))
        self.hist_2.setText(QtWidgets.QApplication.translate("Form", "Гистограмма 2", None, -1))

