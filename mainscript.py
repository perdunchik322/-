import sqlite3
import datetime
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableView,
                             QVBoxLayout, QWidget, QPushButton,
                             QLineEdit, QHBoxLayout, QHeaderView,
                             QMessageBox, QDialog, QLabel, QComboBox)
from PyQt6.QtCore import Qt, QSortFilterProxyModel
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QAction
from PyQt6 import QtCore, QtGui, QtWidgets
import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_screen = QtWidgets.QWidget()
        self.main_screen.setObjectName("main_screen")
        self.main_tabs = QtWidgets.QTabWidget(parent=self.main_screen)
        self.main_tabs.setGeometry(QtCore.QRect(10, 50, 1791, 761))
        self.main_tabs.setObjectName("main_tabs")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableView_of_tasks = QtWidgets.QTableView(parent=self.tab_3)
        self.tableView_of_tasks.setGeometry(QtCore.QRect(0, 40, 1791, 691))
        self.tableView_of_tasks.setObjectName("tableView_of_tasks")
        self.widget = QtWidgets.QWidget(parent=self.tab_3)
        self.widget.setGeometry(QtCore.QRect(10, 10, 856, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Add_task_button = QtWidgets.QPushButton(parent=self.widget)
        self.Add_task_button.setObjectName("Add_task_button")
        self.horizontalLayout_5.addWidget(self.Add_task_button)
        self.Delete_task_button = QtWidgets.QPushButton(parent=self.widget)
        self.Delete_task_button.setObjectName("Delete_task_button")
        self.horizontalLayout_5.addWidget(self.Delete_task_button)
        self.rewrite_task_button = QtWidgets.QPushButton(parent=self.widget)
        self.rewrite_task_button.setObjectName("rewrite_task_button")
        self.horizontalLayout_5.addWidget(self.rewrite_task_button)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.filter_button = QtWidgets.QPushButton(parent=self.widget)
        self.filter_button.setObjectName("filter_button")
        self.horizontalLayout_6.addWidget(self.filter_button)
        self.filter_subject = QtWidgets.QLineEdit(parent=self.widget)
        self.filter_subject.setObjectName("filter_subject")
        self.horizontalLayout_6.addWidget(self.filter_subject)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.filter_priority = QtWidgets.QComboBox(parent=self.widget)
        self.filter_priority.setObjectName("filter_priority")
        self.filter_priority.addItem("")
        self.filter_priority.addItem("")
        self.filter_priority.addItem("")
        self.filter_priority.addItem("")
        self.horizontalLayout_6.addWidget(self.filter_priority)
        self.main_tabs.addTab(self.tab_3, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.main_tabs.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.main_tabs.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(parent=self.main_screen)
        self.label.setGeometry(QtCore.QRect(20, 20, 431, 18))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(parent=self.main_screen)
        self.layoutWidget.setGeometry(QtCore.QRect(1620, 30, 185, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lessons_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.lessons_button.setObjectName("lessons_button")
        self.horizontalLayout_4.addWidget(self.lessons_button)
        self.settings_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.settings_button.setObjectName("settings_button")
        self.horizontalLayout_4.addWidget(self.settings_button)
        self.stackedWidget.addWidget(self.main_screen)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.page_7)
        self.lineEdit.setGeometry(QtCore.QRect(80, 60, 561, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.page_7)
        self.layoutWidget1.setGeometry(QtCore.QRect(1610, 30, 190, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back_button = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_2.addWidget(self.back_button)
        self.lessons_button_2 = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.lessons_button_2.setObjectName("lessons_button_2")
        self.horizontalLayout_2.addWidget(self.lessons_button_2)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.page_8)
        self.layoutWidget2.setGeometry(QtCore.QRect(1600, 30, 196, 28))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.back_button_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.back_button_2.setObjectName("back_button_2")
        self.horizontalLayout_3.addWidget(self.back_button_2)
        self.settings_button_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.settings_button_2.setObjectName("settings_button_2")
        self.horizontalLayout_3.addWidget(self.settings_button_2)
        self.stackedWidget.addWidget(self.page_8)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.main_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_tabs.setToolTip(_translate("MainWindow", "<html><head/><body><p>выф</p></body></html>"))
        self.Add_task_button.setText(_translate("MainWindow", "+Добавить"))
        self.Delete_task_button.setText(_translate("MainWindow", "Удалить"))
        self.rewrite_task_button.setText(_translate("MainWindow", "Перезаписать"))
        self.filter_button.setText(_translate("MainWindow", "Фильтр по предмету:"))
        self.label_3.setText(_translate("MainWindow", "По приоритету"))
        self.filter_priority.setItemText(0, _translate("MainWindow", "Высокий"))
        self.filter_priority.setItemText(1, _translate("MainWindow", "Средний"))
        self.filter_priority.setItemText(2, _translate("MainWindow", "Низкий"))
        self.filter_priority.setItemText(3, _translate("MainWindow", "Любой"))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab_3), _translate("MainWindow", "Все задания"))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab_1), _translate("MainWindow", "Сегодня"))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab_2), _translate("MainWindow", "На неделю"))
        self.label.setText(_translate("MainWindow", "Учебный планировщик 0.1v"))
        self.lessons_button.setText(_translate("MainWindow", "Предметы"))
        self.settings_button.setText(_translate("MainWindow", "Настройки"))
        self.lineEdit.setText(_translate("MainWindow", "А я тут притаился"))
        self.back_button.setText(_translate("MainWindow", "Назад"))
        self.lessons_button_2.setText(_translate("MainWindow", "Предметы"))
        self.back_button_2.setText(_translate("MainWindow", "Назад"))
        self.settings_button_2.setText(_translate("MainWindow", "Настройки"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        self.initUi()

    def initUi(self):
        self.base()  # Создание базы основных заданий
        self.Add_task_button.clicked.connect(self.add_task)  # Подключаем сигнал кнопки добавления задания
        self.Delete_task_button.clicked.connect(self.delete_task)  # Подключаем сигнал кнопки удаления задания
        self.rewrite_task_button.clicked.connect(self.rewrite_task)  # Подключаем сигнал кнопки перезаписи
        self.filter_button.clicked.connect(self.filter)  # Подключаем сигнал кнопки фильтрации
        self.navigation()  # Отдельная функция для навигации по стеку
        self.init_main_table()  # Иницилизирование модели таблицы

    def base(self):
        con = sqlite3.connect("all_tasks.db")
        cur = con.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS all_tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        task TEXT,
        deadline DATE,
        priority TEXT,
        stat TEXT)
        """)

    def init_main_table(self):
        con = sqlite3.connect("all_tasks.db")
        cur = con.cursor()

        # модель данных
        self.model_of_main = QStandardItemModel(0, 5)
        self.model_of_main.setHorizontalHeaderLabels(["Предмет", "Задание", "Дедлайн", "Приоритет", "Статус"])

        # Прокси-модель для фильтрации
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model_of_main)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        # Модель в таблицу
        self.tableView_of_tasks.setModel(self.proxy_model)
        self.tableView_of_tasks.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)

        # Настройка внешнего вида таблицы
        header = self.tableView_of_tasks.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableView_of_tasks.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

        # Выполняем запрос
        result = cur.execute("""SELECT * FROM all_tasks""")
        rows = result.fetchall()
        # Заполняем модель данными
        for row_index, row_data in enumerate(rows):
            for col_index, cell_data in enumerate(row_data):
                item = QStandardItem(str(cell_data))
                self.model_of_main.setItem(row_index, col_index - 1, item)

        con.commit()
        con.close()

    def add_task(self):
        con = sqlite3.connect("all_tasks.db")
        cur = con.cursor()
        dialog = AddTaskDialog(self)
        result = dialog.exec()
        try:
            if result == QDialog.DialogCode.Accepted:  # Проверяем сработала ли кнопка в окне
                line = str(dialog.line_edit.text()).split(", ")
                pattern = r'^\d{2}\.\d{2}\.\d{2}$'
                if len(line) < 3 or not re.match(pattern, line[2]):  # регулярное выражение для проверки формата даты
                    raise ValueError
                if len(line) >= 3:
                    items = [
                        QStandardItem(line[0]),
                        QStandardItem(line[1]),
                        QStandardItem(line[2]),
                        QStandardItem(dialog.priority.currentText()),
                        QStandardItem("Не выполнено")
                    ]
                    self.model_of_main.appendRow(items)  # Приписываем строки, которые добавили
                cur.execute("INSERT INTO all_tasks(subject, task, deadline, priority, stat) VALUES(?, ?, ?, ?, ?)", (
                    line[0], line[1], line[2], dialog.priority.currentText(), "Не выполнено"
                ))
        except ValueError:
            QMessageBox.critical(None, "Ошибка добавления", "Неправильный формат ввода")
        finally:
            con.commit()

    def delete_task(self):  # Удаление задания из таблицы и базы данных
        try:
            dialog = DeleteTaskDialog(self)
            result = dialog.exec()
            con = sqlite3.connect("all_tasks.db")
            if result == QDialog.DialogCode.Accepted:  # Проверили нажали-ли на кнопку "Удалить"
                line = []
                for column in range(self.model_of_main.columnCount()):
                    index = self.model_of_main.index(int(dialog.line_edit.text()) - 1, column)
                    value = self.model_of_main.data(index)
                    line.append(value)
                self.model_of_main.removeRow(int(dialog.line_edit.text()) - 1)
                subject, task, deadline, priority, status = line
                # Удаляем из базы данных
                deliting = "DELETE FROM all_tasks WHERE subject = ? AND task = ? AND deadline = ? AND priority = ? AND stat = ?"
                con.execute(deliting, (subject, task, deadline, priority, status))
        except ValueError:
            QMessageBox.critical(None, "Ошибка удаления", "Неправильный ввод номера")
        finally:
            con.commit()
            con.close()

    # Дописать QmessageBox
    def rewrite_task(self):  # Перезапись строк в модели и в базе
        dialog = RewriteTaskDialog(self)
        result = dialog.exec()
        con = sqlite3.connect("all_tasks.db")
        cur = con.cursor()
        inp = str(dialog.line_edit.text()).split(", ")
        if result == QDialog.DialogCode.Accepted:  # то что в таблице до редактирования
            line = []
            for column in range(self.model_of_main.columnCount()):
                index = self.model_of_main.index(int(inp[0]) - 1, column)
                value = self.model_of_main.data(index)
                line.append(value)
            pr_subject, pr_task, pr_deadline, pr_priority, pr_stat = line  # Старые значения строки в бд
            # заполнение таблицы новыми данными
            line = str(dialog.line_edit.text()).split(", ")
            row = int(line[0])
            for i in range(self.model_of_main.columnCount() - 2):
                index = self.model_of_main.index(row - 1, i)  # строка-1, столбец i
                self.model_of_main.setData(index, line[i + 1])  # изменение данных по индексу
            index = self.model_of_main.index(row - 1, 3)
            self.model_of_main.setData(index, dialog.priority.currentText())
            index = self.model_of_main.index(row - 1, 4)
            self.model_of_main.setData(index, dialog.status.currentText())
        # Перезаписываем в бд
        updater = """
        UPDATE all_tasks 
        SET subject = ?, task = ?, deadline = ?, priority = ?, stat = ? 
        WHERE subject = ? AND task = ? AND deadline = ? AND priority = ? AND stat = ?
        """
        cur.execute(updater, (
            line[1],  # новый subject
            line[2],  # новый task
            line[3],  # новый deadline
            dialog.priority.currentText(),  # новый priority
            dialog.status.currentText(),  # новый stat
            pr_subject,
            pr_task,
            pr_deadline,
            pr_priority,
            pr_stat
        ))
        con.commit()

    def filter(self):
        self.model_of_main.clear()  # отчищаем табл от всех заданий
        self.model_of_main.setHorizontalHeaderLabels(
            ["Предмет", "Задание", "Дедлайн", "Приоритет", "Статус"])  # Ставим заголовки т.к. они тоже очистились
        con = sqlite3.connect("all_tasks.db")
        cur = con.cursor()
        if self.filter_priority.currentText() == "Любой":
            needs = self.filter_subject.text()  # Фильтр тех что нужны
            # Выполняем запрос с условием отделения
            finder = """SELECT * FROM all_tasks WHERE subject = ?"""
            result = cur.execute(finder, (needs,))
            rows = result.fetchall()
        else:
            needs = [self.filter_subject.text(), self.filter_priority.currentText()]  # Фильтр тех что нужны
            # Выполняем запрос с условием отделения
            finder = """SELECT * FROM all_tasks WHERE subject = ? AND priority = ?"""
            result = cur.execute(finder, (needs[0], needs[1]))
            rows = result.fetchall()
            # Заполняем модель данными
        for row_index, row_data in enumerate(rows):
            for col_index, cell_data in enumerate(row_data):
                item = QStandardItem(str(cell_data))
                self.model_of_main.setItem(row_index, col_index - 1, item)

    def logger(self):
        pass  # В разработке

    def navigation(self):  # подключение кнопок навигации по стеку
        self.settings_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.settings_button_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.lessons_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.lessons_button_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.back_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.back_button_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))


# Модальное окно для добавления задания
class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        layout = QVBoxLayout(self)
        self.ask = QLabel(
            'Введите задание в таком формате:Предмет, Текст задания, Дедлайн(dd.mm.yy). И выберите приоритет')
        input_layout = QHBoxLayout()
        self.line_edit = QLineEdit()
        self.priority = QComboBox()
        self.priority.addItem("Высокий")
        self.priority.addItem("Средний")
        self.priority.addItem("Низкий")
        input_layout.addWidget(self.line_edit)
        input_layout.addWidget(self.priority)
        self.add_button = QPushButton("Добавить")
        layout.addWidget(self.ask)
        layout.addLayout(input_layout)
        layout.addWidget(self.add_button)

        self.add_button.clicked.connect(self.accept)


# Модальное окно для удаления задания
class DeleteTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        layout = QVBoxLayout(self)
        self.ask = QLabel("Введите номер задания, которое хотите удалить")
        self.line_edit = QLineEdit()
        self.del_button = QPushButton("Удалить")

        layout.addWidget(self.ask)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.del_button)

        self.del_button.clicked.connect(self.accept)


# Модальное окно для перезаписи
class RewriteTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        layout = QVBoxLayout(self)
        self.ask = QLabel(
            "Введите номер и новое задание в таком формате:номер, Предмет, Текст задания, Дедлайн(dd.mm.yy). И выберите приоритет и статус")
        input_layout = QHBoxLayout()
        self.line_edit = QLineEdit()
        self.priority = QComboBox()
        self.priority.addItem("Высокий")
        self.priority.addItem("Средний")
        self.priority.addItem("Низкий")
        self.status = QComboBox()
        self.status.addItem("Выполнено")
        self.status.addItem("Не выполнено")
        input_layout.addWidget(self.line_edit)
        input_layout.addWidget(self.priority)
        input_layout.addWidget(self.status)
        self.add_button = QPushButton("Перезаписать")
        layout.addWidget(self.ask)
        layout.addLayout(input_layout)
        layout.addWidget(self.add_button)

        self.add_button.clicked.connect(self.accept)


if __name__ == "__main__":  # показываем главное окно
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
