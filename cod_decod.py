import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window_Code(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('cod_decod.ui', self)
        self.cod_button.clicked.connect(self.cod_mess)
        self.decod_button.clicked.connect(self.decod_mess)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.tree_btn.clicked.connect(self.tree_code)

        self.code_table = [['А', 'Б', 'В', 'Г', 'Д', '', ''],
                           ['0', '00', '1', '11', '000', '', '']
                           ]
        self.table_code()

    def cod_mess(self):
        message_new = self.lineEdit.text()
        message_cod = ''
        for i in message_new:
            message_cod += self.code_table[i.upper()]
        self.lineEdit_2.setText(message_cod)

    def item_changed(self, item):
        # Если значение в ячейке было изменено,

        self.code_table[self.titles[item.column()]] = item.text()

    def decod_mess(self):
        pass

    def tree_code(self):
        pass

    def table_code(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(2)
        for i in range(7):
            print(self.code_table[0][i])
            ggg = QTableWidgetItem(str(self.code_table[0][i]))
            #self.tableWidget.setItem(0, i, ggg)

            # self.tableWidget.setItem(1, i, QTableWidgetItem(str(self.code_table[i])))
            #print(self.code_table[keys_code_table[i]])
        #self.tableWidget.setItem(0, 0, QTableWidgetItem(str(0)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window_Code()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
