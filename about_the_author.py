import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QLabel, QGraphicsAnchorLayout, QGridLayout, QVBoxLayout, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class AboutTheAuthor(QWidget):

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
        self.welcome_title.setText("<b>About the Author:</b>")
        self.welcome_title.adjustSize()
        grid.addWidget(self.welcome_title, 0, 0, 1, 3)
        # Author Info
        self.author_info = QLabel(self, alignment=Qt.AlignRight | Qt.AlignVCenter)
        self.author_info.setText('Craig Cuninghame -  <a href="http://www.cuninghamedesign.co.uk/">Cuninghame Design Ltd</a>')
        self.author_info.setOpenExternalLinks(True)
        self.author_info.adjustSize()
        grid.addWidget(self.author_info, 3, 1, 1, 3)

        # Add button links to the functions
        self.introduction_text = QLabel(self, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        self.introduction_text.setText("Hi, my name is Craig Cuninghame\n"
                                       "I am an Electrical Engineer by trade\n "
                                       "and a part time programmer by night\n"
                                       "Lorem ipsum dolor sit amet, mei no case doctus, te vix errem nominati, "
                                       "ut quo scripta alterum placerat. Eum natum assentior at, ex est debet laudem. "
                                       "Sea altera offendit id, quo melius albucius ex. In cum etiam repudiandae, ea "
                                       "his sint hinc accusata. Mel an rebum melius impetus, ei vel enim soleat "
                                       "option.Has semper commodo ea. Quaeque ornatus has et. No cum nemore malorum, "
                                       "no numquam ancillae sed, commodo conceptam ut per. Cu sit sale dicit "
                                       "facilisis, nam audiam apeirian reprimique ei. Summo qualisque molestiae "
                                       "mel id. Omnesque accusamus et sea, has essent reprimique accommodare ad, "
                                       "duo ex possit eirmod noluisse.")
        self.introduction_text.adjustSize()
        self.introduction_text.setWordWrap(True)
        grid.addWidget(self.introduction_text, 1, 0, 1, 3)

        # pic = QtGui.QLabel(window)
        # pic.setGeometry(10, 10, 400, 100)
        # # use full ABSOLUTE path to the image, not relative
        # pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/logo.png"))

        # Universal parameter for text grids
        grid.setRowStretch(1, 1)

        # Setup the overall window
        self.resize(1000, 600)  # Window size <<and position on screen .setGeometry(300, 300, 700, 600)>>
        self.center()


        self.setFixedSize(1200, 800)  # Fix the window size so it does't re-size
        self.setWindowTitle('Craig\'s MEP Toolkit')
        self.setWindowIcon(QIcon('web.png'))
        # self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    print("Something has gone wrong here")


if __name__ == '__main__':
    main()
