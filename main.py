from PyQt5.QtWidgets import *
from game_core import GameCore
# from PyQt5.Qt


class FrenchGameMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.core = GameCore()
        self.stacked_wid = QStackedWidget()
        self.score_label = QLabel(str(self.core.score))
        self.word_label = QLabel()
        self.finish_label = QLabel()
        self.createActions()
        self.createMenus()

        self.start_widget = QWidget()
        self.max_score_drop_down = QComboBox()

        self.game_widget = QWidget()

        self.result_widget = QWidget()
        self.current_score_label = QLabel(str(self.core.score) + '/' + str(self.core.get_max_score()))
        self.result_label = QLabel()

        self.finish_widget = QWidget()
        self.final_result_label = QLabel()

        # if self.core.db_fail:
        #     pass
        self.init_ui_start()
        self.init_ui_game()
        self.init_ui_result()
        self.init_ui_finish()
        self.setCentralWidget(self.stacked_wid)
        self.setWindowTitle("Masculin ou féminine")
        self.setMaximumSize(400, 50)
        self.resize(400, 50)

    def init_ui_start(self):
        """
        :return: None
        """
        layout = QVBoxLayout()
        start_label = QLabel("Guess the Gender")
        start_btn = QPushButton("Start")

        self.max_score_drop_down.addItem('10')
        self.max_score_drop_down.addItem('15')
        self.max_score_drop_down.addItem('20')
        self.max_score_drop_down.addItem('25')

        start_btn.pressed.connect(self.start)
        layout.addWidget(start_label)
        layout.addWidget(self.max_score_drop_down)
        layout.addWidget(start_btn)
        self.start_widget.setLayout(layout)
        self.stacked_wid.addWidget(self.start_widget)

    def init_ui_game(self):
        """
        :return: None
        """
        layout = QGridLayout()
        m_btn = QPushButton("Masculin")
        m_btn.clicked.connect(self.clicked_mas)
        f_btn = QPushButton("féminine")
        f_btn.clicked.connect(self.clicked_fem)
        layout.addWidget(self.word_label, 0, 0, 1, 2)
        layout.addWidget(f_btn, 1, 0)
        layout.addWidget(m_btn, 1, 1)
        self.game_widget.setLayout(layout)
        self.stacked_wid.addWidget(self.game_widget)

    def init_ui_result(self):
        """
        :return: None
        """
        layout = QVBoxLayout()
        nxt_btn = QPushButton("Next")
        nxt_btn.pressed.connect(self.goto_game)
        layout.addWidget(self.result_label)
        layout.addWidget(self.current_score_label)
        layout.addWidget(nxt_btn)
        self.result_widget.setLayout(layout)
        self.stacked_wid.addWidget(self.result_widget)

    def init_ui_finish(self):
        """
        :return: None
        """
        layout = QVBoxLayout()
        restart_btn = QPushButton("Restart")
        restart_btn.pressed.connect(self.goto_start)
        layout.addWidget(self.final_result_label)
        layout.addWidget(restart_btn)
        self.finish_widget.setLayout(layout)
        self.stacked_wid.addWidget(self.finish_widget)

    def createActions(self):
        """
        :return: None
        """
        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q", triggered=self.close)
        self.aboutAct = QAction("&About", self, triggered=self.about)

    def createMenus(self):
        """
        :return: None
        """
        self.OptionsMenu = QMenu("&Options", self)
        self.OptionsMenu.addAction(self.exitAct)

        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)
        # self.helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(self.OptionsMenu)
        self.menuBar().addMenu(self.helpMenu)

    def start(self):
        max_score = int(self.max_score_drop_down.currentText())
        self.core.set_max_score(max_score)
        self.core.running = True
        self.goto_game()

    def clicked_mas(self):
        if self.core.check_answer("mas"):
            self.goto_result(True)
        else:
            self.goto_result(False)

    def clicked_fem(self):
        if self.core.check_answer("fem"):
            self.goto_result(True)
        else:
            self.goto_result(False)

    def goto_start(self):
        """
        :return: None
        """
        self.core.idx = 0
        self.core.reset_score()
        self.stacked_wid.setCurrentIndex(0)

    def goto_game(self):
        """
        :return: None
        """
        if self.core.running:
            self.core.change_current_word()
            self.word_label.setText(self.core.current_word)
            self.stacked_wid.setCurrentIndex(1)
        else:
            self.goto_finish()

    def goto_result(self, result):
        """
        :return: None
        """
        if result:
            text = "Correct!"
        else:
            text = "Incorrect.."
        self.current_score_label.setText(str(self.core.score) + '/' + str(self.core.get_max_score()))
        self.result_label.setText(text)
        self.stacked_wid.setCurrentIndex(2)

    def goto_finish(self):
        """
        :return: None
        """
        self.final_result_label.setText("Final Score:" + str(self.core.score) + '/' + str(self.core.get_max_score()))
        self.stacked_wid.setCurrentIndex(3)

    def about(self):
        """
        :return: None
        """
        QMessageBox.about(self, "About Masculin ou féminine",
                          "<p>A small game I decided to make to help me remember the gender of french words :).</p>")


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrenchGameMainWindow()
    w.show()
    sys.exit(app.exec_())
