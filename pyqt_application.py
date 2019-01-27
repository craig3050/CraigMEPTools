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
        self.welcome_title.setText("<b>Welcome to Craig's MEP Toolkit - please select an option:</b>")
        self.welcome_title.adjustSize()
        grid.addWidget(self.welcome_title, 0, 0, 1, 3)
        # Author Info
        self.author_info = QLabel(self, alignment=Qt.AlignRight | Qt.AlignVCenter)
        self.author_info.setText('Craig Cuninghame -  <a href="http://www.cuninghamedesign.co.uk/">Cuninghame Design Ltd</a>')
        self.author_info.setOpenExternalLinks(True)
        self.author_info.adjustSize()
        grid.addWidget(self.author_info, 8, 1, 1, 3)

        # Add button links to the functions
        grid.addWidget(self.fileRenamerButton(), 3, 1)
        grid.addWidget(self.batchImageCompressor(), 4, 1)
        grid.addWidget(self.addPhotostoWordDocument(), 5, 1)
        grid.addWidget(self.aboutTheAuthor(), 6, 1)
        grid.addWidget(self.exitProgramme(), 7, 1)

        # Universal parameter for text grids
        grid.setRowStretch(1, 1)

        # Setup the overall window
        self.resize(300, 300)  # Window size <<and position on screen .setGeometry(300, 300, 700, 600)>>
        self.center()


        self.setFixedSize(550, 400)  # Fix the window size so it does't re-size
        self.setWindowTitle('Craig MEP Toolkit')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def fileRenamerButton(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        btn = QPushButton('Rename Files', self)
        btn.setToolTip('Functions:\n1. Delete / Add Text\n2. Add Text to Beginning of File Name\n'
                       '3. Add Text to End of File Name\n4. Rename drawings to whatever is in the PDF titleblock\n'
                       '5. Export drawings to an excel list, then re-name files based on the second column')
        btn.resize(400, 50)
        btn.move(75, 50)

    def batchImageCompressor(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        btn = QPushButton('Batch Image Compressor', self)
        btn.setToolTip('This tool compresses a folder full of images to make them easier to e-mail')
        btn.resize(400, 50)
        btn.move(75, 110)

    def addPhotostoWordDocument(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        btn = QPushButton('Add photos to Word Document', self)
        btn.setToolTip('This tool adds a folder of photos to a word document. This is useful for site survey reports')
        btn.resize(400, 50)
        btn.move(75, 170)

    def aboutTheAuthor(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        btn = QPushButton('About', self)
        # btn.setToolTip('Who am i?')
        btn.resize(400, 50)
        btn.move(75, 230)

    def exitProgramme(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        btn = QPushButton('Exit', self)
        btn.clicked.connect(QApplication.instance().quit)
        # btn.setToolTip('Get me out of here!')
        btn.resize(400, 50)
        btn.move(75, 290)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
