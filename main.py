import numpy as np 
import cv2
import math
import matplotlib.pyplot as plt
import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from PySide2.QtCore import QTranslator
import design
import os
import time


img_name = 'cameraman.bmp'
img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)


class ExampleApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        img_name = self.loadImageButton.clicked.connect(self.loadImage)
        self.twoDimButton.clicked.connect(self.twoDimBlur)
        self.oneDimButton.clicked.connect(self.oneDimBlur)

        self.editSize.setText("5")
        self.editRadius.setText("1")
        self.editSigma.setText("0.0000001")

    def loadImage(self):
        self.label.setPixmap(img_name)
        # directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите папку")[0]
        # self.label.setPixmap(str(directory)) 
        # return str(directory)


    def twoDimBlur(self):
        img_out = img.copy()
        height = img.shape[0]
        width = img.shape[1]

        size = int(self.editSize.toPlainText())
        radius = float(self.editRadius.toPlainText())
        sigma = float(self.editSigma.toPlainText())

        gauss = np.zeros((size,size))
        for i in range(size):
            for j in range(size):
                gauss[i][j] = (1/math.sqrt(2*math.pi*sigma))*math.exp(-((i-radius-1)**2 + (j-radius-1)**2)/2*sigma**2)
        gauss = gauss / gauss.sum()
        self.tableWidget.setRowCount(size)
        self.tableWidget.setColumnCount(size)

        for i in range(len(gauss)):
            for j in range(len(gauss[i])):
                newItem = QTableWidgetItem(str(gauss[i][j]))
                self.tableWidget.setItem(i, j, newItem)

        start_time = time.process_time()
        for i in np.arange(2, height-2):
            for j in np.arange(2, width-2):        
                sum = 0
                for k in np.arange(-2, 3):
                    for l in np.arange(-2, 3):
                        a = img.item(i+k, j+l)
                        p = gauss[2+k, 2+l]
                        sum = sum + (p * a)
                b = sum
                img_out.itemset((i,j), b)
        end_time = time.process_time()
        self.timeTwoDim.setText("Time: " + str(end_time - start_time))
        newName = 'sigma'+str(sigma)+'.bmp'
        cv2.imwrite(newName, img_out)
        self.labelTwo.setPixmap(newName)
        

    def oneDimBlur(self):
        img_out = img.copy()
        height = img.shape[0]
        width = img.shape[1]
        
        size = int(self.editSize.toPlainText())
        radius = float(self.editRadius.toPlainText())
        sigma = float(self.editSigma.toPlainText())
        gauss = np.zeros((1,size))
        for i in range(1):
            for j in range(size):
                gauss[i][j] = (1/math.sqrt(2*math.pi*sigma))*math.exp(-((i-radius-1)**2 + (j-radius-1)**2)/2*sigma**2)
        gauss = gauss / gauss.sum()

        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(size)       

        for i in range(len(gauss)):
            for j in range(len(gauss[i])):
                newItem = QTableWidgetItem(str(gauss[i][j]))
                self.tableWidget_2.setItem(i, j, newItem) 
                gauss_trans = np.zeros((size,1))
        for i in range(size):
            for j in range(1):
                gauss_trans[i][j] = (1/math.sqrt(2*math.pi*sigma))*math.exp(-((i-radius-1)**2 + (j-radius-1)**2)/2*sigma**2)
        gauss_trans = gauss_trans / gauss_trans.sum()


        start_time = time.process_time()
        for i in np.arange(height):
            for j in np.arange(width-5):        
                sum = 0
                for k in np.arange(1):
                    for l in np.arange(size):
                        a = img.item(i+k, j+l)
                        p = gauss[0,l]
                        sum = sum + (p * a)
                b = sum
                img_out.itemset((i,j), b)

        for i in np.arange(height-5):
            for j in np.arange(width):        
                sum = 0
                for k in np.arange(-2, 3):
                    for l in np.arange(1):
                        a = img_out.item(i+k, j+l)
                        p = gauss_trans[l,0]
                        sum = sum + (p * a)
                b = sum
                img_out.itemset((i,j), b)
        end_time = time.process_time()
        self.timeOneDim.setText("Time: " + str(end_time - start_time))
        newName = 'one_dim_sigma'+str(sigma)+'.bmp'
        cv2.imwrite(newName, img_out)
        self.labelOne.setPixmap(newName)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
# print(timeit.timeit("main()", setup="from __main__ import main", number=1))

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()








# print(sum(sum(gauss)))

# # plt.imshow(gauss, cmap=plt.get_cmap('jet'), interpolation='nearest')
# # plt.colorbar()
# # plt.show()


