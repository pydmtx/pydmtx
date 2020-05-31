from itertools import count, takewhile

from pydmtx.mapping import MappingMatrix

class Symbol:
    size = [
        (10, 10),
        (12, 12),
        (14, 14),
        (16, 16),
        (18, 18),
        (20, 20),
        (22, 22),
        (24, 24),
        (26, 26),
        (32, 32),
        (36, 36),
        (40, 40),
        (44, 44),
        (48, 48),
        (52, 52),
        (64, 64),
        (72, 72),
        (80, 80),
        (88, 88),
        (96, 96),
        (104, 104),
        (120, 120),
        (132, 132),
        (144, 144),
        (8, 18),
        (8, 32),
        (12, 26),
        (12, 36),
        (16, 36),
        (16, 48),
    ]

    region_size = [
        (8, 8),
        (10, 10),
        (12, 12),
        (14, 14),
        (16, 16),
        (18, 18),
        (20, 20),
        (22, 22),
        (24, 24),
        (14, 14),
        (16, 16),
        (18, 18),
        (20, 20),
        (22, 22),
        (24, 24),
        (14, 14),
        (16, 16),
        (18, 18),
        (20, 20),
        (22, 22),
        (24, 24),
        (18, 18),
        (20, 20),
        (22, 22),
        (6, 16),
        (6, 14),
        (10, 24),
        (10, 16),
        (14, 16),
        (14, 22),
    ]

    def __init__(self, version, quiet_zone=2, **options):
        nrow, ncol = Symbol.size[version]
        row_gap, column_gap = Symbol.region_size[version]

        self.nrow = nrow
        self.ncol = ncol
        self.rgap = row_gap
        self.cgap = column_gap
        self.version = version
        self.quiet_zone = quiet_zone
        self.dark = set()

        self._draw_patterns()
        self._draw_quiet_zone()

    def _draw_patterns(self):
        self._draw_horizontal_patterns()
        self._draw_vertical_patterns()

    def _draw_horizontal_patterns(self):
        for row in takewhile(lambda r: r < self.nrow, count(0, self.rgap + 2)):
            self._draw_dashed_horizontal_line(row)
            self._draw_solid_horizontal_line(row + self.rgap + 1)

    def _draw_dashed_horizontal_line(self, row):
        self.dark.update({(row, 2 * col) for col in range(0, self.ncol // 2)})

    def _draw_solid_horizontal_line(self, row):
        self.dark.update({(row, col) for col in range(0, self.ncol)})

    def _draw_vertical_patterns(self):
        for col in takewhile(lambda c: c < self.ncol, count(0, self.cgap + 2)):
            self._draw_solid_vertical_line(col)
            self._draw_dashed_vertical_line(col + self.cgap + 1)

    def _draw_solid_vertical_line(self, col):
        self.dark.update({(row, col) for row in range(0, self.nrow)})

    def _draw_dashed_vertical_line(self, col):
        self.dark.update({(2 * row + 1, col) for row in range(0, self.nrow // 2)})

    def _draw_quiet_zone(self):
        self.dark = {
            (row + self.quiet_zone, col + self.quiet_zone) for row, col in self.dark
        }

    def draw_data(self, modules):
        mm = MappingMatrix(self.version)
        mapping, remaining_area = mm.get_mapping_matrix()

        dark_modules = [module for module, is_active in zip(mapping, modules) if is_active] + remaining_area

        self.dark.update(set(self._subdivide_into_data_regions(dark_modules)))

    def _subdivide_into_data_regions(self, modules):
        rgap = self.rgap
        cgap = self.cgap

        return [((row // rgap) * (rgap + 2) + (row % rgap) + 1 + self.quiet_zone, (col // cgap) * (cgap + 2) + (col % cgap) + 1 + self.quiet_zone) for row, col in modules]

    def raw(self):
        nrow = self.nrow + 2 * self.quiet_zone
        ncol = self.ncol + 2 * self.quiet_zone
        data = [
            [(row, col) in self.dark for col in range(0, ncol)]
            for row in range(0, nrow)
        ]

        return data

    def __str__(self):
        raw = self.raw()["data"]

        return "\n".join(map(lambda row: "".join(map(lambda x: "@" if x else " ", row)), raw))
