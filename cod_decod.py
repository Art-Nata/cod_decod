import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication, QWidget


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


CODE_TABLE = [['А', 'Б', 'В', 'Г', 'Д', '', ''], ['101', '00', '1001', '110', '1110', '', '']
              ]


def phano(codes):
    for i, c1 in enumerate(codes):
        for j, c2 in enumerate(codes):
            if i != j:
                if c1.startswith(c2) or c2.startswith(c1):
                    return False
    return True


def revphano(codes):
    for i, c1 in enumerate(codes):
        for j, c2 in enumerate(codes):
            if i != j:
                if c1.endswith(c2) or c2.endswith(c1):
                    return False
    return True


class Window_Code(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('cod_decod.ui', self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(2)
        self.cod_button.clicked.connect(self.cod_mess)
        self.decod_button.clicked.connect(self.decod_mess)

        self.table_code()
        self.tableWidget.itemChanged.connect(self.item_changed)

        self.tree_btn.clicked.connect(self.tree_code)

    def cod_mess(self):
        try:
            message_new = self.lineEdit.text()
            message_cod = ''
            for i in message_new:
                message_cod += CODE_TABLE[1][CODE_TABLE[0].index(i.capitalize())]
            self.lineEdit_2.setText(message_cod)
        except ValueError:
            self.statusBar().showMessage('Неправильное сообщение')

    def item_changed(self, item):
        CODE_TABLE[item.row()][item.column()] = item.text()

    def decod_mess(self):
        code_new = self.lineEdit_2.text()

    def tree_code(self):
        self.wnd_tree = Window_tree()
        self.wnd_tree.show()

    def table_code(self):

        for i in range(7):
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(CODE_TABLE[0][i])))
            self.tableWidget.setItem(1, i, QTableWidgetItem(str(CODE_TABLE[1][i])))


class Window_tree(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_tree.ui', self)
        self.message_phano()

    def message_phano(self):
        b = [x for x in CODE_TABLE[1] if x]
        if phano(b):
            self.label_2.setText('Прямое  +')
        else:
            self.label_2.setText('Прямое  -')
        if revphano(CODE_TABLE[1]):
            self.label_3.setText('Обратное  +')
        else:
            self.label_3.setText('Обратное  -')

    def paintEvent(self, event):
        self.w = self.size().width()
        self.h = self.size().height()
        x, y = self.w // 2, 20
        h = max(list(map(len, CODE_TABLE[1])))
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_tree(qp, h, self.w // 2, 20)
        qp.end()

    def draw_tree(self, qp):

        for i in range(h):
            x_end = x_start - x_start // 2 * i + 10
            qp.drawLine(x, y, x_end, y + (self.h - 120) // 4)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window_Code()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
