# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Thu Oct  9 17:26:52 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.imageGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.imageGroupBox.setMinimumSize(QtCore.QSize(600, 0))
        self.imageGroupBox.setObjectName("imageGroupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.imageGroupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.imageGroupBoxLayout = QtWidgets.QVBoxLayout()
        self.imageGroupBoxLayout.setObjectName("imageGroupBoxLayout")
        self.horizontalLayout_6.addLayout(self.imageGroupBoxLayout)
        self.horizontalLayout_5.addWidget(self.imageGroupBox)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.optionGroupBox = QtWidgets.QGroupBox(self.widget)
        self.optionGroupBox.setObjectName("optionGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.optionGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.optionGroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.brushSizeSpinBox = QtWidgets.QSpinBox(self.optionGroupBox)
        self.brushSizeSpinBox.setMinimum(1)
        self.brushSizeSpinBox.setMaximum(100)
        self.brushSizeSpinBox.setProperty("value", 1)
        self.brushSizeSpinBox.setObjectName("brushSizeSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.brushSizeSpinBox)
        self.label_3 = QtWidgets.QLabel(self.optionGroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.brushValueDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.optionGroupBox)
        self.brushValueDoubleSpinBox.setProperty("value", 1.0)
        self.brushValueDoubleSpinBox.setObjectName("brushValueDoubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.brushValueDoubleSpinBox)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.optionGroupBox)
        self.helpGroupBox = QtWidgets.QGroupBox(self.widget)
        self.helpGroupBox.setObjectName("helpGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.helpGroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.helpLabel = QtWidgets.QLabel(self.helpGroupBox)
        self.helpLabel.setObjectName("helpLabel")
        self.horizontalLayout_3.addWidget(self.helpLabel)
        self.verticalLayout.addWidget(self.helpGroupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.openAction = QtWidgets.QAction(MainWindow)
        self.openAction.setObjectName("openAction")
        self.saveAction = QtWidgets.QAction(MainWindow)
        self.saveAction.setObjectName("saveAction")
        self.toolBar.addAction(self.openAction)
        self.toolBar.addAction(self.saveAction)

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
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.openAction.setText(_translate("MainWindow", "Open"))
        self.openAction.setToolTip(_translate("MainWindow", "Open Image File        Ctrl+O"))
        self.openAction.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.saveAction.setText(_translate("MainWindow", "Save"))
        self.saveAction.setToolTip(_translate("MainWindow", "Save Result        Ctrl+S"))
        self.saveAction.setShortcut(_translate("MainWindow", "Ctrl+S"))

