import re
import os
import pathlib
import traceback
from datetime import datetime
import pandas as pd
import numpy as np
import pyansys
from PyQt5.QtWidgets import QTableWidgetItem

from Cells import *
from Drawers import NAngleCellsDrawer, RectangleCellsDrawer
from ResultTableHeaders import ResultTableHeaders


class CalculationParams:

    def __init__(self, rotate_angle, angle_num, volume_part, matrix_degree):
        self.rotate_angle = rotate_angle
        self.angle_num = angle_num
        self.volume_part = volume_part
        self.matrix_degree = matrix_degree

class CalculationContext:

    def __init__(self,
                 rotate_angle_start, rotate_angle_end, rotate_angle_step,
                 angle_num_start, angle_num_end, angle_num_step,
                 volume_part_start, volume_part_end, volume_part_step,
                 matrix_degree_start, matrix_degree_end, matrix_degree_step):
        self.rotate_angle_start = min(rotate_angle_start, rotate_angle_end)
        self.rotate_angle_end = max(rotate_angle_start, rotate_angle_end)
        self.rotate_angle_step = rotate_angle_step
        self.angle_num_start = min(angle_num_start, angle_num_end)
        self.angle_num_end = max(angle_num_start, angle_num_end)
        self.angle_num_step = angle_num_step
        self.volume_part_start = min(volume_part_start, volume_part_end)
        self.volume_part_end = max(volume_part_start, volume_part_end)
        self.volume_part_step = volume_part_step
        self.matrix_degree_start = min(matrix_degree_start, matrix_degree_end)
        self.matrix_degree_end = max(matrix_degree_start, matrix_degree_end)
        self.matrix_degree_step = matrix_degree_step

