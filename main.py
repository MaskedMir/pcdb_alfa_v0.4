import sys
from select_alg import *
from interface import *


class Interface(QtWidgets.QMainWindow):     # Класс для открытия интерфейса/GUI
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.search)
        self.base_line_edit = self.ui.lineEdit

    def search(self):   # Сбор и обработка данных от пользователя
        price_pc = self.ui.lineEdit.text()      # Сбор входных данных
        pc_list = pc_selection(int(price_pc))   # Запуск поиска комплектующих
        pc_str = []
        for pc_j in pc_list:    # Цикл по обработке выходных данных
            if hasattr(pc_j, '__iter__'):
                pc_str.append(" ".join(map(str, pc_j)))
            else:
                pc_str.append(str(pc_j))
        pc_str.append(f"Цена сборки: {db_pc_list(pc_list)}")
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(pc_str)     # Вывод данных в интерфейс



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec())
