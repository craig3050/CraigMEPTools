import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from MainUI import Ui_MainWindow

class MainWindow:
    def __init__(self):
##Page 0 - Main Page side menu
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        self.ui.button_home.clicked.connect(self.show_page_home)
        self.ui.button_drawingrenamer.clicked.connect(self.show_page_drawingrenamer)
        self.ui.button_standardssearch.clicked.connect(self.show_page_standardssearch)

## Page 1 - Home Page


## Page 2 - Drawing Renamer
        self.ui.pushButton_enter_path.clicked.connect(self.enter_path)
        self.ui.pushButton_enter_beginningtext.clicked.connect(self.enter_beginningtext)
        self.ui.pushButton_enter_endtext.clicked.connect(self.enter_endtext)
        self.ui.pushButton_enter_replace_text.clicked.connect(self.enter_replace_text)
        self.ui.pushButton_enter_titleblock_search.clicked.connect(self.enter_titleblock_search)
        self.ui.pushButton_rename.clicked.connect(self.rename_file)
        self.ui.pushButton_enter_excel_export.clicked.connect(self.excel_list_export)
        self.ui.pushButton_enter_excel_export_2.clicked.connect(self.excel_list_import)


    def show(self):
        self.main_win.show()

    def show_page_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
    def show_page_drawingrenamer(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_drawing_renamer)
    def show_page_standardssearch(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_standards_search)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

