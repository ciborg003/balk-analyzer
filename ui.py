# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import typing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMutex
from PyQt5.QtWidgets import QWidget

from Calculation import CalculationContext, Calculation
from BodyParams import BodyParameters
import _thread as thread


class Ui_Dialog(object):



    def __init__(self):
        self.__mutex = QMutex()
        super().__init__()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 440)
        Dialog.setModal(False)
        self.input_angle_num_start = QtWidgets.QLineEdit(Dialog)
        self.input_angle_num_start.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.input_angle_num_start.setObjectName("input_angle_num_start")
        self.input_rotate_angle_start = QtWidgets.QLineEdit(Dialog)
        self.input_rotate_angle_start.setGeometry(QtCore.QRect(120, 130, 113, 20))
        self.input_rotate_angle_start.setObjectName("input_rotate_angle_start")
        self.input_volume_part_start = QtWidgets.QLineEdit(Dialog)
        self.input_volume_part_start.setGeometry(QtCore.QRect(120, 170, 113, 20))
        self.input_volume_part_start.setObjectName("input_volume_part_start")
        self.input_degree_start = QtWidgets.QLineEdit(Dialog)
        self.input_degree_start.setGeometry(QtCore.QRect(140, 270, 113, 20))
        self.input_degree_start.setObjectName("input_degree_start")
        self.input_degree_step = QtWidgets.QLineEdit(Dialog)
        self.input_degree_step.setGeometry(QtCore.QRect(140, 350, 113, 20))
        self.input_degree_step.setObjectName("input_degree_step")
        self.input_degree_end = QtWidgets.QLineEdit(Dialog)
        self.input_degree_end.setGeometry(QtCore.QRect(140, 310, 113, 20))
        self.input_degree_end.setObjectName("input_degree_end")
        self.input_cell_height = QtWidgets.QLineEdit(Dialog)
        self.input_cell_height.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.input_cell_height.setObjectName("input_cell_height")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 111, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(120, 70, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(270, 70, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(420, 70, 47, 13))
        self.label_7.setObjectName("label_7")
        self.input_rotate_angle_end = QtWidgets.QLineEdit(Dialog)
        self.input_rotate_angle_end.setGeometry(QtCore.QRect(270, 130, 113, 20))
        self.input_rotate_angle_end.setObjectName("input_rotate_angle_end")
        self.input_angle_num_end = QtWidgets.QLineEdit(Dialog)
        self.input_angle_num_end.setGeometry(QtCore.QRect(270, 90, 113, 20))
        self.input_angle_num_end.setObjectName("input_angle_num_end")
        self.input_volume_part_end = QtWidgets.QLineEdit(Dialog)
        self.input_volume_part_end.setGeometry(QtCore.QRect(270, 170, 113, 20))
        self.input_volume_part_end.setObjectName("input_volume_part_end")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 350, 111, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 270, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 310, 101, 20))
        self.label_10.setObjectName("label_10")
        self.input_volume_part_step = QtWidgets.QLineEdit(Dialog)
        self.input_volume_part_step.setGeometry(QtCore.QRect(420, 170, 113, 20))
        self.input_volume_part_step.setObjectName("input_volume_part_step")
        self.input_rotate_angle_step = QtWidgets.QLineEdit(Dialog)
        self.input_rotate_angle_step.setGeometry(QtCore.QRect(420, 130, 113, 20))
        self.input_rotate_angle_step.setObjectName("input_rotate_angle_step")
        self.input_angle_num_step = QtWidgets.QLineEdit(Dialog)
        self.input_angle_num_step.setGeometry(QtCore.QRect(420, 90, 113, 20))
        self.input_angle_num_step.setObjectName("input_angle_num_step")
        self.button_research = QtWidgets.QPushButton(Dialog)
        self.button_research.setGeometry(QtCore.QRect(270, 20, 261, 23))
        self.button_research.setObjectName("button_research")
        self.button_research.clicked.connect(self.research)
        self.result_list = QtWidgets.QListWidget(Dialog)
        self.result_list.setGeometry(QtCore.QRect(270, 210, 511, 200))
        self.result_list.setObjectName("result_list")
        # self.result_list.clicked.connect(self.tableClick)
        self.button_result = QtWidgets.QPushButton(Dialog)
        self.button_result.setGeometry(QtCore.QRect(20, 380, 233, 30))
        self.button_result.setObjectName("button_retry")
        self.button_result.clicked.connect(self.retry)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(620, 170, 51, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(620, 130, 51, 20))
        self.label_12.setObjectName("label_12")
        self.input_body_width = QtWidgets.QLineEdit(Dialog)
        self.input_body_width.setGeometry(QtCore.QRect(670, 130, 113, 20))
        self.input_body_width.setObjectName("input_body_width")
        self.input_body_height = QtWidgets.QLineEdit(Dialog)
        self.input_body_height.setGeometry(QtCore.QRect(670, 170, 113, 20))
        self.input_body_height.setObjectName("input_body_height")
        self.input_body_length = QtWidgets.QLineEdit(Dialog)
        self.input_body_length.setGeometry(QtCore.QRect(670, 90, 113, 20))
        self.input_body_length.setObjectName("input_body_length")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(620, 90, 51, 16))
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(590, 20, 71, 20))
        self.label_14.setObjectName("label_14")
        self.input_footing_length = QtWidgets.QLineEdit(Dialog)
        self.input_footing_length.setGeometry(QtCore.QRect(670, 20, 113, 20))
        self.input_footing_length.setObjectName("input_footing_length")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def __get_body_params(self):
        return BodyParameters(
            int(self.input_body_width.text()),
            int(self.input_body_length.text()),
            int(self.input_body_height.text()),
            int(self.input_footing_length.text()))

    def __get_calculation_context(self):
        return CalculationContext(
            int(self.input_rotate_angle_start.text()),
            int(self.input_rotate_angle_end.text()),
            int(self.input_rotate_angle_step.text()),
            int(self.input_angle_num_start.text()),
            int(self.input_angle_num_end.text()),
            int(self.input_angle_num_step.text()),
            int(self.input_volume_part_start.text()),
            int(self.input_volume_part_end.text()),
            int(self.input_volume_part_step.text()),
            int(self.input_degree_start.text()),
            int(self.input_degree_end.text()),
            int(self.input_degree_step.text()))


    def research(self):
        context = self.__get_calculation_context()
        body_params = self.__get_body_params()
        self.calculation = Calculation()
        thread.start_new_thread(self.calculation.calculate, (body_params, context, self.result_list))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.input_angle_num_start.setText(_translate("Dialog", "3"))
        self.input_rotate_angle_start.setText(_translate("Dialog", "0"))
        self.input_volume_part_start.setText(_translate("Dialog", "10"))
        self.input_degree_start.setText(_translate("Dialog", "3"))
        self.input_degree_step.setText(_translate("Dialog", "1"))
        self.input_degree_end.setText(_translate("Dialog", "5"))
        self.input_cell_height.setText(_translate("Dialog", "30"))
        self.label.setText(_translate("Dialog", "Высота ячейи"))
        self.label_2.setText(_translate("Dialog", "Количество углов"))
        self.label_3.setText(_translate("Dialog", "Угол поворота"))
        self.label_4.setText(_translate("Dialog", "Часть от объёма (%)"))
        self.label_5.setText(_translate("Dialog", "Начало"))
        self.label_6.setText(_translate("Dialog", "Конец"))
        self.label_7.setText(_translate("Dialog", "Шаг"))
        self.input_rotate_angle_end.setText(_translate("Dialog", "0"))
        self.input_angle_num_end.setText(_translate("Dialog", "5"))
        self.input_volume_part_end.setText(_translate("Dialog", "30"))
        self.label_8.setText(_translate("Dialog", "Шаг"))
        self.label_9.setText(_translate("Dialog", "Началья степень"))
        self.label_10.setText(_translate("Dialog", "Конечная степень"))
        self.input_volume_part_step.setText(_translate("Dialog", "5"))
        self.input_rotate_angle_step.setText(_translate("Dialog", "1"))
        self.input_angle_num_step.setText(_translate("Dialog", "1"))
        self.button_research.setText(_translate("Dialog", "Исследовать"))
        self.button_result.setText(_translate("Dialog", "Результат"))
        self.label_11.setText(_translate("Dialog", "Высота"))
        self.label_12.setText(_translate("Dialog", "Ширина"))
        self.input_body_width.setText(_translate("Dialog", "20"))
        self.input_body_height.setText(_translate("Dialog", "30"))
        self.input_body_length.setText(_translate("Dialog", "20"))
        self.label_13.setText(_translate("Dialog", "Длина"))
        self.label_14.setText(_translate("Dialog", "Длина опоры"))

    def tableClick(self):
        item = self.result_list.selectedItems()[0]
        self.button_result.setEnabled(self.calculation.is_retry_successful(item.text()))

    def retry(self):
        if len(self.result_list.selectedItems()) == 1:
            print("\n\n\n\n\n\n00000000000000000000000000000000")
            item = self.result_list.selectedItems()[0]
            # self.__mutex.lock()
            print("\n\n\n\n\n\n11111111111111111111111111111111")
            self.calculation.show_result(item)
            # thread.start_new_thread(self.calculation.show_result, [item])
            # self.__mutex.unlock()

class MyDialog(QtWidgets.QDialog):

    def __init__(self, parent = None):
        super().__init__(parent)

    def closeEvent(self, event: QtGui.QCloseEvent):
        print("Event: " + event)
        super(MyDialog, self).closeEvent(event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = MyDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
