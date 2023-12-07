import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


CODE_TABLE = [['А', 'Б', 'В', 'Г', 'Д', '', ''], ['0', '00', '1', '11', '000', '', '']
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
        self.tree_btn.clicked.connect(self.tree_code)
        self.table_code()
        self.tableWidget.itemChanged.connect(self.item_changed)

    def cod_mess(self):
        message_new = self.lineEdit.text()
        message_cod = ''
        for i in message_new:
            message_cod += CODE_TABLE[1][CODE_TABLE[0].index(i.capitalize())]
        self.lineEdit_2.setText(message_cod)

    def item_changed(self, item):
        pass

    def decod_mess(self):
        code_new = self.lineEdit_2.text()

    def tree_code(self):
        pass

    def table_code(self):

        for i in range(7):
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(CODE_TABLE[0][i])))
            self.tableWidget.setItem(1, i, QTableWidgetItem(str(CODE_TABLE[1][i])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window_Code()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
