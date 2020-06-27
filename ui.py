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
        self.__dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 500)
        Dialog.setModal(False)

        #Cells configuration form
        self.label_angle_number = QtWidgets.QLabel(Dialog)
        self.label_angle_number.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_angle_number.setObjectName("label_angle_number")
        self.label_rotate_angle = QtWidgets.QLabel(Dialog)
        self.label_rotate_angle.setGeometry(QtCore.QRect(10, 80, 81, 20))
        self.label_rotate_angle.setObjectName("label_rotate_angle")
        self.label_volume_part = QtWidgets.QLabel(Dialog)
        self.label_volume_part.setGeometry(QtCore.QRect(10, 120, 111, 20))
        self.label_volume_part.setObjectName("label_volume_part")
        self.label_start = QtWidgets.QLabel(Dialog)
        self.label_start.setGeometry(QtCore.QRect(120, 20, 47, 13))
        self.label_start.setObjectName("label_start")
        self.label_end = QtWidgets.QLabel(Dialog)
        self.label_end.setGeometry(QtCore.QRect(270, 20, 47, 13))
        self.label_end.setObjectName("label_end")
        self.label_step = QtWidgets.QLabel(Dialog)
        self.label_step.setGeometry(QtCore.QRect(420, 20, 47, 13))
        self.label_step.setObjectName("label_step")
        self.label_degree_start = QtWidgets.QLabel(Dialog)
        self.label_degree_start.setGeometry(QtCore.QRect(10, 160, 111, 20))
        self.label_degree_start.setObjectName("label_degree_start")

        self.input_angle_num_start = QtWidgets.QLineEdit(Dialog)
        self.input_angle_num_start.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.input_angle_num_start.setObjectName("input_angle_num_start")
        self.input_angle_num_end = QtWidgets.QLineEdit(Dialog)
        self.input_angle_num_end.setGeometry(QtCore.QRect(270, 40, 113, 20))
        self.input_angle_num_end.setObjectName("input_angle_num_end")
        self.input_angle_num_step = QtWidgets.QLineEdit(Dialog)
        self.input_angle_num_step.setGeometry(QtCore.QRect(420, 40, 113, 20))
        self.input_angle_num_step.setObjectName("input_angle_num_step")

        self.input_rotate_angle_start = QtWidgets.QLineEdit(Dialog)
        self.input_rotate_angle_start.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.input_rotate_angle_start.setObjectName("input_rotate_angle_start")
        self.input_rotate_angle_end = QtWidgets.QLineEdit(Dialog)
        self.input_rotate_angle_end.setGeometry(QtCore.QRect(270, 80, 113, 20))
        self.input_rotate_angle_end.setObjectName("input_rotate_angle_end")
        self.input_rotate_angle_step = QtWidgets.QLineEdit(Dialog)
        self.input_rotate_angle_step.setGeometry(QtCore.QRect(420, 80, 113, 20))
        self.input_rotate_angle_step.setObjectName("input_rotate_angle_step")

        self.input_volume_part_start = QtWidgets.QLineEdit(Dialog)
        self.input_volume_part_start.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.input_volume_part_start.setObjectName("input_volume_part_start")
        self.input_volume_part_end = QtWidgets.QLineEdit(Dialog)
        self.input_volume_part_end.setGeometry(QtCore.QRect(270, 120, 113, 20))
        self.input_volume_part_end.setObjectName("input_volume_part_end")
        self.input_volume_part_step = QtWidgets.QLineEdit(Dialog)
        self.input_volume_part_step.setGeometry(QtCore.QRect(420, 120, 113, 20))
        self.input_volume_part_step.setObjectName("input_volume_part_step")

        self.input_degree_start = QtWidgets.QLineEdit(Dialog)
        self.input_degree_start.setGeometry(QtCore.QRect(120, 160, 113, 20))
        self.input_degree_start.setObjectName("input_degree_start")
        self.input_degree_end = QtWidgets.QLineEdit(Dialog)
        self.input_degree_end.setGeometry(QtCore.QRect(270, 160, 113, 20))
        self.input_degree_end.setObjectName("input_degree_end")
        self.input_degree_step = QtWidgets.QLineEdit(Dialog)
        self.input_degree_step.setGeometry(QtCore.QRect(420, 160, 113, 20))
        self.input_degree_step.setObjectName("input_degree_step")

        #Research form
        self.button_research = QtWidgets.QPushButton(Dialog)
        self.button_research.setGeometry(QtCore.QRect(600, 275, 200, 30))
        self.button_research.setObjectName("button_research")
        self.button_research.clicked.connect(self.research)
        self.result_list = QtWidgets.QListWidget(Dialog)
        self.result_list.setGeometry(QtCore.QRect(10, 275, 525, 200))
        self.result_list.setObjectName("result_list")
        # self.result_list.clicked.connect(self.tableClick)
        self.button_result = QtWidgets.QPushButton(Dialog)
        self.button_result.setGeometry(QtCore.QRect(600, 315, 200, 30))
        self.button_result.setObjectName("button_retry")
        self.button_result.clicked.connect(self.retry)


        #Area for cells configuration
        self.label_body_z0 = QtWidgets.QLabel(Dialog)
        self.label_body_z0.setGeometry(QtCore.QRect(620, 40, 15, 20))
        self.label_body_z0.setObjectName("label_body_z0")
        self.input_body_z0 = QtWidgets.QLineEdit(Dialog)
        self.input_body_z0.setGeometry(QtCore.QRect(640, 40, 50, 20))
        self.input_body_z0.setObjectName("input_body_z0")
        self.label_body_z1 = QtWidgets.QLabel(Dialog)
        self.label_body_z1.setGeometry(QtCore.QRect(710, 40, 15, 20))
        self.label_body_z1.setObjectName("label_body_z1")
        self.input_body_z1 = QtWidgets.QLineEdit(Dialog)
        self.input_body_z1.setGeometry(QtCore.QRect(730, 40, 50, 20))
        self.input_body_z1.setObjectName("input_body_z1")

        self.label_body_y0 = QtWidgets.QLabel(Dialog)
        self.label_body_y0.setGeometry(QtCore.QRect(620, 80, 15, 20))
        self.label_body_y0.setObjectName("label_body_y0")
        self.input_body_y0 = QtWidgets.QLineEdit(Dialog)
        self.input_body_y0.setGeometry(QtCore.QRect(640, 80, 50, 20))
        self.input_body_y0.setObjectName("input_body_y0")
        self.label_body_y1 = QtWidgets.QLabel(Dialog)
        self.label_body_y1.setGeometry(QtCore.QRect(710, 80, 15, 20))
        self.label_body_y1.setObjectName("label_body_y1")
        self.input_body_y1 = QtWidgets.QLineEdit(Dialog)
        self.input_body_y1.setGeometry(QtCore.QRect(730, 80, 50, 20))
        self.input_body_y1.setObjectName("input_body_y1")

        self.label_body_x0 = QtWidgets.QLabel(Dialog)
        self.label_body_x0.setGeometry(QtCore.QRect(620, 120, 15, 16))
        self.label_body_x0.setObjectName("label_body_x0")
        self.input_body_x0 = QtWidgets.QLineEdit(Dialog)
        self.input_body_x0.setGeometry(QtCore.QRect(640, 120, 50, 20))
        self.input_body_x0.setObjectName("input_body_x0")
        self.label_body_x1 = QtWidgets.QLabel(Dialog)
        self.label_body_x1.setGeometry(QtCore.QRect(710, 120, 15, 16))
        self.label_body_x1.setObjectName("label_body_x1")
        self.input_body_x1 = QtWidgets.QLineEdit(Dialog)
        self.input_body_x1.setGeometry(QtCore.QRect(730, 120, 50, 20))
        self.input_body_x1.setObjectName("input_body_x1")

        # self.label_body_height = QtWidgets.QLabel(Dialog)
        # self.label_body_height.setGeometry(QtCore.QRect(620, 40, 51, 20))
        # self.label_body_height.setObjectName("label_body_height")
        # self.input_body_height = QtWidgets.QLineEdit(Dialog)
        # self.input_body_height.setGeometry(QtCore.QRect(670, 40, 50, 20))
        # self.input_body_height.setObjectName("input_body_height")
        #
        # self.label_body_width = QtWidgets.QLabel(Dialog)
        # self.label_body_width.setGeometry(QtCore.QRect(620, 80, 51, 20))
        # self.label_body_width.setObjectName("label_body_width")
        # self.input_body_width = QtWidgets.QLineEdit(Dialog)
        # self.input_body_width.setGeometry(QtCore.QRect(670, 80, 50, 20))
        # self.input_body_width.setObjectName("input_body_width")
        #
        # self.label_body_length = QtWidgets.QLabel(Dialog)
        # self.label_body_length.setGeometry(QtCore.QRect(620, 120, 51, 16))
        # self.label_body_length.setObjectName("label_body_length")
        # self.input_body_length = QtWidgets.QLineEdit(Dialog)
        # self.input_body_length.setGeometry(QtCore.QRect(670, 120, 50, 20))
        # self.input_body_length.setObjectName("input_body_length")

        #Input files form
        self.button_detail_file = QtWidgets.QPushButton(Dialog)
        self.button_detail_file.setGeometry(QtCore.QRect(10, 200, 200, 25))
        self.button_detail_file.setObjectName("detail_file")
        self.button_detail_file.clicked.connect(self.pick_model_file)
        self.input_detail_file = QtWidgets.QLineEdit(Dialog)
        self.input_detail_file.setGeometry(QtCore.QRect(220, 200, 315, 25))
        self.input_detail_file.setObjectName("input_detail_file")
        self.input_detail_file.setEnabled(False)

        self.button_load_schema_file = QtWidgets.QPushButton(Dialog)
        self.button_load_schema_file.setGeometry(QtCore.QRect(10, 230, 200, 25))
        self.button_load_schema_file.setObjectName("detail_file")
        self.button_load_schema_file.clicked.connect(self.pick_schema_load_file)
        self.input_load_schema_file = QtWidgets.QLineEdit(Dialog)
        self.input_load_schema_file.setGeometry(QtCore.QRect(220, 230, 315, 25))
        self.input_load_schema_file.setObjectName("input_load_schema_file")
        self.input_load_schema_file.setEnabled(False)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def __get_body_params(self):
        return BodyParameters(
            int(self.input_body_x0.text()),
            int(self.input_body_x1.text()),
            int(self.input_body_y0.text()),
            int(self.input_body_y1.text()),
            int(self.input_body_z0.text()),
            int(self.input_body_z1.text()))
        # return BodyParameters(
        #     int(self.input_body_width.text()),
        #     int(self.input_body_length.text()),
        #     int(self.input_body_z0.text()))

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

    def pick_model_file(self):
        self.__detail_file_name = QtWidgets.QFileDialog.getOpenFileName(self.__dialog, 'Open file', 'D:\\master degree\\balk-analyzer', '3D model.igs files (*.igs)')
        self.input_detail_file.setText(self.__detail_file_name[0])

    def pick_schema_load_file(self):
        self.__schema_load_file_name = QtWidgets.QFileDialog.getOpenFileName(self.__dialog, 'Open file', 'D:\\master degree\\balk-analyzer', '(*.*)')
        self.input_load_schema_file.setText(self.__schema_load_file_name[0])

    def research(self):
        context = self.__get_calculation_context()
        body_params = self.__get_body_params()
        self.calculation = Calculation(self.__detail_file_name, self.__schema_load_file_name)
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
        self.label_angle_number.setText(_translate("Dialog", "Количество углов"))
        self.label_rotate_angle.setText(_translate("Dialog", "Угол поворота"))
        self.label_volume_part.setText(_translate("Dialog", "Часть от объёма (%)"))
        self.label_start.setText(_translate("Dialog", "Начало"))
        self.label_end.setText(_translate("Dialog", "Конец"))
        self.label_step.setText(_translate("Dialog", "Шаг"))
        self.input_rotate_angle_end.setText(_translate("Dialog", "0"))
        self.input_angle_num_end.setText(_translate("Dialog", "5"))
        self.input_volume_part_end.setText(_translate("Dialog", "30"))
        self.label_degree_start.setText(_translate("Dialog", "Началья степень"))
        self.input_volume_part_step.setText(_translate("Dialog", "5"))
        self.input_rotate_angle_step.setText(_translate("Dialog", "1"))
        self.input_angle_num_step.setText(_translate("Dialog", "1"))
        self.button_research.setText(_translate("Dialog", "Исследовать"))
        self.button_result.setText(_translate("Dialog", "Результат"))
        # self.label_body_height.setText(_translate("Dialog", "Высота"))
        # self.label_body_width.setText(_translate("Dialog", "Ширина"))
        # self.input_body_width.setText(_translate("Dialog", "10"))
        # self.input_body_height.setText(_translate("Dialog", "10"))
        # self.input_body_length.setText(_translate("Dialog", "10"))
        # self.label_body_length.setText(_translate("Dialog", "Длина"))

        self.label_body_z0.setText(_translate("Dialog", "Z0"))
        self.input_body_z0.setText(_translate("Dialog", "0"))
        self.label_body_x0.setText(_translate("Dialog", "X0"))
        self.input_body_x0.setText(_translate("Dialog", "0"))
        self.label_body_y0.setText(_translate("Dialog", "Y0"))
        self.input_body_y0.setText(_translate("Dialog", "0"))
        self.label_body_z1.setText(_translate("Dialog", "Z0"))
        self.input_body_z1.setText(_translate("Dialog", "10"))
        self.label_body_x1.setText(_translate("Dialog", "X0"))
        self.input_body_x1.setText(_translate("Dialog", "10"))
        self.label_body_y1.setText(_translate("Dialog", "Y0"))
        self.input_body_y1.setText(_translate("Dialog", "10"))

        self.button_detail_file.setText(_translate("Dialog", "Файл детали"))
        self.button_load_schema_file.setText(_translate("Dialog", "Файл схемы нагрузки"))

    def tableClick(self):
        item = self.result_list.selectedItems()[0]
        self.button_result.setEnabled(self.calculation.is_retry_successful(item.text()))

    def retry(self):
        if len(self.result_list.selectedItems()) == 1:
            item = self.result_list.selectedItems()[0]
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
