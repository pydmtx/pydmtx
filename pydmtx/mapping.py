class MappingMatrix:
    size = [
        (8, 8),
        (10, 10),
        (12, 12),
        (14, 14),
        (16, 16),
        (18, 18),
        (20, 20),
        (22, 22),
        (24, 24),
        (28, 28),
        (32, 32),
        (36, 36),
        (40, 40),
        (44, 44),
        (48, 48),
        (56, 56),
        (64, 64),
        (72, 72),
        (80, 80),
        (88, 88),
        (96, 96),
        (108, 108),
        (120, 120),
        (132, 132),
        (6, 16),
        (6, 28),
        (10, 24),
        (10, 32),
        (14, 32),
        (14, 44),
    ]


    def __init__(self, version):
        nrow, ncol = MappingMatrix.size[version]

        self.nrow = nrow
        self.ncol = ncol
        self.version = version


    def get_mapping_matrix(self):
        mapping = []
        occupied = set()

        for module in self._generate_placement_path():
            if module not in occupied:
                modules = [self._module(row, col) for row, col in self._shape(*module)]

                occupied.update(set(modules))
                mapping.extend(modules)

        if (self.nrow, self.ncol) in {(10, 10), (14, 14), (18, 18), (22, 22)}:
            remaining_area = [(self.nrow - 1, self.ncol - 1), (self.nrow - 2, self.ncol - 2)]
        else:
            remaining_area = []

        return mapping, remaining_area


    def _generate_placement_path(self):
        row, col, direction = 4, 0, "right"

        while row < self.nrow or col < self.ncol:
            yield row, col

            if direction == "right":
                if row - 2 >= 0 and col + 2 < self.ncol:
                    row, col, direction = row - 2, col + 2, "right"
                else:
                    row, col, direction = row - 1, col + 5, "left"
            else:
                if row + 2 < self.nrow and col - 2 >= 0:
                    row, col, direction = row + 2, col - 2, "left"
                else:
                    row, col, direction = row + 5, col - 1, "right"


    def _shape(self, row, col):
        if row == self.nrow and col == 0:
            return [
                (self.nrow - 1, 0),
                (self.nrow - 1, 1),
                (self.nrow - 1, 2),
                (0, self.ncol - 2),
                (0, self.ncol - 1),
                (1, self.ncol - 1),
                (2, self.ncol - 1),
                (3, self.ncol - 1),
            ]
        elif row == self.nrow - 2 and col == 0 and (self.ncol % 4) != 0:
            return [
                (self.nrow - 3, 0),
                (self.nrow - 2, 0),
                (self.nrow - 1, 0),
                (0, self.ncol - 4),
                (0, self.ncol - 3),
                (0, self.ncol - 2),
                (0, self.ncol - 1),
                (1, self.ncol - 1),
            ]
        elif row == self.nrow - 2 and col == 0 and (self.ncol % 8) == 4:
            return [
                (self.nrow - 3, 0),
                (self.nrow - 2, 0),
                (self.nrow - 1, 0),
                (0, self.ncol - 2),
                (0, self.ncol - 1),
                (1, self.ncol - 1),
                (2, self.ncol - 1),
                (3, self.ncol - 1),
            ]
        elif row == self.nrow + 4 and col == 2 and (self.ncol % 8) == 0:
            return [
                (self.nrow - 1, 0),
                (self.nrow - 1, self.ncol - 1),
                (0, self.ncol - 3),
                (0, self.ncol - 2),
                (0, self.ncol - 1),
                (1, self.ncol - 3),
                (1, self.ncol - 2),
                (1, self.ncol - 1),
            ]
        elif 0 <= row < self.nrow and 0 <= col < self.ncol:
            return [
                (row - 2, col - 2),
                (row - 2, col - 1),
                (row - 1, col - 2),
                (row - 1, col - 1),
                (row - 1, col),
                (row, col - 2),
                (row, col - 1),
                (row, col),
            ]

        return []


    def _module(self, row, col):
        if row < 0:
            return self._module(row + self.nrow, col + 4 - (self.nrow + 4) % 8)
        elif col < 0:
            return self._module(row + 4 - (self.ncol + 4) % 8, col + self.ncol)
        else:
            return (row, col)
