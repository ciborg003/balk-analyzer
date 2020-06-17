import asyncio
import os
import pathlib
import traceback
from datetime import datetime
import subprocess
import pyansys

from Cells import *
from Drawers import NAngleCellsDrawer, RectangleCellsDrawer
from QListWidgetHashableItem import QListWidgetHashableItem


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

    def calculate(self, body_params, context, result_list):
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
            count += 1
            self.researchFromDetailModel(body_params, param, cells, root_folder + os.sep + str(count), result_list)



    def __calc_params(self, context):
        list = []

        for angle_num in range(context.angle_num_start, context.angle_num_end + 1, context.angle_num_step):
            for rotate_angle in range(context.rotate_angle_start, context.rotate_angle_end + 1, context.rotate_angle_step):
                for volume_part in range(context.volume_part_start, context.volume_part_end + 1, context.volume_part_step):
                    for matrix_degree in range(context.matrix_degree_start, context.matrix_degree_end + 1, context.matrix_degree_step):
                        list.append(CalculationParams(rotate_angle, angle_num, volume_part, matrix_degree))

        return list

    def researchFromDetailModel(self, body_params, calc_param, cells, research_folder, result_list, item=None):
        res = 'Angle num: {}, Rotate angle: {}, Volume part: {}, Matrix degree: {}. In progress'.format(
            calc_param.angle_num, calc_param.rotate_angle, calc_param.volume_part, calc_param.matrix_degree)

        if item == None:
            item = QListWidgetHashableItem(res)
            result_list.addItem(item)

        try:
            self.results[item] = [body_params, calc_param, cells, research_folder, result_list, 'IN_PROGRESS']
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

            ansys.exit()

            res = 'Angle num: {}, Rotate angle: {}, Volume part: {}, Matrix degree: {}. Finished'.format(
                calc_param.angle_num, calc_param.rotate_angle, calc_param.volume_part, calc_param.matrix_degree)
            self.results[res] = [body_params, calc_param, cells, research_folder, result_list, 'FINISHED']
            item.setText(res)
        except Exception as e:
            print(traceback.format_exc())
            res = 'Angle num: {}, Rotate angle: {}, Volume part: {}, Matrix degree: {}. Failed'.format(
                calc_param.angle_num, calc_param.rotate_angle, calc_param.volume_part, calc_param.matrix_degree)
            self.results[item] = [body_params, calc_param, cells, research_folder, result_list, 'IN_PROGRESS']
            item.setText(res)

    def buildBody(self, body_params, calc_param, cells, research_folder, result_list, item = None):
        res = 'Angle num: {}, Rotate angle: {}, Volume part: {}, Matrix degree: {}. In progress'.format(
            calc_param.angle_num, calc_param.rotate_angle, calc_param.volume_part, calc_param.matrix_degree)

        if item == None:
            item = QListWidgetHashableItem(res)
            result_list.addItem(item)

        try:
            self.results[item] = [body_params, calc_param, cells, research_folder, result_list, 'IN_PROGRESS']
            ansys = self.init_ansys(research_folder)
            drawer = self.create_drawer(ansys, cells, body_params, calc_param)
            ansys.prep7()

            opora1_x1 = body_params.foot_spacing;
            opora1_x2 = body_params.foot_spacing + body_params.footing_length
            opora1_y1 = 0;
            opora1_y2 = body_params.width
            opora1_z = -1
            opora1_point_ids = [drawer.point_service.add(opora1_x1, opora1_y1, opora1_z),
                                drawer.point_service.add(opora1_x1, opora1_y2, opora1_z),
                                drawer.point_service.add(opora1_x2, opora1_y2, opora1_z),
                                drawer.point_service.add(opora1_x2, opora1_y1, opora1_z)]
            opora1_id = drawer.plain_service.add(opora1_point_ids)

            opora2_x1 = body_params.length - (body_params.foot_spacing + body_params.footing_length);
            opora2_x2 = body_params.length - body_params.foot_spacing
            opora2_y1 = 0;
            opora2_y2 = body_params.width
            opora2_z = -1
            opora2_point_ids = [drawer.point_service.add(opora2_x1, opora2_y1, opora2_z),
                                drawer.point_service.add(opora2_x1, opora2_y2, opora2_z),
                                drawer.point_service.add(opora2_x2, opora2_y2, opora2_z),
                                drawer.point_service.add(opora2_x2, opora2_y1, opora2_z)]
            opora2_id = drawer.plain_service.add(opora2_point_ids)

            press_x1 = body_params.length/2 - 0.5
            press_x2 = body_params.length/2 + 0.5
            press_y1 = 0
            press_y2 = body_params.width
            press_z = body_params.height + 1
            press_point_ids = [drawer.point_service.add(press_x1, press_y1, press_z),
                               drawer.point_service.add(press_x1, press_y2, press_z),
                               drawer.point_service.add(press_x2, press_y2, press_z),
                               drawer.point_service.add(press_x2, press_y1, press_z)]
            press_id = drawer.plain_service.add(press_point_ids)

            drawer.set_cells(cells)

            main_plain_point_ids = [
                drawer.point_service.add(0, 0),
                drawer.point_service.add(body_params.length, 0),
                drawer.point_service.add(body_params.length, body_params.width),
                drawer.point_service.add(0, body_params.width)]

            main_plain_id = drawer.plain_service.add(main_plain_point_ids)

            result_plain_id = drawer.draw_cells_based_on_main_plain(main_plain_id)

            ansys.voffst(opora1_id, -1)
            ansys.voffst(opora2_id, -1)
            ansys.voffst(press_id, 1)
            ansys.voffst(result_plain_id, body_params.height)

            # ansys.run("ASEL, ALL")
            ansys.run("VGLUE, ALL")

            ansys.run("ASEL, ALL")
            ansys.run("DENSITY = 8.0e-6")
            ansys.run("YOUNG = 210000.0")
            ansys.run("MP, EX, 1, YOUNG")
            ansys.run("MP, NUXY, 1, 0.3")
            ansys.run("MP, DENS, 1, DENSITY")
            ansys.run("et, 1, solid186")
            ansys.run("MSHKEY, 0")
            ansys.run("MSHAPE, 1, 3d")
            ansys.run("VMESH, all")
            ansys.run("FINISH")

            ansys.run("/ SOL")
            ansys.run("FLST, 2, 2, 5, ORDE, 2")
            ansys.run("FITEM, 2, 1")
            ansys.run("FITEM, 2, -2")
            ansys.run("/ GO")
            ansys.run("DA, P51X, ALL,")
            ansys.run("FLST, 2, 1, 5, ORDE, 1")
            ansys.run("FITEM, 2, 3")
            ansys.run("/ GO")
            ansys.run("SFA, P51X, 1, PRES, 1000")
            ansys.run("! / STATUS, SOLU")
            ansys.run("SOLVE")
            ansys.run("FINISH")
            ansys.run("/ POST1")
            ansys.run("SET, FIRST")
            ansys.run("NSORT, S, EQV")
            ansys.run("*GET, STRESS_MAX, SORT,, MAX")
            ansys.run("*STATUS, STRESS_MAX")
            ansys.run("AVPRIN, 0,,")
            ansys.run("ETABLE, EVolume, VOLU,")
            ansys.run("SSUM")
            ansys.run("*GET, total_vol, SSUM,, ITEM, EVOLUME")
            ansys.run("*STATUS, total_vol")

            ansys.exit()

            res = 'Angle num: {}, Rotate angle: {}, Volume part: {}, Matrix degree: {}. Finished'.format(calc_param.angle_num, calc_param.rotate_angle, calc_param.volume_part, calc_param.matrix_degree)
            self.results[res] = [body_params, calc_param, cells, research_folder, result_list, 'FINISHED']
            item.setText(res)
        except Exception as e:
            print(traceback.format_exc())
            res = 'Angle num: {}, Rotate angle: {}, Volume part: {}, Matrix degree: {}. Failed'.format(
                calc_param.angle_num, calc_param.rotate_angle, calc_param.volume_part, calc_param.matrix_degree)
            self.results[item] = [body_params, calc_param, cells, research_folder, result_list, 'IN_PROGRESS']
            item.setText(res)


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

    def is_retry_successful(self, key):
        status = self.results[key][ResultIndexes.STATUS]

        return status == "FINISHED"

    def show_result(self, item):
        def show(path):
            res = pyansys.read_binary(path)
            res.plot_nodal_solution(0, 'x', label='Displacement')

        path = self.results[item][ResultIndexes.RESEARCH_FOLDER] + os.sep + "file.rst"
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        res = loop.run_until_complete(show(path))


    def retry_research(self, item, result_list):
        research_list = self.results[item]

        body_params = research_list[ResultIndexes.BODY_PARAMS]
        calc_params = research_list[ResultIndexes.CALC_PARAMS]
        cells = research_list[ResultIndexes.CELLS]
        research_folder = research_list[ResultIndexes.RESEARCH_FOLDER]
        self.buildBody(body_params, calc_params, cells, research_folder, result_list, self. item)



class ResultIndexes:
    BODY_PARAMS = 0
    CALC_PARAMS = 1
    CELLS = 2
    RESEARCH_FOLDER = 3
    RESULT_LIST = 4
    STATUS = 5