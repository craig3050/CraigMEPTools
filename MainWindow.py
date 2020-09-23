import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from pdf_annotate import PdfAnnotator, Location, Appearance
from datetime import date

from MainUI import Ui_MainWindow

from Drawing_Renamer import Drawing_Renamer_Tools
from Standards_Search import Standards_Search_Tools
from Image_Tools import Image_Tools
from check_for_updates import Check_For_Updates

##Global Variables##
current_version_number = 1.4

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
        self.ui.pushButton_refresh_drawing_stamp.clicked.connect(self.refresh_stamp)

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
        self.main_file_list = {}
        self.main_file_list.clear()
        self.file_path = QFileDialog.getExistingDirectory(None, "Open a folder", "C:\\", QFileDialog.ShowDirsOnly)
        file_details = Drawing_Renamer_Tools(self.file_path, self.main_file_list)
        self.main_file_list = file_details.return_list_of_files()
        self.ui.label_pathname.setText(self.file_path)
        self.ui.listWidget.clear()
        for file_name in self.main_file_list:
            self.ui.listWidget.addItem(file_name)
        return

    def enter_beginningtext(self):
        file_details = Drawing_Renamer_Tools(self.file_path, self.main_file_list)
        beginning_text = self.ui.lineEdit_enter_beginningtext.text()
        self.ui.listWidget.clear()
        self.main_file_list = file_details.enter_beginningtext(beginning_text)
        for key, values in self.main_file_list.items():
            text_to_print = f'{key} =====> {values}'
            self.ui.listWidget.addItem(text_to_print)
        return

    def enter_endtext(self):
        file_details = Drawing_Renamer_Tools(self.file_path, self.main_file_list)
        end_text = self.ui.lineEdit_enter_endtext.text()
        self.ui.listWidget.clear()
        self.main_file_list = file_details.enter_endtext(end_text)
        for key, values in self.main_file_list.items():
            text_to_print = f'{key} =====> {values}'
            self.ui.listWidget.addItem(text_to_print)
        return

    def enter_replace_text(self):
        file_details = Drawing_Renamer_Tools(self.file_path, self.main_file_list)
        replace_text_before = self.ui.lineEdit_enter_replace_text_before.text()
        replace_text_after = self.ui.lineEdit_enter_replace_text_after.text()
        self.ui.listWidget.clear()
        self.main_file_list = file_details.enter_replace_text(replace_text_before, replace_text_after)
        for key, values in self.main_file_list.items():
            text_to_print = f'{key} =====> {values}'
            self.ui.listWidget.addItem(text_to_print)
        return

    def enter_titleblock_search(self):
        file_details = Drawing_Renamer_Tools(self.file_path, self.main_file_list)
        sample_drawing_number = self.ui.lineEdit_enter_titleblock_search.text()
        self.ui.listWidget.clear()
        self.ui.listWidget.addItem("Please wait - this may take a while...")
        self.ui.listWidget.addItem("Do not close window until complete - new drawings will list as they are found\n")
        for item in self.main_file_list:
            try:
                file_extension = item.split(".")[-1]
                full_file_path = f'{self.file_path}/{item}'
                best_guess_drawing_number = file_details.enter_titleblock_search(full_file_path, sample_drawing_number)
                self.main_file_list[item] = f'{best_guess_drawing_number}.{file_extension}'
                self.ui.listWidget.addItem(best_guess_drawing_number)
                QtCore.QCoreApplication.processEvents()
            # If it all goes wrong leave filename as is
            except Exception as e:
                self.main_file_list[item] = item
                self.ui.listWidget.addItem(e)
        for key, values in self.main_file_list.items():
            text_to_print = f'{key} =====> {values}'
            self.ui.listWidget.addItem(text_to_print)
        return

    def rename_file(self):
        file_details = Drawing_Renamer_Tools(self.file_path, self.main_file_list)
        self.ui.listWidget.clear()
        self.ui.listWidget.addItem("Renaming files")
        temp_dict = {}
        try:
            for key, values in self.main_file_list.items():
                new_file_name = self.file_path + "/" + values
                old_file_name = self.file_path + "/" + key
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
            file_details = Drawing_Renamer_Tools(self.file_path, self.main_file_list)
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
            file_details = Drawing_Renamer_Tools(self.file_path, self.main_file_list)
            self.ui.listWidget.clear()
            self.main_file_list = file_details.excel_list_import()
            self.ui.listWidget.addItem("Displaying Values:\n")
            for key, values in self.main_file_list.items():
                text_to_print = f'{key} =====> {values}'
                self.ui.listWidget.addItem(text_to_print)
        except Exception as e:
            self.ui.listWidget.clear()
            self.ui.listWidget.addItem("Something has gone wrong - see exception below:\n\n")
            self.ui.listWidget.addItem(e)

