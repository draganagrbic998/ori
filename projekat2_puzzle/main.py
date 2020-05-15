
import time
import sys

import numpy as np
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont

from projekat2_puzzle.mainMulti import ProtivnikWorkThread
from projekat2_puzzle.qmain import QLearningWorkThread
from projekat2_puzzle.search import AStarWorkThread
from projekat2_puzzle.puzzle import PuzzleProblem

from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QSizePolicy

from projekat2_puzzle.ui_mainwindow import Ui_MainWindow

slagalice = {
    3: [
        [2, 1, 7, 6, 3, 4, 5, 0, 8]
    ],
    4: [
        [0 , 12, 9, 13, 15, 11, 10, 14, 8, 3, 6, 2, 4, 7, 5, 1]
    ]
}

goals = {
    3: [1, 2, 3, 4, 5, 6, 7, 8, 0],
    4: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
}

font = QFont()
font.setPointSize(12)
font.setBold(True)
font.setWeight(75)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.slagalica = []
        self.dimenzije = 3

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.Obavestenje.setAlignment(Qt.AlignCenter)
        self.ui.SaProtivnikomVrednost.setAlignment(Qt.AlignCenter)

        self.astarWorker = AStarWorkThread(None)
        self.astarWorker.signal.connect(self.osvezi_slagalicu)
        self.astarWorker.setTerminationEnabled(True)


        self.protivnikWorker = ProtivnikWorkThread(None)
        self.protivnikWorker.signal.connect(self.osvezi_slagalicu_protivnik)
        self.protivnikWorker.setTerminationEnabled(True)

        self.qLearningWorker = QLearningWorkThread(None)
        self.qLearningWorker.signal.connect(self.osvezi_slagalicu_qLearning)
        self.qLearningWorker.setTerminationEnabled(True)

        self.slagalica_layout = QGridLayout(self.ui.SlagalicaContainer)
        self.slagalica_layout.setVerticalSpacing(0)

        self.ui.PretragaBezProtivnika.clicked.connect(self.show_bez)
        self.ui.PretragaSaProtivnikom.clicked.connect(self.show_sa)
        self.ui.QLearning.clicked.connect(self.show_qlearning)
        self.ui.NapraviSlagalicuButton.clicked.connect(self.napravi_slagalicu)

        self.ui.ResiBezButton.clicked.connect(self.resi_bez)
        self.ui.ResiSaButton.clicked.connect(self.resi_sa)
        self.ui.ResiQLButton.clicked.connect(self.resi_qlearning)


    def show_bez(self):
        self.protivnikWorker.terminate()
        self.qLearningWorker.terminate()

        self.ui.Obavestenje.setText("")
        self.ui.SaProtivnikomVrednost.setText("")
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_sa(self):
        self.astarWorker.terminate()
        self.qLearningWorker.terminate()

        self.ui.Obavestenje.setText("")
        self.ui.SaProtivnikomVrednost.setText("")
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_qlearning(self):
        self.astarWorker.terminate()
        self.protivnikWorker.terminate()

        self.ui.Obavestenje.setText("")
        self.ui.SaProtivnikomVrednost.setText("")
        self.ui.stackedWidget.setCurrentIndex(2)

    def napravi_slagalicu(self):
        self.astarWorker.terminate()
        self.protivnikWorker.terminate()
        self.qLearningWorker.terminate()

        self.ui.Obavestenje.setText("")
        self.ui.SaProtivnikomVrednost.setText("")

        if self.ui.stackedWidget.currentIndex() == 0:
            if self.ui.VelicinaBezPicker.currentText() == "3x3":
                self.dimenzije = 3
            else:
                self.dimenzije = 4
        elif self.ui.stackedWidget.currentIndex() == 1:
            if self.ui.VelicinaSaPicker.currentText() == "3x3":
                self.dimenzije = 3
            else:
                self.dimenzije = 4
        else:
            self.dimenzije = 3

        if len(slagalice[self.dimenzije]) == 1:
            self.slagalica = slagalice[self.dimenzije][0]
        else:
            self.slagalica = slagalice[self.dimenzije][np.random.randint(0, len(slagalice[self.dimenzije]) - 1)]

        self.isprazni_slagalicu()
        self.popuni_slagalicu()

    def osvezi_slagalicu(self, data):
        self.ui.Obavestenje.setText("")
        self.ui.SaProtivnikomVrednost.setText("")

        key = next(iter(data))

        self.ui.Obavestenje.setText(key)
        self.slagalica = data[key]
        self.isprazni_slagalicu()
        self.popuni_slagalicu()

    def osvezi_slagalicu_protivnik(self, data):
        self.ui.Obavestenje.setText("")
        self.ui.SaProtivnikomVrednost.setText("")

        key = next(iter(data))

        if key == "pobedili":
            self.ui.Obavestenje.setText("POBEDILI!")
        elif key == "izgubili":
            self.ui.Obavestenje.setText("IZGUBILI!")

        self.slagalica = data[key][0]
        self.ui.SaProtivnikomVrednost.setText((str(data[key][1])))

        self.isprazni_slagalicu()
        self.popuni_slagalicu(key)


    def osvezi_slagalicu_qLearning(self, data):
        self.ui.Obavestenje.setText("")
        key = next(iter(data))

        if key == "reseno":
            self.ui.Obavestenje.setText("RESENO!")
        else:
            self.ui.Obavestenje.setText(key)

        self.slagalica = data[key]
        self.isprazni_slagalicu()
        self.popuni_slagalicu(key)

    def isprazni_slagalicu(self):
        if self.slagalica_layout.count() != 0:
            while self.slagalica_layout.count():
                item = self.slagalica_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    pass

    def popuni_slagalicu(self, what = ""):
        for i in range(0, self.dimenzije):
            for j in range(0, self.dimenzije):
                polje = QLabel()
                if self.slagalica[self.dimenzije*i + j] == 0:
                    if what == "enemy":
                        polje.setStyleSheet("background: rgb(200,200,255)")
                    elif what == "pobedili" or what == "RESENO!":
                        polje.setStyleSheet("background: rgb(255,0,0)")
                    elif what == "izgubili":
                        polje.setStyleSheet("background: rgb(0,0,255)")
                    else:
                        polje.setStyleSheet("background: rgb(255,200,200)")
                else:
                    polje.setStyleSheet("background: rgb(220,220,220)")

                polje.setFixedSize(100, 100)
                polje.setAlignment(Qt.AlignCenter)
                polje.setText(str(self.slagalica[self.dimenzije*i + j]))
                sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                sizePolicy1.setHeightForWidth(polje.sizePolicy().hasHeightForWidth())
                polje.setSizePolicy(sizePolicy1)
                polje.setFont(font)

                self.slagalica_layout.addWidget(polje, i, j, 1, 1)

    def resi_bez(self):
        if not self.slagalica:
            return

        self.protivnikWorker.terminate()
        self.qLearningWorker.terminate()

        self.astarWorker.puzzle_problem = PuzzleProblem(self.slagalica, goals[self.dimenzije])
        self.astarWorker.start()

    def resi_sa(self):
        if not self.slagalica:
            return

        self.astarWorker.terminate()
        self.qLearningWorker.terminate()

        self.protivnikWorker.puzzle_problem = PuzzleProblem(self.slagalica, goals[self.dimenzije])
        self.protivnikWorker.iterNum = self.ui.IterNumSaPicker.value()
        self.protivnikWorker.depth = self.ui.DepthPicker.value()
        self.protivnikWorker.agent = self.ui.AgentPicker.currentText()
        self.protivnikWorker.start()

    def resi_qlearning(self):
        if not self.slagalica:
            return

        self.astarWorker.terminate()
        self.protivnikWorker.terminate()

        self.qLearningWorker.puzzle_problem = PuzzleProblem(self.slagalica, goals[self.dimenzije])
        self.qLearningWorker.iterNum = self.ui.IterNumQLPicker.value()
        self.qLearningWorker.start()

def main():

    print ("Slagalica se resava...")    #za sada samo da vidimo jel radi, kasnije dodajem PySide i gui da lepo vidimo slagalice
    start = time.time()
    #mama = aStarSearch(PuzzleProblem([0,12,9,13,15,11,10,14,8,3,6,2,4,7,5,1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]))
    end = time.time()
    print ("Proteklo vreme je " + str(end - start) + ".")
    #return mama


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
