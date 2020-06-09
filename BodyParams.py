class BodyParameters:
    length = 0
    width = 0
    height = 0
    v = 0

    def __init__(self, width, length, height, footing_length = 0, foot_spacing=0):
        self.width = width
        self.height = height
        self.length = length
        self.v = width * height * length
        self.footing_length = footing_length
        self.foot_spacing = foot_spacing

    def get_x0_body(self):
        return 0

    def get_xend_body(self):
        return self.length

    def get_y0_body(self):
        return 0

    def get_yend_body(self):
        return self.width

    def get_z0_body(self):
        return 0

    def get_zend_body(self):
        return self.height


    def get_x0_cells(self):
        return self.foot_spacing + self.footing_length

    def get_xend_cells(self):
        return self.length - (self.foot_spacing + self.footing_length)

    def get_y0_cells(self):
        return 0

    def get_yend_cells(self):
        return self.width

    def get_z0_cells(self):
        return 0

    def get_zend_cells(self):
        return self.height

    def get_delta_foot(self):
        return self.length - 2 * (self.footing_length + self.foot_spacing)