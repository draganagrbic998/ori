import sys
import numpy as np
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QSizePolicy

from projekat1_puzzle.mainwindow import Ui_MainWindow
from projekat1_puzzle.puzzle import PuzzleProblem
from projekat1_puzzle.singleAgent import AStarWorkThread
from projekat1_puzzle.multiAgent import EnemyWorkThread
from projekat1_puzzle.qAgent import QLearningWorkThread

puzzles = {
    3: [
        #[2, 1, 7, 6, 3, 4, 5, 0, 8],
        #[1, 3, 7, 0, 8, 2, 5, 4, 6],
        [1, 0, 4, 2, 5, 3, 8, 7, 6],
        #[5, 2, 7, 8, 4, 0, 1, 3, 6]
    ],
    4: [
        [0,12,9,13,15,11,10,14,3,7,2,5,4,8,6,1],
        [0,12,10,13,15,11,14,9,3,7,2,5,4,8,6,1],
        [0,11,9,13,12,15,10,14,3,7,6,2,4,8,5,1],
        [0,15,9,13,11,12,10,14,3,7,6,2,4,8,5,1],
        [0,12,9,13,15,11,10,14,3,7,6,2,4,8,5,1],
        [0,12,14,13,15,11,9,10,3,7,6,2,4,8,5,1],
        [0,12,10,13,15,11,14,9,3,7,6,2,4,8,5,1],
        [0,12,11,13,15,14,10,9,3,7,6,2,4,8,5,1],
        [0,12,10,13,15,11,9,14,7,3,6,2,4,8,5,1],
        [0,12,9,13,15,11,14,10,3,8,6,2,4,7,5,1],
        [0,12,9,13,15,11,10,14,7,8,6,2,4,3,5,1],
        [0,12,9,13,15,11,10,14,8,3,6,2,4,7,5,1],
        [0,12,14,13,15,11,9,10,8,3,6,2,4,7,5,1],
        [0,12,10,13,15,11,14,9,7,8,6,2,4,3,5,1],
        [0,12,9,13,15,8,10,14,11,7,6,2,4,3,5,1],
        [0,12,9,13,15,11,10,14,3,7,5,6,4,8,2,1],
        [0,12,9,13,15,11,10,14,7,8,5,6,4,3,2,1]
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

        super().__init__()
        self.puzzle = []
        self.puzzle_size = 3

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.Obavestenje.setAlignment(Qt.AlignCenter)
        self.slagalica_layout = QGridLayout(self.ui.SlagalicaContainer)
        self.slagalica_layout.setVerticalSpacing(0)

        self.astarWorker = AStarWorkThread(None)
        self.astarWorker.signal.connect(self.refresh_astar)
        self.astarWorker.setTerminationEnabled(True)

        self.enemyWorker = EnemyWorkThread(None)
        self.enemyWorker.signal.connect(self.refresh_enemy)
        self.enemyWorker.setTerminationEnabled(True)

        self.qLearningWorker = QLearningWorkThread(None)
        self.qLearningWorker.signal.connect(self.refresh_qlearning)
        self.qLearningWorker.setTerminationEnabled(True)

        self.ui.PretragaBezProtivnika.clicked.connect(self.show_astar)
        self.ui.PretragaSaProtivnikom.clicked.connect(self.show_enemy)
        self.ui.QLearning.clicked.connect(self.show_qlearning)

        self.ui.ResiBezButton.clicked.connect(self.solve_astar)
        self.ui.ResiSaButton.clicked.connect(self.solve_enemy)
        self.ui.ResiQLButton.clicked.connect(self.solve_qlearning)

    def show_astar(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.reset_puzzle()

    def show_enemy(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.reset_puzzle()

    def show_qlearning(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.reset_puzzle()

    def refresh_astar(self, data):

        key = next(iter(data))
        self.puzzle = data[key]
        self.empty_puzzle()
        self.fill_puzzle()
        self.ui.Obavestenje.setText(key)
        self.ui.Obavestenje.setStyleSheet("color: rgb(0,0,255)")

    def refresh_enemy(self, data):

        key = next(iter(data))
        blue = True if key != "enemy" and key != "done" else False
        self.puzzle = data[key][0]
        self.empty_puzzle()
        self.fill_puzzle(blue)

        content = key if len(data[key]) <= 1 else data[key][1]
        self.ui.Obavestenje.setText(str(content))

        if key == "me" or key == "enemy":
            self.ui.Obavestenje.setStyleSheet("color: rgb(0,0,0)")
        elif key == "done":
            self.ui.Obavestenje.setStyleSheet("color: rgb(255,0,0)")
        else:
            self.ui.Obavestenje.setStyleSheet("color: rgb(0,0,255)")

    def refresh_qlearning(self, data):

        self.ui.Obavestenje.setText(data)
        self.ui.Obavestenje.setStyleSheet("color: rgb(0,0,255)")

        if "SOLVED" in data:
            self.ui.Obavestenje.setStyleSheet("color: rgb(255,0,0)")
            self.puzzle = goals[3]
            self.empty_puzzle()
            self.fill_puzzle(False)

    def solve_astar(self):

        self.reset_puzzle()
        self.astarWorker.puzzle_problem = PuzzleProblem(self.puzzle, goals[self.puzzle_size])
        self.astarWorker.start()

    def solve_enemy(self):

        self.reset_puzzle()
        self.enemyWorker.puzzle_problem = PuzzleProblem(self.puzzle, goals[self.puzzle_size])
        self.enemyWorker.iter_num = int(self.ui.IterNumSaPicker.value())
        self.enemyWorker.depth = int(self.ui.DepthPicker.value())
        self.enemyWorker.agent = self.ui.AgentPicker.currentText()
        self.enemyWorker.start()

    def solve_qlearning(self):

        self.reset_puzzle()
        self.qLearningWorker.puzzle_problem = PuzzleProblem(self.puzzle, goals[self.puzzle_size])
        self.qLearningWorker.iter_num = int(self.ui.IterNumQPicker.value())
        self.qLearningWorker.alpha = float(self.ui.alpha.value())
        self.qLearningWorker.discount = float(self.ui.discount.value())
        self.qLearningWorker.agent = self.ui.qagent.currentText()
        self.qLearningWorker.start()

    def reset_puzzle(self):

        self.astarWorker.terminate()
        self.enemyWorker.terminate()
        self.qLearningWorker.terminate()
        self.ui.Obavestenje.setText("")

        if self.ui.stackedWidget.currentIndex() == 0:
            if self.ui.VelicinaBezPicker.currentText() == "3x3":
                self.puzzle_size = 3
            else:
                self.puzzle_size = 4
        elif self.ui.stackedWidget.currentIndex() == 1:
            self.puzzle_size = 4
        else:
            self.puzzle_size = 3

        if len(puzzles[self.puzzle_size]) == 1:
            self.puzzle = puzzles[self.puzzle_size][0]
        else:
            self.puzzle = puzzles[self.puzzle_size][np.random.randint(0, len(puzzles[self.puzzle_size]) - 1)]

        self.empty_puzzle()
        self.fill_puzzle()

    def empty_puzzle(self):
        if self.slagalica_layout.count() != 0:
            while self.slagalica_layout.count():
                item = self.slagalica_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    pass

    def fill_puzzle(self, blue = True):
        for i in range(0, self.puzzle_size):
            for j in range(0, self.puzzle_size):
                field = QLabel()
                if self.puzzle[self.puzzle_size * i + j] == 0:
                    if blue:
                        field.setStyleSheet("background: rgb(0,0,255)")
                    else:
                        field.setStyleSheet("background: rgb(255,0,0)")
                else:
                    field.setStyleSheet("background: rgb(220,220,220)")

                field.setText(str(self.puzzle[self.puzzle_size * i + j]))
                field.setFixedSize(100, 100)
                field.setAlignment(Qt.AlignCenter)
                field.setFont(font)
                temp = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                temp.setHeightForWidth(field.sizePolicy().hasHeightForWidth())
                field.setSizePolicy(temp)
                self.slagalica_layout.addWidget(field, i, j, 1, 1)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
