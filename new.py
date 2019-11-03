import numpy as np
import cv2
import matplotlib.pyplot as plt
import pyautogui
import argparse
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit


def nothing(x):
    pass


clicks = list()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 17))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(210, 50, 171, 141))
        self.listWidget.setStyleSheet("background: rgba(211, 5, 7,0.4)")
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 171, 17))
        self.label_2.setObjectName("label_2")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(220, 230, 151, 331))
        self.listView_2.setStyleSheet("background: rgba(94,34,112,0.3)")
        self.listView_2.setObjectName("listView_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 200, 141, 17))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 230, 131, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(230, 50, 131, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_3.addWidget(self.pushButton_12)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 20, 241, 17))
        self.label_4.setObjectName("label_4")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(390, 50, 281, 471))
        self.listWidget_2.setStyleSheet("background:rgba(78,78,8,0.3)")
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(400, 440, 231, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(400, 320, 231, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 80, 161, 17))
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 190, 67, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(620, 220, 67, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(620, 150, 67, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(680, 20, 141, 17))
        self.label_13.setObjectName("label_13")
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(690, 90, 184, 401))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_5.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_5.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_5.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_5.addWidget(self.pushButton_16)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_14.setMaximumSize(QtCore.QSize(250, 20))
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.layoutWidget_3)
        self.plainTextEdit_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.plainTextEdit_5.setPlaceholderText("")
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.verticalLayout_5.addWidget(self.plainTextEdit_5)
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_5.addWidget(self.pushButton_17)
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(680, 50, 201, 471))
        self.listView_3.setStyleSheet("background:rgba(2,33,114,0.2)")
        self.listView_3.setObjectName("listView_3")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(400, 150, 213, 95))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setMaximumSize(QtCore.QSize(50, 20))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(150, 20))
        self.plainTextEdit.setBaseSize(QtCore.QSize(10, 10))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setMaximumSize(QtCore.QSize(50, 20))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(
            self.formLayoutWidget_2)
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(150, 20))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout_2.addWidget(self.plainTextEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setMaximumSize(QtCore.QSize(50, 20))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(
            self.formLayoutWidget_2)
        self.plainTextEdit_3.setMaximumSize(QtCore.QSize(150, 20))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.horizontalLayout_3.addWidget(self.plainTextEdit_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setMaximumSize(QtCore.QSize(50, 20))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(
            self.formLayoutWidget_2)
        self.plainTextEdit_4.setMaximumSize(QtCore.QSize(150, 20))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.horizontalLayout_4.addWidget(self.plainTextEdit_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.formLayout_2.setLayout(
            0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_4)
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(30, 60, 151, 441))
        self.columnView.setStyleSheet("background:rgb(233, 185, 110)")
        self.columnView.setObjectName("columnView")
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(40, 110, 131, 331))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButton_pushed)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pushButton_2pushed)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pushButton_3pushed)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_4)

        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.pushButton_4pushed)

        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.pushButton_5pushed)

        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.pushButton_9pushed)

        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.pushButton_10pushed)
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_3.raise_()
        self.columnView.raise_()
        self.listView_2.raise_()
        self.listView_3.raise_()
        self.listWidget_2.raise_()
        self.layoutWidget.raise_()
        self.label.raise_()
        self.listWidget.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.layoutWidget_2.raise_()
        self.label_4.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.label_5.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.layoutWidget_3.raise_()
        self.formLayoutWidget_2.raise_()
        self.layoutWidget_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "1. image processing"))
        self.label_2.setText(_translate("MainWindow", "2. adaptive threshold"))
        self.label_3.setText(_translate("MainWindow", "4. convolution"))
        self.pushButton_5.setText(_translate("MainWindow", "gaussian"))
        self.pushButton_6.setText(_translate("MainWindow", "sobel X"))
        self.pushButton_7.setText(_translate("MainWindow", "sobel Y"))
        self.pushButton_8.setText(_translate("MainWindow", "magnitube"))
        self.pushButton_11.setText(_translate(
            "MainWindow", "global threshold"))
        self.pushButton_12.setText(_translate("MainWindow", "local threshold"))
        self.label_4.setText(_translate(
            "MainWindow", "3. image transformation"))
        self.pushButton_9.setText(_translate(
            "MainWindow", "3.2 perspective  transformation"))
        self.pushButton_10.setText(_translate(
            "MainWindow", "3.1 roration scaling traslation"))
        self.label_5.setText(_translate("MainWindow", "parameter"))
        self.label_10.setText(_translate("MainWindow", "pixel"))
        self.label_11.setText(_translate("MainWindow", "pixel"))
        self.label_12.setText(_translate("MainWindow", "deg"))
        self.label_13.setText(_translate("MainWindow", "5. "))
        self.pushButton_13.setText(_translate(
            "MainWindow", "5.1 show train image"))
        self.pushButton_14.setText(_translate(
            "MainWindow", "5.2 show hyperparameter"))
        self.pushButton_15.setText(_translate(
            "MainWindow", "5.3 train one epoch"))
        self.pushButton_16.setText(_translate(
            "MainWindow", "5.4 show train result"))
        self.label_14.setText(_translate("MainWindow", "test image index :"))
        self.pushButton_17.setText(_translate("MainWindow", "5.5 inference"))
        self.label_6.setText(_translate("MainWindow", "angel :"))
        self.label_7.setText(_translate("MainWindow", "scale :"))
        self.label_8.setText(_translate("MainWindow", "Tx : "))
        self.label_9.setText(_translate("MainWindow", "Ty:"))
        self.pushButton.setText(_translate("MainWindow", "load image"))
        self.pushButton_2.setText(_translate("MainWindow", "color convention"))
        self.pushButton_3.setText(_translate("MainWindow", "image filpping"))
        self.pushButton_4.setText(_translate("MainWindow", "blending"))

    def pushButton_pushed(self):
        pic = cv2.imread('dog.bmp')
        cv2.imshow('dog.bmp', pic)
        print('Hight: ' + str(pic.shape[0]))
        print('Width: ' + str(pic.shape[1]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def pushButton_2pushed(self):
        image = cv2.imread("color.png")
        cv2.imshow("color.png", image)
        red = image[:, :, 0].copy()
        green = image[:, :, 1].copy()
        blue = image[:, :, 2].copy()
        image[:, :, 0] = green
        image[:, :, 1] = blue
        image[:, :, 2] = red
        cv2.imwrite("color2.png", image)
        pic = cv2.imread('color2.png')
        cv2.imshow("color2.png", pic)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def pushButton_3pushed(self):
        image = cv2.imread("dog.bmp")
        h_flip = cv2.flip(image, 1)
        cv2.imwrite("dog2.bmp", h_flip)
        pic = cv2.imread('dog2.bmp')
        cv2.imshow("dog.bmp", image)
        cv2.imshow("dog2.bmp", pic)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def pushButton_4pushed(self):
        image = cv2.imread("dog.bmp")
        pic = cv2.imread('dog2.bmp')
        res = cv2.addWeighted(image, 0.5, pic, 0.5, 0)
        cv2.namedWindow('mainIMG')
        cv2.createTrackbar('Alpha', 'mainIMG', 0, 10, nothing)
        print('must press esc to leave')
        while (True):
            cv2.imshow('mainIMG', res)
            if cv2.waitKey(1) == 27:
                break
            alpha = cv2.getTrackbarPos('Alpha', 'mainIMG') / 10
            beta = 1 - alpha
            res = cv2.addWeighted(image, alpha, pic, beta, 0)
        cv2.destroyAllWindows()

    def pushButton_10pushed(self):
        input_angel = int(self.plainTextEdit.toPlainText())
        input_scale = float(self.plainTextEdit_2.toPlainText())
        input_Tx = int(self.plainTextEdit_3.toPlainText())
        input_Ty = int(self.plainTextEdit_4.toPlainText())
        image = cv2.imread("OriginalTransform.png")
        cv2.waitKey(0)
        (h, w) = image.shape[:2]
        center = (130, 125)  # 中心
        cv2.imshow("Original", image)

        M = np.float32([[1, 0, input_Tx], [0, 1, -input_Ty], [0, 0, 1]])  # 轉成三維矩陣
        Rot = cv2.getRotationMatrix2D(center, input_angel, input_scale)  # 旋轉缩放矩阵：(旋转中心，旋轉角度，缩放大小)
        Rot = np.vstack([Rot, [0, 0, 1]])
        changedMatrix = np.matmul(M, Rot)  # mix兩個改變到矩陣
        changed = cv2.warpPerspective(image, changedMatrix, (w, h), flags=cv2.INTER_LANCZOS4)
        cv2.imshow("Changed", changed)
        cv2.waitKey(0)

    def mouse_callback(self, event, x, y, flags, params):
        image = cv2.imread("OriginalPerspective.png")
        # left-click event value is 1
        if event == 1:
            test=np.array([])
            clicks.append([x, y])
            x,y = clicks[0]
            if len(clicks) == 4:
                x1,y1 = clicks[0]
                x2,y2 = clicks[1]
                x3,y3 = clicks[2]
                x4,y4 = clicks[3]
                top_left_x = min([x1, x2, x3, x4])
                top_left_y = min([y1, y2, y3, y4])
                bot_right_x = max([x1, x2, x3, x4])
                bot_right_y = max([y1, y2, y3, y4])
                cropped__img = image[top_left_y:bot_right_y, top_left_x:bot_right_x]
                cv2.imshow("cropped", cropped__img)
                clicks.clear()
                cv2.waitKey(0)


    def pushButton_9pushed(self):
        image = cv2.imread("OriginalPerspective.png")
        right_clicks = list()
        scale_width = 640 / image.shape[1]
        scale_height = 480 / image.shape[0]
        scale = min(scale_width, scale_height)
        window_width = int(image.shape[1] * scale)
        window_height = int(image.shape[0] * scale)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', window_width, window_height)
        # set mouse callback function for window
        cv2.imshow('image', image)
        cv2.setMouseCallback('image', self.mouse_callback)
        cv2.waitKey(0)

    def pushButton_5pushed(self):
        im = Image.open('School.jpg')
        width = im.size[0]
        height = im.size[1]
        im = im.convert('RGB')
        array = []
        for x in range(width):
            for y in range(height):
                r, g, b = im.getpixel((x, y))
                rgb = (r, g, b)
                array.append(rgb)
        print(array)

