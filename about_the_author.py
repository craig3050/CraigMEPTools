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
        self.introduction_text.setText("""
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Arial'; font-size:8pt; font-weight:400; font-style:normal;">
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Hi, my name is Craig Cuninghame. I am an engineer by day, and part time programmer by night. I would love to spend more time on my hobbies, but alas, life gets in the way. </p>
<p style="-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Here is a link to my website: <a href="https://www.cuninghamedesign.co.uk/"><span style=" text-decoration: underline; color:#0000ff;">Craig Cuninghame</span></a></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Here is a link to my <a href="https://www.linkedin.com/in/craig-cuninghame-a86a2082/"><span style=" text-decoration: underline; color:#0000ff;">LinkedIn</span></a></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>
        """)
        self.introduction_text.setOpenExternalLinks(True)
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
