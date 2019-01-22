import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QLabel, QGraphicsAnchorLayout, QGridLayout
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
        self.welcome_title.setText("Welcome to Craig's MEP Toolkit - please select an option:")
        self.welcome_title.adjustSize()
        self.welcome_title.setFont(QFont("Ariel", weight=QFont.Bold))
        grid.addWidget(self.welcome_title, 0, 0)
        # Author Info
        self.author_info = QLabel(self, alignment=Qt.AlignRight | Qt.AlignVCenter)
        self.author_info.setText('Craig Cuninghame - Cuninghame Design Ltd')
        self.author_info.adjustSize()
        grid.addWidget(self.author_info, 5, 1)
        # Universal perameter for text grids
        grid.setRowStretch(1, 1)

        # Add button links to the functions

        # Setup the overall window
        self.setGeometry(300, 300, 1000, 750)  # Window size and position on screen
        self.setWindowTitle('Craig MEP Toolkit')
        self.setWindowIcon(QIcon('web.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
