# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(129, -1, 931, 551))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.label = QtWidgets.QLabel(self.page_home)
        self.label.setGeometry(QtCore.QRect(10, 20, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.about_the_author = QtWidgets.QLabel(self.page_home)
        self.about_the_author.setGeometry(QtCore.QRect(10, 90, 331, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.about_the_author.setFont(font)
        self.about_the_author.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.about_the_author.setWordWrap(True)
        self.about_the_author.setObjectName("about_the_author")
        self.stackedWidget.addWidget(self.page_home)
        self.page_drawing_renamer = QtWidgets.QWidget()
        self.page_drawing_renamer.setObjectName("page_drawing_renamer")
        self.pushButton_rename = QtWidgets.QPushButton(self.page_drawing_renamer)
        self.pushButton_rename.setGeometry(QtCore.QRect(7, 490, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_rename.setFont(font)
        self.pushButton_rename.setObjectName("pushButton_rename")
        self.lineEdit_enter_titleblock_search = QtWidgets.QLineEdit(self.page_drawing_renamer)
        self.lineEdit_enter_titleblock_search.setGeometry(QtCore.QRect(7, 341, 250, 20))
        self.lineEdit_enter_titleblock_search.setObjectName("lineEdit_enter_titleblock_search")
        self.lineEdit_enter_replace_text_before = QtWidgets.QLineEdit(self.page_drawing_renamer)
        self.lineEdit_enter_replace_text_before.setGeometry(QtCore.QRect(57, 239, 201, 20))
        self.lineEdit_enter_replace_text_before.setObjectName("lineEdit_enter_replace_text_before")
        self.lineEdit_enter_beginningtext = QtWidgets.QLineEdit(self.page_drawing_renamer)
        self.lineEdit_enter_beginningtext.setGeometry(QtCore.QRect(7, 140, 251, 20))
        self.lineEdit_enter_beginningtext.setObjectName("lineEdit_enter_beginningtext")
        self.pushButton_enter_endtext = QtWidgets.QPushButton(self.page_drawing_renamer)
        self.pushButton_enter_endtext.setGeometry(QtCore.QRect(261, 190, 74, 23))
        self.pushButton_enter_endtext.setObjectName("pushButton_enter_endtext")
        self.pushButton_enter_excel_export = QtWidgets.QPushButton(self.page_drawing_renamer)
        self.pushButton_enter_excel_export.setGeometry(QtCore.QRect(7, 420, 150, 41))
        self.pushButton_enter_excel_export.setObjectName("pushButton_enter_excel_export")
        self.lineEdit_enter_endtext = QtWidgets.QLineEdit(self.page_drawing_renamer)
        self.lineEdit_enter_endtext.setGeometry(QtCore.QRect(8, 191, 250, 20))
        self.lineEdit_enter_endtext.setObjectName("lineEdit_enter_endtext")
        self.label_enter_path = QtWidgets.QLabel(self.page_drawing_renamer)
        self.label_enter_path.setGeometry(QtCore.QRect(7, 60, 231, 21))
        self.label_enter_path.setObjectName("label_enter_path")
        self.Title_lablel_2 = QtWidgets.QLabel(self.page_drawing_renamer)
        self.Title_lablel_2.setGeometry(QtCore.QRect(137, 284, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title_lablel_2.setFont(font)
        self.Title_lablel_2.setObjectName("Title_lablel_2")
        self.label_enter_endtext_3 = QtWidgets.QLabel(self.page_drawing_renamer)
        self.label_enter_endtext_3.setGeometry(QtCore.QRect(7, 390, 331, 31))
        self.label_enter_endtext_3.setWordWrap(True)
        self.label_enter_endtext_3.setObjectName("label_enter_endtext_3")
        self.label_enter_beginningtext = QtWidgets.QLabel(self.page_drawing_renamer)
        self.label_enter_beginningtext.setGeometry(QtCore.QRect(7, 120, 231, 21))
        self.label_enter_beginningtext.setObjectName("label_enter_beginningtext")
        self.line = QtWidgets.QFrame(self.page_drawing_renamer)
        self.line.setGeometry(QtCore.QRect(14, 470, 311, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_enter_replace_text_2 = QtWidgets.QLabel(self.page_drawing_renamer)
        self.label_enter_replace_text_2.setGeometry(QtCore.QRect(17, 237, 41, 21))
        self.label_enter_replace_text_2.setObjectName("label_enter_replace_text_2")
        self.Title_lablel = QtWidgets.QLabel(self.page_drawing_renamer)
        self.Title_lablel.setGeometry(QtCore.QRect(17, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title_lablel.setFont(font)
        self.Title_lablel.setObjectName("Title_lablel")
        self.pushButton_enter_path = QtWidgets.QPushButton(self.page_drawing_renamer)
        self.pushButton_enter_path.setGeometry(QtCore.QRect(213, 60, 120, 20))
        self.pushButton_enter_path.setObjectName("pushButton_enter_path")
        self.pushButton_enter_replace_text = QtWidgets.QPushButton(self.page_drawing_renamer)
        self.pushButton_enter_replace_text.setGeometry(QtCore.QRect(261, 240, 74, 41))
        self.pushButton_enter_replace_text.setObjectName("pushButton_enter_replace_text")
        self.pushButton_enter_beginningtext = QtWidgets.QPushButton(self.page_drawing_renamer)
        self.pushButton_enter_beginningtext.setGeometry(QtCore.QRect(260, 139, 75, 23))
        self.pushButton_enter_beginningtext.setObjectName("pushButton_enter_beginningtext")
        self.label_pathname = QtWidgets.QLabel(self.page_drawing_renamer)
        self.label_pathname.setGeometry(QtCore.QRect(7, 80, 311, 20))
        self.label_pathname.setObjectName("label_pathname")
        self.lineEdit_enter_replace_text_after = QtWidgets.QLineEdit(self.page_drawing_renamer)
        self.lineEdit_enter_replace_text_after.setGeometry(QtCore.QRect(57, 262, 201, 20))
        self.lineEdit_enter_replace_text_after.setObjectName("lineEdit_enter_replace_text_after")
        self.label_enter_titleblock_search = QtWidgets.QLabel(self.page_drawing_renamer)
        self.label_enter_titleblock_search.setGeometry(QtCore.QRect(7, 321, 311, 21))
        self.label_enter_titleblock_search.setObjectName("label_enter_titleblock_search")
        self.Title_lablel_3 = QtWidgets.QLabel(self.page_drawing_renamer)
        self.Title_lablel_3.setGeometry(QtCore.QRect(137, 359, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title_lablel_3.setFont(font)
        self.Title_lablel_3.setObjectName("Title_lablel_3")
        self.label_enter_replace_text = QtWidgets.QLabel(self.page_drawing_renamer)
        self.label_enter_replace_text.setGeometry(QtCore.QRect(8, 219, 230, 21))
        self.label_enter_replace_text.setObjectName("label_enter_replace_text")
        self.listWidget = QtWidgets.QListWidget(self.page_drawing_renamer)
        self.listWidget.setGeometry(QtCore.QRect(337, 10, 581, 531))
        self.listWidget.setObjectName("listWidget")
        self.label_enter_replace_text_3 = QtWidgets.QLabel(self.page_drawing_renamer)
        self.label_enter_replace_text_3.setGeometry(QtCore.QRect(17, 260, 41, 21))
        self.label_enter_replace_text_3.setObjectName("label_enter_replace_text_3")
        self.pushButton_enter_excel_export_2 = QtWidgets.QPushButton(self.page_drawing_renamer)
        self.pushButton_enter_excel_export_2.setGeometry(QtCore.QRect(177, 420, 150, 41))
        self.pushButton_enter_excel_export_2.setObjectName("pushButton_enter_excel_export_2")
        self.label_enter_endtext = QtWidgets.QLabel(self.page_drawing_renamer)
        self.label_enter_endtext.setGeometry(QtCore.QRect(8, 171, 230, 21))
        self.label_enter_endtext.setObjectName("label_enter_endtext")
        self.pushButton_enter_titleblock_search = QtWidgets.QPushButton(self.page_drawing_renamer)
        self.pushButton_enter_titleblock_search.setGeometry(QtCore.QRect(260, 340, 74, 23))
        self.pushButton_enter_titleblock_search.setObjectName("pushButton_enter_titleblock_search")
        self.stackedWidget.addWidget(self.page_drawing_renamer)
        self.page_standards_search = QtWidgets.QWidget()
        self.page_standards_search.setObjectName("page_standards_search")
        self.stackedWidget.addWidget(self.page_standards_search)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(100, 20, 31, 511))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.button_home = QtWidgets.QToolButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(10, 20, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.button_drawingrenamer = QtWidgets.QToolButton(self.centralwidget)
        self.button_drawingrenamer.setGeometry(QtCore.QRect(10, 90, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_drawingrenamer.setFont(font)
        self.button_drawingrenamer.setObjectName("button_drawingrenamer")
        self.button_standardssearch = QtWidgets.QToolButton(self.centralwidget)
        self.button_standardssearch.setGeometry(QtCore.QRect(10, 160, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_standardssearch.setFont(font)
        self.button_standardssearch.setObjectName("button_standardssearch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Craig\'s MEP Toolkit"))
        self.about_the_author.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hi, my name is Craig Cuninghame. I am an engineer by day, and part time programmer by night. I would love to spend more time on my hobbies, but alas, life gets in the way. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here is a link to my website: <a href=\"https://www.cuninghamedesign.co.uk/\"><span style=\" text-decoration: underline; color:#0000ff;\">Craig Cuninghame</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here is a link to my <a href=\"https://www.linkedin.com/in/craig-cuninghame-a86a2082/\"><span style=\" text-decoration: underline; color:#0000ff;\">LinkedIn</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_rename.setText(_translate("MainWindow", "Rename"))
        self.lineEdit_enter_titleblock_search.setText(_translate("MainWindow", "<<Enter Sample Drawing Number>>"))
        self.pushButton_enter_endtext.setText(_translate("MainWindow", "Preview"))
        self.pushButton_enter_excel_export.setText(_translate("MainWindow", "1.Export"))
        self.label_enter_path.setToolTip(_translate("MainWindow", "<html><head/><body><p>e.g. \'C:/Users/Craig/Desktop/Foldername\'</p></body></html>"))
        self.label_enter_path.setText(_translate("MainWindow", "Open the folder with the files to rename:"))
        self.Title_lablel_2.setText(_translate("MainWindow", "Or"))
        self.label_enter_endtext_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter a sample drawing number as the programme searches for the same format</p></body></html>"))
        self.label_enter_endtext_3.setText(_translate("MainWindow", "Use Excel to rename the files:"))
        self.label_enter_beginningtext.setToolTip(_translate("MainWindow", "<html><head/><body><p>e.g. &quot;Your_Filename&quot; becomes &quot;Additional Text Your Filename&quot;</p></body></html>"))
        self.label_enter_beginningtext.setText(_translate("MainWindow", "Enter text to add to the start of the filename:"))
        self.label_enter_replace_text_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>e.g. &quot;Your_Filename&quot; becomes &quot;Additional Text Your Filename&quot;</p></body></html>"))
        self.label_enter_replace_text_2.setText(_translate("MainWindow", "Before"))
        self.Title_lablel.setText(_translate("MainWindow", "Drawing Renamer V1"))
        self.pushButton_enter_path.setText(_translate("MainWindow", "Open"))
        self.pushButton_enter_replace_text.setText(_translate("MainWindow", "Preview"))
        self.pushButton_enter_beginningtext.setText(_translate("MainWindow", "Preview"))
        self.label_pathname.setText(_translate("MainWindow", "<<Filepath>>"))
        self.label_enter_titleblock_search.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter a sample drawing number as the programme searches for the same format</p></body></html>"))
        self.label_enter_titleblock_search.setText(_translate("MainWindow", "Attempt to rename the file automatically from the title block:"))
        self.Title_lablel_3.setText(_translate("MainWindow", "Or"))
        self.label_enter_replace_text.setToolTip(_translate("MainWindow", "<html><head/><body><p>Leave the \'after\' box blank if you want text deleted from the filename</p></body></html>"))
        self.label_enter_replace_text.setText(_translate("MainWindow", "Replace text within a filename:"))
        self.label_enter_replace_text_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>e.g. &quot;Your_Filename&quot; becomes &quot;Additional Text Your Filename&quot;</p></body></html>"))
        self.label_enter_replace_text_3.setText(_translate("MainWindow", "After"))
        self.pushButton_enter_excel_export_2.setText(_translate("MainWindow", "2.Import"))
        self.label_enter_endtext.setToolTip(_translate("MainWindow", "<html><head/><body><p>e.g. &quot;Your_Filename&quot; becomes &quot;Your Filename Additional Text&quot;</p></body></html>"))
        self.label_enter_endtext.setText(_translate("MainWindow", "Enter text to add to the end of the filename:"))
        self.pushButton_enter_titleblock_search.setText(_translate("MainWindow", "Preview"))
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.button_drawingrenamer.setText(_translate("MainWindow", "Drawing \n"
" Renamer"))
        self.button_standardssearch.setText(_translate("MainWindow", "Standards \n"
" Search"))
