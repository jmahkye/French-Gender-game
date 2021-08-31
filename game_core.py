from db_reader import DataBaseReader


class GameCore:
    def __init__(self):
        self._max_idx = 10
        self.idx = 0
        self.db_fail = False
        try:
            self.reader = DataBaseReader()
        except:
            self.db_fail = True
        self.score = 0
        self._current_word_dict = {'id': 0, 'name': '', 'gender': '', 'quantity': ''}
        self.current_word = ''
        self.running = False

    def change_current_word(self):
        self.running = True
        data = self.reader.get_random_row()
        self._current_word_dict['id'] = data[0]
        self._current_word_dict['name'] = data[1]
        self._current_word_dict['gender'] = data[2]
        self._current_word_dict['quantity'] = data[3]
        self.set_current_word()

    def set_max_score(self, score):
        self._max_idx = score

    def get_max_score(self):
        return self._max_idx

    def check_answer(self, answer):
        correct = False
        if answer[:3] == self._current_word_dict['gender']:
            self._add_to_score()
            correct = True
        self.set_current_word()
        self.idx += 1
        if self.idx >= self._max_idx:
            self.running = False
        return correct

    def set_current_word(self):
        self.current_word = self._current_word_dict['name']

    def _add_to_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0
