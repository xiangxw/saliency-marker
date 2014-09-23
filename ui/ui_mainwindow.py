# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Sep 23 16:48:59 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.imageGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.imageGroupBox.setMinimumSize(QtCore.QSize(600, 0))
        self.imageGroupBox.setObjectName("imageGroupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.imageGroupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.imageLayout = QtWidgets.QHBoxLayout()
        self.imageLayout.setObjectName("imageLayout")
        self.horizontalLayout_6.addLayout(self.imageLayout)
        self.horizontalLayout_5.addWidget(self.imageGroupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.optionGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.optionGroupBox.setObjectName("optionGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.optionGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.optionGroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.brushSizeSpinBox = QtWidgets.QSpinBox(self.optionGroupBox)
        self.brushSizeSpinBox.setObjectName("brushSizeSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.brushSizeSpinBox)
        self.brushValueSpinBox = QtWidgets.QSpinBox(self.optionGroupBox)
        self.brushValueSpinBox.setProperty("value", 1)
        self.brushValueSpinBox.setObjectName("brushValueSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.brushValueSpinBox)
        self.label_3 = QtWidgets.QLabel(self.optionGroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.optionGroupBox)
        self.helpGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.helpGroupBox.setObjectName("helpGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.helpGroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.helpLabel = QtWidgets.QLabel(self.helpGroupBox)
        self.helpLabel.setObjectName("helpLabel")
        self.horizontalLayout_3.addWidget(self.helpLabel)
        self.verticalLayout.addWidget(self.helpGroupBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_4.addWidget(self.saveButton)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_4.addWidget(self.resetButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Saliency Marker"))
        self.imageGroupBox.setTitle(_translate("MainWindow", "Image"))
        self.optionGroupBox.setTitle(_translate("MainWindow", "Option"))
        self.label_2.setText(_translate("MainWindow", "Brush Size"))
        self.label_3.setText(_translate("MainWindow", "Brush Value"))
        self.helpGroupBox.setTitle(_translate("MainWindow", "Help"))
        self.helpLabel.setText(_translate("MainWindow", "Step 1: Set brush size(with of the brush rect).\n"
"Step 2: Set value of the brush to paint(from 0 to 255).\n"
"Step 3: Brush the image and save it."))
        self.saveButton.setText(_translate("MainWindow", "&Save"))
        self.resetButton.setText(_translate("MainWindow", "&Reset"))

