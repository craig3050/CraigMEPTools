import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

from MainUI import Ui_MainWindow

from Drawing_Renamer import Drawing_Renamer_Tools
from Standards_Search import Standards_Search_Tools
from Image_Tools import Image_Tools
from check_for_updates import Check_For_Updates

##Global Variables##
current_version_number = 1.3
main_file_list = {}
file_path = ""
file_path_standards = ""
list_of_standards = []
document_to_write = ""
file_path_imagetools = ""
list_of_images = []
logo_file_path = ""
file_path_drawing_to_stamp = ""
file_path_logo_to_stamp = ""
list_of_drawingstostamp = ""


#For scaling application on different resolutions
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

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
        self.ui.button_imagetools.clicked.connect(self.show_page_image_tools)
        self.ui.button_drawingstamper.clicked.connect(self.show_page_drawing_stamper)
        self.welcome_text()

## Page 1 - Home Page
        self.ui.about_the_author.setOpenExternalLinks(True)

## Page 2 - Drawing Renamer ############################################################################
        self.ui.pushButton_enter_path.clicked.connect(self.enter_path)
        self.ui.pushButton_enter_beginningtext.clicked.connect(self.enter_beginningtext)
        self.ui.pushButton_enter_endtext.clicked.connect(self.enter_endtext)
        self.ui.pushButton_enter_replace_text.clicked.connect(self.enter_replace_text)
        self.ui.pushButton_enter_titleblock_search.clicked.connect(self.enter_titleblock_search)
        self.ui.pushButton_rename.clicked.connect(self.rename_file)
        self.ui.pushButton_enter_excel_export.clicked.connect(self.excel_list_export)
        self.ui.pushButton_enter_excel_export_2.clicked.connect(self.excel_list_import)


## Page 3 - Standards Search ############################################################################
        self.ui.pushButton_enter_path_standards.clicked.connect(self.enter_path_standards)
        self.ui.pushButton_enter_path_standards_2.clicked.connect(self.standards_search_bsi)
        self.ui.pushButton_enter_path_standards_3.clicked.connect(self.export_standards_to_text_file)

## Page 4 - Image Tools ############################################################################
        self.ui.pushButton_enter_path_imagetools.clicked.connect(self.enter_path_imagetools)
        self.ui.pushButton_compress_pictures.clicked.connect(self.compress_pictures)
        self.ui.pushButton_enter_path_imagetools_2.clicked.connect(self.enter_path_imagetools_logo)
        self.ui.pushButton_add_a_logo.clicked.connect(self.add_a_logo)

## Page 5 - Drawing Stamper ############################################################################
        self.ui.pushButton_enter_path_drawing_stamper.clicked.connect(self.enter_path_drawingstostamp)
        self.ui.pushButton_enter_path_drawing_stamper_2.clicked.connect(self.enter_path_logotostamp)
        self.ui.pushButton_drawing_stamp_go.clicked.connect(self.process_drawing_stamps)

    def show(self):
        self.main_win.show()

    def show_page_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
    def show_page_drawingrenamer(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_drawing_renamer)
    def show_page_standardssearch(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_standards_search)
    def show_page_image_tools(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_image_tools)
    def show_page_drawing_stamper(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_stamper)

    def welcome_text(self):
        global current_version_number
        self.ui.listWidget_home.clear()
        self.ui.listWidget_home.addItem("Welcome")
        self.ui.listWidget_home.addItem("Checking for updates...\n")
        try:
            version_number = Check_For_Updates()
            new_version_number = version_number.return_version_number()
            print(new_version_number)
            self.ui.listWidget_home.addItem(f"Version number is {current_version_number}, latest version is {new_version_number}")
            change_log = version_number.return_change_log()
            print(change_log)
            self.ui.listWidget_home.addItem(f"=================\n\nChange Log:\n\n{change_log}")
        except Exception as e:
            self.ui.listWidget_home.addItem(f"Unable to check for updates.\n {e}")



