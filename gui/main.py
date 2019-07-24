from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

import sys
sys.path.append("..")

from wxobs.observation import Observation


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Weather Observations'
        self.left = 100
        self.top = 50
        self.width = 800
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        text = QLabel()
        text.setWordWrap(True)
        button = QPushButton('Get Latest')
        button.clicked.connect(lambda: text.setText(_get_latest_ob()))
        layout = QVBoxLayout()
        layout.addWidget(text)
        layout.addWidget(button)
        layout.setAlignment(button, Qt.AlignHCenter)
        self.setLayout(layout)

        self.show()


def _get_latest_ob():
    ob = Observation()
    return ob.raw


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
