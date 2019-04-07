import numpy as np 
import cv2
import matplotlib.pyplot as plt
import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from PySide2.QtCore import QTranslator
import design
import os
import time


img_name = 'test.bmp'
img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)


class ExampleApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        img_name = self.loadImageButton.clicked.connect(self.loadImage)
        self.twoDimButton.clicked.connect(self.twoDimBlur)
        self.oneDimButton.clicked.connect(self.oneDimBlur)

        self.editRadius.setText("6")
        self.editSigma.setText("2")

        self.compareBrightButton.clicked.connect(self.compareBright)
        self.showHistButton.clicked.connect(self.showHist)
        self.showHistButton_2.clicked.connect(self.showHist_2)
        self.showHistButton_3.clicked.connect(self.showHist_3)

    def loadImage(self):
        self.label.setPixmap(img_name)
        # directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите папку")[0]
        # self.label.setPixmap(str(directory)) 
        # return str(directory)


    def twoDimBlur(self):
        img_out = img.copy()
        height = img.shape[0]
        width = img.shape[1]

        
        radius = int(self.editRadius.toPlainText())
        sigma = float(self.editSigma.toPlainText())
        size = int(2*radius+1)

        gauss = np.zeros((size,size))
        for i in range(size):
            for j in range(size):
                gauss[i][j] = (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-((i-radius)**2 + (j-radius)**2)/(2*sigma**2))
        # print(gauss.sum())
        # print()
        gauss = gauss / gauss.sum()
        self.tableWidget.setRowCount(size)
        self.tableWidget.setColumnCount(size)

        for i in range(len(gauss)):
            for j in range(len(gauss[i])):
                newItem = QTableWidgetItem(str(gauss[i][j]))
                self.tableWidget.setItem(i, j, newItem)

        start_time = time.process_time()
        for i in np.arange(radius, height-radius):
            for j in np.arange(radius, width-radius):        
                sum = 0.0
                for k in np.arange(-radius, radius+1):
                    for l in np.arange(-radius, radius+1):
                        a = img.item(i+k, j+l)
                        p = gauss[radius+k, radius+l]
                        sum = sum + (p * a)
                b = sum
                img_out.itemset((i,j), b)
        end_time = time.process_time()
        self.timeTwoDim.setText("Time: " + str(end_time - start_time))
        newName = 'twoDimImgOut.bmp'
        cv2.imwrite(newName, img_out)
        self.labelTwo.setPixmap(newName)
        plt.imshow(gauss, cmap=plt.get_cmap('jet'), interpolation='nearest')
        plt.colorbar()
        plt.show()
        

    def oneDimBlur(self):
        img_temp = img.copy()
        img_out = img.copy()
        height = img.shape[0]
        width = img.shape[1]
        
        
        radius = int(self.editRadius.toPlainText())
        sigma = float(self.editSigma.toPlainText())
        size = int(2*radius+1)
        gauss2D = np.zeros((size,size))
        for i in range(size):
            for j in range(size):
                gauss2D[i][j] = (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-((i-radius)**2 + (j-radius)**2)/(2*sigma**2))
        # print(gauss2D.sum())
        # print()
        gauss2D = gauss2D / gauss2D.sum()

        gauss = np.zeros((1,size))
        for j in range(size):
            gauss[0][j] = gauss2D[:][j].sum()
            # print(gauss[0][j])
        # print(gauss.sum())
        gauss = gauss / gauss.sum()

        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(size)       

        for i in range(len(gauss)):
            for j in range(len(gauss[i])):
                newItem = QTableWidgetItem(str(gauss[i][j]))
                self.tableWidget_2.setItem(i, j, newItem) 
        gauss_trans = np.zeros((size,1))
        for i in range(size):
            gauss_trans[i][0] = gauss2D[i][:].sum()
        #     print(gauss_trans[i][0])
        # print(gauss_trans.sum())
        gauss_trans = gauss_trans / gauss_trans.sum()
        gauss_ish = gauss*gauss_trans #/ (gauss*gauss_trans).sum()
        # for i in np.arange(size):
        #     for j in np.arange(size):
        #         print(gauss_ish[i][j] - gauss2D[i][j], end=" ")
        #     print()


        start_time = time.process_time()
        for i in np.arange(height):
            for j in np.arange(radius, width-radius):
                sum = 0.0
                for l in np.arange(-radius, radius+1):
                    a = img.item(i, j+l)
                    p = gauss[0, radius+l]
                    sum = sum + (p * a)
                b = sum
                img_temp.itemset((i,j), b)
        for i in np.arange(radius, height-radius):
            for j in np.arange(width):
                sum = 0.0
                for k in np.arange(-radius, radius+1):
                    a = img_temp.item(i+k, j)
                    p = gauss_trans[radius+k, 0]
                    sum = sum + (p * a)

                b = sum
                img_out.itemset((i,j), b)

        end_time = time.process_time()
        self.timeOneDim.setText("Time: " + str(end_time - start_time))
        newName = 'oneDimImgOut.bmp'
        cv2.imwrite(newName, img_out)
        self.labelOne.setPixmap(newName)
        plt.imshow(gauss, cmap=plt.get_cmap('jet'), interpolation='nearest')
        plt.colorbar()
        plt.show()

    def compareBright(self):
        x = int(self.editX.toPlainText())
        y = int(self.editY.toPlainText())
        img_1d = cv2.imread('oneDimImgOut.bmp', cv2.IMREAD_GRAYSCALE)
        img_2d = cv2.imread('twoDimImgOut.bmp',cv2.IMREAD_GRAYSCALE)
        first_img = img.item(x,y)
        oneDim_img = img_1d.item(x,y)
        twoDim_img = img_2d.item(x,y)
        # test
        height = img_1d.shape[0]
        width = img_1d.shape[1]
        # for x in np.arange(height):
        #     for y in np.arange(width):
        #         print(img_1d.item(x, y)-img_2d.item(x,y), end=" ")
        #     print()
        img.itemset((x,y), 0)
        self.browseBright.setText(str(first_img)+" "+str(oneDim_img)+" "+str(twoDim_img))

    def showHist(self):
        plt.hist(img.ravel(),256,[0,256]); 
        plt.savefig("hist.png")
        plt.show()
    def showHist_2(self):
        img_1d = cv2.imread('oneDimImgOut.bmp', cv2.IMREAD_GRAYSCALE)
        plt.hist(img_1d.ravel(),256,[0,256]); 
        plt.savefig("hist.png")
        plt.show()
    def showHist_3(self):
        img_2d = cv2.imread('twoDimImgOut.bmp',cv2.IMREAD_GRAYSCALE)
        plt.hist(img_2d.ravel(),256,[0,256]); 
        plt.savefig("hist.png")
        plt.show()


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