## Page 3 - Standards Search ############################################################################

    def enter_path_standards(self):
        self.ui.listWidget.clear()
        try:
            self.file_path_standards = QFileDialog.getOpenFileName(None, "Open a folder", "C:\\")
            self.file_path_standards = self.file_path_standards[0]
            print(self.file_path_standards)
            self.ui.label_pathname_standards.setText(self.file_path_standards)
            self.ui.listWidget_standards.clear()
            self.ui.listWidget_standards.addItem("File Loaded Successfully")
            self.ui.listWidget_standards.addItem("Searching for Standards - please wait...")
            QtCore.QCoreApplication.processEvents()
            file_details = Standards_Search_Tools(self.file_path_standards)
            full_text_from_document = file_details.extract_text_from_pdf()
            print(full_text_from_document)
            self.list_of_standards = file_details.text_search_for_standards(full_text_from_document)
            self.ui.listWidget_standards.clear()
            self.ui.listWidget_standards.addItem("Standards found within the document:\n")
            for item in self.list_of_standards:
                self.ui.listWidget_standards.addItem(item)
        except Exception as e:
            self.ui.listWidget_standards.addItem(e)

    def standards_search_bsi(self):
        file_details = Standards_Search_Tools(self.file_path_standards)
        self.ui.listWidget_standards.clear()
        self.ui.listWidget_standards.addItem("Searching the BSI website for status")
        QtCore.QCoreApplication.processEvents()
        self.document_to_write = ""
        for standard_name in self.list_of_standards:
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
            self.document_to_write += temp_document_to_write
            self.ui.listWidget_standards.addItem(f"Searching BSI for {standard_name}")
        QtCore.QCoreApplication.processEvents()
        self.ui.listWidget_standards.clear()
        self.ui.listWidget_standards.addItem(f"Search Complete\n\n")
        self.ui.listWidget_standards.addItem(self.document_to_write)

    def export_standards_to_text_file(self):
        self.ui.listWidget_standards.clear()
        self.ui.listWidget_standards.addItem("Writing standards to a file...")
        try:
            file_details = Standards_Search_Tools(self.file_path_standards)
            file_details.write_to_file(self.document_to_write)
            self.ui.listWidget_standards.addItem("Writing complete. The file will be in the same directory as the source file")
        except Exception as e:
            self.ui.listWidget_standards.addItem(e)

## Page 4 - Image Tools ############################################################################
    def enter_path_imagetools(self):
        self.file_path_imagetools = QFileDialog.getExistingDirectory(None, "Open a folder", "C:\\", QFileDialog.ShowDirsOnly)
        file_details = Image_Tools(self.file_path_imagetools)
        self.list_of_images = file_details.return_list_of_files()
        self.ui.label_pathname_imagetools.setText(self.file_path_imagetools)
        self.ui.listWidget_image_tools.clear()
        self.ui.listWidget_image_tools.addItem("List of files in folder:\n")
        for image in self.list_of_images:
            self.ui.listWidget_image_tools.addItem(image)
        return


    def compress_pictures(self):
        compression_quality = self.ui.lineEdit_image_tools_quality.text()
        file_details = Image_Tools(self.file_path_imagetools)
        file_details.setup_directories()
        self.ui.listWidget_image_tools.clear()
        for image in self.list_of_images:
            try:
                file_details.compress_pictures(image, compression_quality)
                self.ui.listWidget_image_tools.addItem(f'Converting {image}')
                QtCore.QCoreApplication.processEvents()
            except Exception as e:
                self.ui.listWidget_image_tools.addItem(f'Unable to convert {image} - {e}')
        self.ui.listWidget_image_tools.addItem("\nProgramme Complete")


    def enter_path_imagetools_logo(self):
        self.logo_file_path = QFileDialog.getOpenFileName(None, "Open a folder", "C:\\")
        self.logo_file_path = self.logo_file_path[0]
        self.ui.label_pathname_imagetools_3.setText(self.file_path_imagetools)
        self.ui.listWidget_image_tools.clear()
        self.ui.listWidget_image_tools.addItem("Press \'2. Add a logo to the image\' to start the programme")


    def add_a_logo(self):
        try:
            self.ui.listWidget_image_tools.clear()
            file_details = Image_Tools(self.file_path_imagetools)
            for image in self.list_of_images:
                try:
                    print(self.file_path_imagetools)
                    print(image)
                    print(self.logo_file_path)
                    file_details.add_a_logo(image, self.logo_file_path)
                    self.ui.listWidget_image_tools.addItem(f'Adding a logo to {image}')
                    QtCore.QCoreApplication.processEvents()
                except Exception as e:
                    self.ui.listWidget_image_tools.addItem(f'Unable to process {image} - {e}')
            self.ui.listWidget_image_tools.addItem("\nProgramme Complete")
        except Exception as e:
            self.ui.listWidget_image_tools.clear()
            self.ui.listWidget_image_tools.addItem("Error - have you loaded the folder?")
            self.ui.listWidget_image_tools.addItem(str(e))


