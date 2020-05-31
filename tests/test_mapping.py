from pathlib import Path

from pydmtx.mapping import MappingMatrix


def test_mapping_matrices():
    matrices = []

    for version in range(30):
        mapping = MappingMatrix(version)

        m = dict(
            zip(
                mapping.get_mapping_matrix()[0],
                _generate_labels(*MappingMatrix.size[version]),
            )
        )

        matrix = "\n".join(["".join([m.get((row, col), "EMPTY ") for col in range(mapping.ncol)]) for row in range(mapping.nrow)])

        matrices.append(matrix)

    assert "\n".join(matrices) == Path("tests/fixtures/mapping_matrices.txt").read_text().replace("\r\n", "\n")


def _generate_labels(nrow, ncol):
    return [
        f"{major + 1:3}.{minor + 1} "
        for major in range((nrow * ncol) // 8)
        for minor in range(8)
    ]