## Page 2 - Drawing Renamer #################################
    def enter_path(self):
        global file_path
        global main_file_list
        main_file_list.clear()
        file_path = QFileDialog.getExistingDirectory(None, "Open a folder", "C:\\", QFileDialog.ShowDirsOnly)
        file_details = Drawing_Renamer_Tools(file_path, main_file_list)
        main_file_list = file_details.return_list_of_files()
        self.ui.label_pathname.setText(file_path)
        self.ui.listWidget.clear()
        for file_name in main_file_list:
            self.ui.listWidget.addItem(file_name)
        return

    def enter_beginningtext(self):
        global file_path
        global main_file_list
        file_details = Drawing_Renamer_Tools(file_path, main_file_list)
        beginning_text = self.ui.lineEdit_enter_beginningtext.text()
        self.ui.listWidget.clear()
        main_file_list = file_details.enter_beginningtext(beginning_text)
        for key, values in main_file_list.items():
            text_to_print = f'{key} =====> {values}'
            self.ui.listWidget.addItem(text_to_print)
        return

    def enter_endtext(self):
        global file_path
        global main_file_list
        file_details = Drawing_Renamer_Tools(file_path, main_file_list)
        end_text = self.ui.lineEdit_enter_endtext.text()
        self.ui.listWidget.clear()
        main_file_list = file_details.enter_endtext(end_text)
        for key, values in main_file_list.items():
            text_to_print = f'{key} =====> {values}'
            self.ui.listWidget.addItem(text_to_print)
        return

    def enter_replace_text(self):
        global file_path
        global main_file_list
        file_details = Drawing_Renamer_Tools(file_path, main_file_list)
        replace_text_before = self.ui.lineEdit_enter_replace_text_before.text()
        replace_text_after = self.ui.lineEdit_enter_replace_text_after.text()
        self.ui.listWidget.clear()
        main_file_list = file_details.enter_replace_text(replace_text_before, replace_text_after)
        for key, values in main_file_list.items():
            text_to_print = f'{key} =====> {values}'
            self.ui.listWidget.addItem(text_to_print)
        return

    def enter_titleblock_search(self):
        global file_path
        global main_file_list
        file_details = Drawing_Renamer_Tools(file_path, main_file_list)
        sample_drawing_number = self.ui.lineEdit_enter_titleblock_search.text()
        self.ui.listWidget.clear()
        self.ui.listWidget.addItem("Please wait - this may take a while...")
        self.ui.listWidget.addItem("Do not close window until complete - new drawings will list as they are found\n")
        for item in main_file_list:
            try:
                file_extension = item.split(".")[-1]
                full_file_path = f'{file_path}/{item}'
                best_guess_drawing_number = file_details.enter_titleblock_search(full_file_path, sample_drawing_number)
                main_file_list[item] = f'{best_guess_drawing_number}.{file_extension}'
                self.ui.listWidget.addItem(best_guess_drawing_number)
                QtCore.QCoreApplication.processEvents()
            # If it all goes wrong leave filename as is
            except Exception as e:
                main_file_list[item] = item
                self.ui.listWidget.addItem(e)
        for key, values in main_file_list.items():
            text_to_print = f'{key} =====> {values}'
            self.ui.listWidget.addItem(text_to_print)
        return

    def rename_file(self):
        global file_path
        global main_file_list
        file_details = Drawing_Renamer_Tools(file_path, main_file_list)
        self.ui.listWidget.clear()
        self.ui.listWidget.addItem("Renaming files")
        temp_dict = {}
        try:
            for key, values in main_file_list.items():
                new_file_name = file_path + "/" + values
                old_file_name = file_path + "/" + key
                file_details.rename_file(old_file_name, new_file_name)
                self.ui.listWidget.addItem("Renaming files")
                text_to_print = f'{old_file_name} =====> {new_file_name}'
                self.ui.listWidget.addItem(text_to_print)
                temp_dict[values] = values
        except Exception as e:
            self.ui.listWidget.addItem(e)
        main_file_list = temp_dict
        self.ui.listWidget.addItem("Rename Completed Successfully")

    def excel_list_export(self):
        try:
            global file_path
            global main_file_list
            file_details = Drawing_Renamer_Tools(file_path, main_file_list)
            self.ui.listWidget.clear()
            self.ui.listWidget.addItem("Saving files to excel sheet...")
            file_details.excel_list_export()
            self.ui.listWidget.clear()
            self.ui.listWidget.addItem("Excel file called \'Drawing_list\' has been saved in the same folder as the drawings")
            self.ui.listWidget.addItem("\n\nAdd your new drawing numbers into Column C")
            self.ui.listWidget.addItem("\n\nOnce complete make sure the file is closed, then press \'2.Import\'")
        except Exception as e:
            self.ui.listWidget.clear()
            self.ui.listWidget.addItem("Something has gone wrong - see exception below:\n\n")
            self.ui.listWidget.addItem(e)

    def excel_list_import(self):
        try:
            global file_path
            global main_file_list
            file_details = Drawing_Renamer_Tools(file_path, main_file_list)
            self.ui.listWidget.clear()
            main_file_list = file_details.excel_list_import()
            self.ui.listWidget.addItem("Displaying Values:\n")
            for key, values in main_file_list.items():
                text_to_print = f'{key} =====> {values}'
                self.ui.listWidget.addItem(text_to_print)
        except Exception as e:
            self.ui.listWidget.clear()
            self.ui.listWidget.addItem("Something has gone wrong - see exception below:\n\n")
            self.ui.listWidget.addItem(e)