class Calculation:


    def __init__(self, detail_fn, load_schema_fn):
        self.results = {}
        self.detail_fn = detail_fn[0]
        self.load_schema_fn = load_schema_fn[0]

    def calculate(self, body_params, context, result_table):
        root_folder = os.getcwd() + os.sep + 'researches' + os.sep + datetime.now().strftime('%d-%m-%Y %H-%M-%S')
        count = 0
        for param in self.__calc_params(context):
            if param.angle_num < 3:
                cells = CircleCells(body_params)
            else:
                cells = NAngleCells(body_params)
                cells.angle_num = param.angle_num

            cells.columns = cells.rows = param.matrix_degree
            cells.cell_height = body_params.height
            cells.v_cells = body_params.v * param.volume_part / 100
            cells.calculation()

            result_table.setRowCount(count+1)
            result_table.setItem(count, ResultTableHeaders.ANGLE_NUM, QTableWidgetItem(str(param.angle_num)))
            result_table.setItem(count, ResultTableHeaders.ROTATE_ANGLE, QTableWidgetItem(str(param.rotate_angle)))
            result_table.setItem(count, ResultTableHeaders.VOLUME_PART, QTableWidgetItem(str(param.volume_part)))
            result_table.setItem(count, ResultTableHeaders.MATRIX_DEGREE, QTableWidgetItem(str(param.matrix_degree)))
            result_table.setItem(count, ResultTableHeaders.STATUS, QTableWidgetItem('In progress'))

            self.researchFromDetailModel(body_params, param, cells, root_folder + os.sep + str(count), result_table, count)

            count += 1



    def __calc_params(self, context):
        list = []

        for angle_num in range(context.angle_num_start, context.angle_num_end + 1, context.angle_num_step):
            for rotate_angle in range(context.rotate_angle_start, context.rotate_angle_end + 1, context.rotate_angle_step):
                for volume_part in range(context.volume_part_start, context.volume_part_end + 1, context.volume_part_step):
                    for matrix_degree in range(context.matrix_degree_start, context.matrix_degree_end + 1, context.matrix_degree_step):
                        list.append(CalculationParams(rotate_angle, angle_num, volume_part, matrix_degree))

        return list

    def researchFromDetailModel(self, body_params, calc_param, cells, research_folder, result_table, count):
        try:
            self.results[count] = [body_params, calc_param, cells, research_folder, 'IN_PROGRESS']
            ansys = self.init_ansys(research_folder)
            drawer = self.create_drawer(ansys, cells, body_params, calc_param)
            ansys.run("/ BATCH")
            ansys.run("WPSTYLE,, , , , , , , 0")
            ansys.run("/ AUX15")
            ansys.run("IOPTN, IGES, SMOOTH")
            ansys.run("IOPTN, MERGE, YES")
            ansys.run("IOPTN, SOLID, YES")
            ansys.run("IOPTN, SMALL, YES")
            ansys.run("IOPTN, GTOLER, DEFA")
            ansys.run("IGESIN, '%s','IGS','%s' ! import" % (str(pathlib.Path(self.detail_fn).stem), str(pathlib.Path(self.detail_fn).parent.absolute())))
            ansys.run("! VPLOT")
            ansys.run("FINISH")
            ansys.prep7()
            ansys.run("NUMCMP, ALL")

            res = ansys.run("*GET, KMax, VOLU,, NUM, MAX")
            start = res.index("VALUE= ") + 7
            volume_id = res[start:]

            drawer.set_cells(cells)
            drawer.draw_cells_volumes()

            ansys.run("VSBV,%s,ALL,,," % (volume_id))

            with open(file=self.load_schema_fn, mode="r", encoding="utf-8") as load_schema_commands:
                for command in load_schema_commands:
                    if not command.isspace() and command[0] != '!':
                        ansys.run(command)

            max_press = self.get_max_press(ansys)
            result_table.setItem(count, ResultTableHeaders.MAX_PRESS, QTableWidgetItem(str(max_press)))

            ansys.exit()

            result_table.setItem(count, ResultTableHeaders.STATUS, QTableWidgetItem('Finished'))
            self.results[count] = [body_params, calc_param, cells, research_folder, 'FINISHED']
        except Exception as e:
            print(traceback.format_exc())
            result_table.setItem(count, ResultTableHeaders.STATUS, QTableWidgetItem('Failed'))
            self.results[count] = [body_params, calc_param, cells, research_folder, 'IN_PROGRESS']

    def get_max_press(self, ansys):
        ansys.run("/ POST1")
        ansys.run("SET, FIRST")
        ansys.run("NSORT, S, EQV")
        ansys.run("*GET, STRESS_MAX, SORT,, MAX")
        ansys.run("STRESS_MAX")
        status = ansys.run("*STATUS, STRESS_MAX")
        start = status.index("\n STRESS_MAX")
        max_stress = re.findall('\d+\\.\d+', status[start:])[0]

        return float(max_stress)

    def init_ansys(self, root_folder):
        path = pathlib.Path(root_folder)
        path.parent.mkdir(parents=True, exist_ok=True)
        os.mkdir(root_folder)
        return pyansys.Mapdl(
            run_location=root_folder,
            interactive_plotting=True,
            override=True,
            start_timeout=600)

    def create_drawer(self, ansys, cells, body_params, calc_params):
        if (issubclass(cells.__class__, NAngleCells)):
            return NAngleCellsDrawer(body_params, calc_params.angle_num, ansys)
        elif (issubclass(cells.__class__, RectangleCells)):
            return RectangleCellsDrawer(body_params, cells.rows, ansys)

    def show_result(self, index):
        if (self.results[index][ResultIndexes.STATUS] == 'FINISHED'):
            path = self.results[index][ResultIndexes.RESEARCH_FOLDER] + os.sep + "file.rst"
            os.system("plot_result.py \"" + path + "\"")

    def show_stress_chart(self, index):
        if (self.results[index][ResultIndexes.STATUS] == 'FINISHED'):
            path = self.results[index][ResultIndexes.RESEARCH_FOLDER] + os.sep + "file.rst"
            os.system("plot_stress_chart.py \"" + path + "\"")

class ResultIndexes:
    BODY_PARAMS = 0
    CALC_PARAMS = 1
    CELLS = 2
    RESEARCH_FOLDER = 3
    STATUS = 4