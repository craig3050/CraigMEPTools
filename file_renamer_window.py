import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QLabel, QGraphicsAnchorLayout, QGridLayout, QVBoxLayout, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Grid Layout
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(10)

        # Add standard text
        # Welcome Title
        self.welcome_title = QLabel(self, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        self.welcome_title.setText("<b>File Renamer:</b>")
        self.welcome_title.adjustSize()
        grid.addWidget(self.welcome_title, 0, 0, 1, 3)
        # Author Info
        self.author_info = QLabel(self, alignment=Qt.AlignRight | Qt.AlignVCenter)
        self.author_info.setText('Craig Cuninghame -  <a href="http://www.cuninghamedesign.co.uk/">Cuninghame Design Ltd</a>')
        self.author_info.setOpenExternalLinks(True)
        self.author_info.adjustSize()
        grid.addWidget(self.author_info, 8, 1, 1, 3)

        # Add button links to the functions


        # Universal parameter for text grids
        grid.setRowStretch(1, 1)

        # Setup the overall window
        self.resize(300, 300)  # Window size <<and position on screen .setGeometry(300, 300, 700, 600)>>
        self.center()


        self.setFixedSize(550, 400)  # Fix the window size so it does't re-size
        self.setWindowTitle('Craig\'s MEP Toolkit')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())