## Page 3 - Standards Search ############################################################################

    def enter_path_standards(self):
        global file_path_standards
        global list_of_standards
        self.ui.listWidget.clear()
        try:
            file_path_standards = QFileDialog.getOpenFileName(None, "Open a folder", "C:\\")
            file_path_standards = file_path_standards[0]
            print(file_path_standards)
            self.ui.label_pathname_standards.setText(file_path_standards)
            self.ui.listWidget_standards.clear()
            self.ui.listWidget_standards.addItem("File Loaded Successfully")
            self.ui.listWidget_standards.addItem("Searching for Standards - please wait...")
            QtCore.QCoreApplication.processEvents()
            file_details = Standards_Search_Tools(file_path_standards)
            full_text_from_document = file_details.extract_text_from_pdf()
            print(full_text_from_document)
            list_of_standards = file_details.text_search_for_standards(full_text_from_document)
            self.ui.listWidget_standards.clear()
            self.ui.listWidget_standards.addItem("Standards found within the document:\n")
            for item in list_of_standards:
                self.ui.listWidget_standards.addItem(item)
        except Exception as e:
            self.ui.listWidget_standards.addItem(e)

    def standards_search_bsi(self):
        global file_path_standards
        global list_of_standards
        global document_to_write
        file_details = Standards_Search_Tools(file_path_standards)
        self.ui.listWidget_standards.clear()
        self.ui.listWidget_standards.addItem("Searching the BSI website for status")
        QtCore.QCoreApplication.processEvents()
        document_to_write = ""
        for standard_name in list_of_standards:
            QtCore.QCoreApplication.processEvents()
            temp_document_to_write = ""
            returned_text = file_details.return_list_of_standards(standard_name)
            temp_document_to_write += "\n\n==============================================================================\n\n"
            temp_document_to_write += standard_name
            temp_document_to_write += "\n\n\n"
            for item in returned_text:
                temp_document_to_write += f"Name: {item[0]}\n"
                temp_document_to_write += f"Title: {item[1]}\n"
                temp_document_to_write += f"Publish Date: {item[3]} \n"
                temp_document_to_write += f"Status: {item[5]} \n\n"
            document_to_write += temp_document_to_write
            self.ui.listWidget_standards.addItem(f"Searching BSI for {standard_name}")
        QtCore.QCoreApplication.processEvents()
        self.ui.listWidget_standards.clear()
        self.ui.listWidget_standards.addItem(f"Search Complete\n\n")
        self.ui.listWidget_standards.addItem(document_to_write)

    def export_standards_to_text_file(self):
        global file_path_standards
        global document_to_write
        self.ui.listWidget_standards.clear()
        self.ui.listWidget_standards.addItem("Writing standards to a file...")
        try:
            file_details = Standards_Search_Tools(file_path_standards)
            file_details.write_to_file(document_to_write)
            self.ui.listWidget_standards.addItem("Writing complete. The file will be in the same directory as the source file")
        except Exception as e:
            self.ui.listWidget_standards.addItem(e)

