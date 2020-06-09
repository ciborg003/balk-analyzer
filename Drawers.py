import math

class AbstractNAngleDrawers:

    def __init__(self, body, angle, ansys):
        self.__ansys = ansys
        self.point_service = PointService(self.__ansys)
        self.line_service = LineService(self.__ansys)
        self.plane_service = PlaneService(self.line_service, self.__ansys)

        self._body = body
        self._deflection_angle = angle * math.pi / 180

    def subtract_plane(self, points, plane_id):
        point_ids = []
        for point in points:
            point_ids.append(self.point_service.add(point["x"], point["y"]))

        removed_plane_id = self.plane_service.add(point_ids)
        return self.plane_service.remove_plane_from_plane(plane_id, removed_plane_id)

    def calc_points(self, x0, y0, x_end, y_end, n):
        angle_0 = math.atan2(y_end - y0, x_end - x0)
        points = []
        r = math.sqrt((x_end - x0) ** 2 + (y_end - y0) ** 2)
        for i in range(n):
            angle = 2 * math.pi * i / n + angle_0
            x = r * math.cos(angle) + x0
            y = r * math.sin(angle) + y0

            points.append({"x": x, "y": y})

        return points

    def draw_cells(self, plane_id):
        pass

    def set_cells(self, cells):
        self._cells = cells

    def get_deflection(self):
        return self._deflection_angle

class NAngleCellsDrawer(AbstractNAngleDrawers):

    def __init__(self, body, angle, ansys):
        super().__init__(body, angle, ansys)

    def draw_cells(self, plane_id):
        result_plane_id = plane_id

        # Distance between cells in X and Y
        # len_x = (self._body.length - 2 * self._cells.radius * self._cells.columns) / (self._cells.columns + 1)
        available_body_len = self._body.get_xend_cells() - self._body.get_x0_cells()
        len_x = (available_body_len - 2 * self._cells.radius * self._cells.columns) / (self._cells.columns + 1)
        len_y = (self._body.width - 2 * self._cells.radius * self._cells.rows) / (self._cells.rows + 1)

        for i in range(0, self._cells.rows):
            current_y = (i + 1) * len_y + (2 * i + 1) * self._cells.radius

            for j in range(0, self._cells.columns):
                # current_x = (j + 1) * len_x + (2 * j + 1) * self._cells.radius
                current_x = self._body.get_x0_cells() + (j + 1) * len_x + (2 * j + 1) * self._cells.radius
                points = self.calc_points_for_n_angle_cell_at_coordinate(current_x, current_y)

                result_plane_id = self.subtract_plane(points, result_plane_id)

        return result_plane_id

    # x0 and y0 are center of the figure
    def calc_points_for_n_angle_cell_at_coordinate(self, x0, y0):
        delta_angle = 2 * math.pi / self._cells.angle_num
        rotate_angle_rad = self._cells.rotation_angle * math.pi / 180

        points = []

        current_angle = 0
        while current_angle < 2 * math.pi:
            x = x0 + self._cells.radius * math.cos(current_angle + rotate_angle_rad)
            y = y0 + self._cells.radius * math.sin(current_angle + rotate_angle_rad)

            current_angle += delta_angle

            points.append({"x": x, "y": y})

        if (points[0]["x"] == points[len(points) - 1]["x"]) and (points[0]["y"] == points[len(points) - 1]["y"]):
            points.pop(len(points) - 1)
        return points



