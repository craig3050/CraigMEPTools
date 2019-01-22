import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QLabel, QGraphicsAnchorLayout, QGridLayout, QVBoxLayout
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

        # Add standard text
        # Welcome Title
        self.welcome_title = QLabel(self, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        self.welcome_title.setText("<b>Welcome to Craig's MEP Toolkit - please select an option:</b>")
        self.welcome_title.adjustSize()
        grid.addWidget(self.welcome_title, 0, 0)
        # Author Info
        self.author_info = QLabel(self, alignment=Qt.AlignRight | Qt.AlignVCenter)
        self.author_info.setText('Craig Cuninghame - Cuninghame Design Ltd')
        self.author_info.adjustSize()
        grid.addWidget(self.author_info, 5, 1)

        # Add button links to the functions
        grid.addWidget(self.fileRenamerButton(), 3, 1)

        # Universal parameter for text grids
        grid.setRowStretch(1, 1)

        # Setup the overall window
        self.setGeometry(300, 300, 1000, 750)  # Window size and position on screen
        self.setWindowTitle('Craig MEP Toolkit')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def fileRenamerButton(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        btn = QPushButton('Rename Files', self)
        btn.setToolTip('Functions:\n1. Delete / Add Text\n2. Add Text to Beginning of File Name\n'
                       '3. Add Text to End of File Name\n4. Rename drawings to whatever is in the PDF titleblock\n'
                       '5. Export drawings to an excel list, then re-name files based on the second column')
        #btn.resize(btn.sizeHint())
        #btn.move(100, 100)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