## Page 4 - Image Tools ############################################################################
    def enter_path_imagetools(self):
        global file_path_imagetools
        global list_of_images
        file_path_imagetools = QFileDialog.getExistingDirectory(None, "Open a folder", "C:\\", QFileDialog.ShowDirsOnly)
        file_details = Image_Tools(file_path_imagetools)
        list_of_images = file_details.return_list_of_files()
        self.ui.label_pathname_imagetools.setText(file_path_imagetools)
        self.ui.listWidget_image_tools.clear()
        self.ui.listWidget_image_tools.addItem("List of files in folder:\n")
        for image in list_of_images:
            self.ui.listWidget_image_tools.addItem(image)
        return


    def compress_pictures(self):
        global file_path_imagetools
        compression_quality = self.ui.lineEdit_image_tools_quality.text()
        file_details = Image_Tools(file_path_imagetools)
        file_details.setup_directories()
        self.ui.listWidget_image_tools.clear()
        for image in list_of_images:
            try:
                file_details.compress_pictures(image, compression_quality)
                self.ui.listWidget_image_tools.addItem(f'Converting {image}')
                QtCore.QCoreApplication.processEvents()
            except Exception as e:
                self.ui.listWidget_image_tools.addItem(f'Unable to convert {image} - {e}')
        self.ui.listWidget_image_tools.addItem("\nProgramme Complete")


    def enter_path_imagetools_logo(self):
        global logo_file_path
        global file_path_imagetools
        logo_file_path = QFileDialog.getOpenFileName(None, "Open a folder", "C:\\")
        logo_file_path = logo_file_path[0]
        self.ui.label_pathname_imagetools_3.setText(file_path_imagetools)
        self.ui.listWidget_image_tools.clear()
        self.ui.listWidget_image_tools.addItem("Press \'2. Add a logo to the image\' to start the programme")


    def add_a_logo(self):
        global logo_file_path
        global file_path_imagetools
        self.ui.listWidget_image_tools.clear()
        file_details = Image_Tools(file_path_imagetools)
        for image in list_of_images:
            try:
                print(file_path_imagetools)
                print(image)
                print(logo_file_path)
                file_details.add_a_logo(image, logo_file_path)
                self.ui.listWidget_image_tools.addItem(f'Adding a logo to {image}')
                QtCore.QCoreApplication.processEvents()
            except Exception as e:
                self.ui.listWidget_image_tools.addItem(f'Unable to process {image} - {e}')
        self.ui.listWidget_image_tools.addItem("\nProgramme Complete")

## Page 5 - Drawing Stamper ############################################################################
    def enter_path_drawingstostamp(self):
        global file_path_drawing_to_stamp
        global list_of_drawingstostamp
        self.ui.listWidget_drawing_stamper.clear()
        file_path_drawing_to_stamp = QFileDialog.getExistingDirectory(None, "Open a folder", "C:\\", QFileDialog.ShowDirsOnly)
        file_details = Image_Tools(file_path_drawing_to_stamp)
        list_of_drawingstostamp= file_details.return_list_of_files()
        for drawing in list_of_drawingstostamp:
            self.ui.listWidget_drawing_stamper.addItem(drawing)
        return

    def enter_path_logotostamp(self):
        global file_path_logo_to_stamp
        file_path_logo_to_stamp = QFileDialog.getOpenFileName(None, "Open a file", "C:\\")
        disclaimer_words = self.ui.textEdit_drawing_stamper_disclaimer.toPlainText()
        logo_details = Image_Tools(file_path_logo_to_stamp)
        returned_stamp = logo_details.add_logo_to_drawing_stamp(file_path_logo_to_stamp, disclaimer_words)
        self.ui.listWidget_drawing_stamper.clear()
        self.ui.listWidget_drawing_stamper.addItem("Preview of drawing stamp:")
        myPixmap = QtGui.QPixmap.fromImage(returned_stamp)
        myScaledPixmap = myPixmap.scaled(self.ui.label_show_drawing_stamp.size(), QtCore.Qt.KeepAspectRatio)
        self.ui.label_show_drawing_stamp.setPixmap(myScaledPixmap)
        return

    def process_drawing_stamps(self):
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