class RectangleCellsDrawer(AbstractNAngleDrawers):

    def __init__(self, body, angle, ansys):
        super().__init__(body, angle, ansys)

    def draw_cells(self, plane_id):
        result_plane_id = plane_id

        len_x = (self._body.length - self._cells.cell_length * self._cells.columns) / (self._cells.columns + 1)
        len_y = (self._body.width - self._cells.cell_width * self._cells.rows) / (self._cells.rows + 1)

        for i in range(1, self._cells.rows + 1):
            for j in range(1, self._cells.columns + 1):

                x0_j = j * len_x + (j - 1) * self._cells.cell_length
                x1_j = j * (len_x + self._cells.cell_length)

                y0_i = i * len_y + (i - 1) * self._cells.cell_width
                y1_i = i * (len_y + self._cells.cell_width)

                points = [
                    {"x": x0_j, "y": y0_i},
                    {"x": x0_j, "y": y1_i},
                    {"x": x1_j, "y": y1_i},
                    {"x": x1_j, "y": y0_i}
                ]

                result_plane_id = self.subtract_plane(points, result_plane_id)

        return result_plane_id

        # x_current = (-self._body.width) / 2.0 + (self.cell_obj.k + self.cell_obj.cell_width / 2.0)
        # y_current = (self._body.length / 2.0) - (self.cell_obj.k + (self.cell_obj.cell_length / 2.0))
        # x_end = ((-self._body.width) / 2.0) + (self.cell_obj.k + self.cell_obj.cell_width)
        # y_end = (self._body.length / 2.0) - (self.cell_obj.k + self.cell_obj.cell_length)
        #
        # leftHoleCenterX = x_current
        # leftHoleCenterY = y_current
        #
        # delta = self.cell_obj.cell_width + self.cell_obj.k
        #
        # row = self.cell_obj.rows
        # column = self.cell_obj.columns
        #
        # for i in range(row):
        #     points = self.calc_points(x_current, y_current, x_end, y_end, 4)
        #     result_plane_id = self.subtract_plane(points, result_plane_id)
        #
        #     for j in range(1, column):
        #         x_current += delta
        #         x_end += delta
        #         points = self.calc_points(x_current, y_current, x_end, y_end, 4)
        #         result_plane_id = self.subtract_plane(points, result_plane_id)
        #
        #     x_current = leftHoleCenterX
        #     y_current = leftHoleCenterY - (self.cell_obj.k + self.cell_obj.cell_length)
        #     leftHoleCenterX = x_current
        #     leftHoleCenterY = y_current
        #
        #     x_end = x_current + self.cell_obj.cell_width / 2.0
        #     y_end = y_current + self.cell_obj.cell_length / 2.0
        #
        # return result_plane_id

    def set_cells(self, cells):
        self._cells = cells


class PointService:
    __id = 0

    def __init__(self, ansys):
        self.__ansys = ansys
        super().__init__()

    def add(self, x0, y0, z0=0):
        if (self.__id > 0):
            res = self.__ansys.run("*GET, KMax, Kp,, NUM, MAX")
            start = res.index("VALUE= ") + 7
            max = res[start:]
            self.__id = int(float(max))

        self.__id += 1

        self.__ansys.k(self.__id, x0, y0, z0)

        return self.__id

class LineService:
    __id = 0

    def __init__(self, ansys):
        self.__ansys = ansys
        super().__init__()

    def add(self, point1, point2):
        if (self.__id > 0):
            res = self.__ansys.run("*GET, KMax, LINE,, NUM, MAX")
            start = res.index("VALUE= ") + 7
            max = res[start:]
            self.__id = int(float(max))

        self.__id += 1
        self.__ansys.l(point1, point2)
        return self.__id

class PlaneService:
    __id = 0
    __used_ids = set()

    def __init__(self, line_service, ansys):
        self.__line_service = line_service
        self.__ansys = ansys
        super().__init__()

    def add(self, points):
        lines = []
        for i in range(len(points)):
            if (i < len(points) - 1):
                line_id = self.__line_service.add(points[i], points[i+1])
            else:
                line_id = self.__line_service.add(points[i], points[0])
            lines.append(line_id)

        command = "AL,%s" % (", ".join([str(line_id) for line_id in lines]))
        self.__ansys.run(command)
        return self.__get_id()

    def remove_plane_from_plane(self, plane_id, removed_plane_id):
        self.__ansys.asba(plane_id, removed_plane_id)

        id = self.__get_id()
        self.__used_ids.remove(plane_id)
        self.__used_ids.remove(removed_plane_id)

        return id

    def get_max_id(self):
        res = self.__ansys.run("*GET, KMax, AREA,, NUM, MAX")
        start = res.index("VALUE= ") + 7
        max = res[start:]
        return max

    def __get_id(self):
        difference = set(range(1, self.__id + 1)).difference(self.__used_ids)

        if len(difference) == 0:
            self.__id += 1
            id = self.__id
        else:
            id = min(difference)

        self.__used_ids.add(id)
        return id