## Page 5 - Drawing Stamper ############################################################################
    def enter_path_drawingstostamp(self):
        self.ui.listWidget_drawing_stamper.clear()
        self.file_path_drawing_to_stamp = QFileDialog.getExistingDirectory(None, "Open a folder", "C:\\", QFileDialog.ShowDirsOnly)
        file_details = Image_Tools(self.file_path_drawing_to_stamp)
        self.list_of_drawingstostamp= file_details.return_list_of_files()
        for drawing in self.list_of_drawingstostamp:
            self.ui.listWidget_drawing_stamper.addItem(drawing)
        return

    def enter_path_logotostamp(self):
        try:
            self.file_path_logo_to_stamp = QFileDialog.getOpenFileName(None, "Open a file", "C:\\")
            disclaimer_words = self.ui.textEdit_drawing_stamper_disclaimer.toPlainText()
            logo_details = Image_Tools(self.file_path_logo_to_stamp)
            returned_stamp = logo_details.add_logo_to_drawing_stamp(self.file_path_logo_to_stamp, disclaimer_words, self.file_path_drawing_to_stamp)
            self.ui.listWidget_drawing_stamper.clear()
            self.ui.listWidget_drawing_stamper.addItem("Preview of drawing stamp:")
            myPixmap = QtGui.QPixmap.fromImage(returned_stamp[0])
            myScaledPixmap = myPixmap.scaled(self.ui.label_show_drawing_stamp.size(), QtCore.Qt.KeepAspectRatio)
            self.ui.label_show_drawing_stamp.setPixmap(myScaledPixmap)
            self.processed_file_stamp = returned_stamp[1]
        except Exception as e:
            self.ui.listWidget_drawing_stamper.clear()
            self.ui.listWidget_drawing_stamper.addItem("You must specify a file")
        return

    def refresh_stamp(self):
        disclaimer_words = self.ui.textEdit_drawing_stamper_disclaimer.toPlainText()
        logo_details = Image_Tools(self.file_path_logo_to_stamp)
        returned_stamp = logo_details.add_logo_to_drawing_stamp(self.file_path_logo_to_stamp, disclaimer_words, self.file_path_drawing_to_stamp)
        self.ui.listWidget_drawing_stamper.clear()
        self.ui.listWidget_drawing_stamper.addItem("Preview of drawing stamp:")
        myPixmap = QtGui.QPixmap.fromImage(returned_stamp[0])
        myScaledPixmap = myPixmap.scaled(self.ui.label_show_drawing_stamp.size(), QtCore.Qt.KeepAspectRatio)
        self.ui.label_show_drawing_stamp.setPixmap(myScaledPixmap)
        self.processed_file_stamp = returned_stamp[1]
        return

    def process_drawing_stamps(self):
        try:
            os.mkdir(f'{self.file_path_drawing_to_stamp}/Stamped')
        except Exception as e:
            print(e)
            self.ui.listWidget_drawing_stamper.clear()
            self.ui.listWidget_drawing_stamper.addItem("Unable to create directory - error code below:\n")
            self.ui.listWidget_drawing_stamper.addItem(str(e))

        today = date.today()
        today_date = today.strftime("%d/%m/%y")

        drawing_status = ""
        if self.ui.radioButton_status_a.isChecked() == True:
            drawing_status = "A"
        elif self.ui.radioButton_status_b.isChecked() == True:
            drawing_status = "B"
        elif self.ui.radioButton_status_c.isChecked() == True:
            drawing_status = "C"
        else:
            drawing_status = "Unknown"

        self.ui.listWidget_drawing_stamper.clear()
        self.ui.listWidget_drawing_stamper.addItem("Adding annotations:\n")
        for drawing in self.list_of_drawingstostamp:
            try:
                full_drawing_path = self.file_path_drawing_to_stamp + '/' + drawing
                self.ui.listWidget_drawing_stamper.addItem(drawing)
                QtCore.QCoreApplication.processEvents()
                full_path_drawing_stamp = self.file_path_drawing_to_stamp + "/Blank_Stamp.png"
                a = PdfAnnotator(full_drawing_path)
                a.add_annotation(
                    'image',
                    Location(x1=50, y1=50, x2=400, y2=400, page=0),
                    Appearance(image=full_path_drawing_stamp)
                )
                a.add_annotation(
                    'text',
                    Location(x1=120, y1=320, x2=300, y2=332, page=0),
                    Appearance(stroke_color=(1, 1, 1), stroke_width=5, content=self.ui.lineEdit_drawing_stamper_jobnumber.text(), fill=(0.705, 0.094, 0.125, 1))
                ) #https://doc.instantreality.org/tools/color_calculator/
                a.add_annotation(
                    'text',
                    Location(x1=130, y1=305, x2=300, y2=317, page=0),
                    Appearance(stroke_color=(1, 1, 1), stroke_width=5, content=self.ui.lineEdit_drawing_stamper_date.text(), fill=(0.705, 0.094, 0.125, 1))
                )
                a.add_annotation(
                    'text',
                    Location(x1=75, y1=276, x2=300, y2=288, page=0),
                    Appearance(stroke_color=(1, 1, 1), stroke_width=5, content=self.ui.lineEdit_drawing_stamper_reviewerinitials.text(), fill=(0.705, 0.094, 0.125, 1))
                )
                a.add_annotation(
                    'text',
                    Location(x1=200, y1=276, x2=320, y2=288, page=0),
                    Appearance(stroke_color=(1, 1, 1), stroke_width=5, content=f"Status {drawing_status}", fill=(0.705, 0.094, 0.125, 1))
                )
                a.add_annotation(
                    'text',
                    Location(x1=330, y1=276, x2=400, y2=288, page=0),
                    Appearance(stroke_color=(1, 1, 1), stroke_width=5, content=today_date, fill=(0.705, 0.094, 0.125, 1))
                )

                # Put an X in the box noting the status
                if drawing_status == "A":
                    a.add_annotation(
                        'text',
                        Location(x1=117, y1=203, x2=300, y2=215, page=0),
                        Appearance(stroke_color=(1, 1, 1), stroke_width=5,
                                   content="X", fill=(0.705, 0.094, 0.125, 1))
                    )
                if drawing_status == "B":
                    a.add_annotation(
                        'text',
                        Location(x1=117, y1=189, x2=300, y2=201, page=0),
                        Appearance(stroke_color=(1, 1, 1), stroke_width=5,
                                   content="X", fill=(0.705, 0.094, 0.125, 1))
                    )
                if drawing_status == "C":
                    a.add_annotation(
                        'text',
                        Location(x1=117, y1=174, x2=300, y2=186, page=0),
                        Appearance(stroke_color=(1, 1, 1), stroke_width=5,
                                   content="X", fill=(0.705, 0.094, 0.125, 1))
                    )

            except Exception as e:
                print(e)
                self.ui.listWidget_drawing_stamper.addItem("Unable to add annotation - error code below:\n")
                self.ui.listWidget_drawing_stamper.addItem(str(e))
                self.ui.listWidget_drawing_stamper.addItem("Check - is this file a PDF?")


            try:
                #Write the resultant file
                a.write(f'{self.file_path_drawing_to_stamp}/Stamped/{drawing}')
            except Exception as e:
                print(e)
                self.ui.listWidget_drawing_stamper.addItem("Unable to save file - error code below:\n")
                self.ui.listWidget_drawing_stamper.addItem(str(e))
                self.ui.listWidget_drawing_stamper.addItem("Check - do these files already exist?")
                return

        #Display success message
        self.ui.listWidget_drawing_stamper.clear()
        self.ui.listWidget_drawing_stamper.addItem("Stamps added successfully!")

        return




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

