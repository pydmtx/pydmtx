from pathlib import Path
from setuptools import setup, find_packages

long_description = Path("README.md").read_text()

setup(
    name="pydmtx",
    version="0.1.0",
    description="todo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mariusz Gumienny",
    author_email="mkgumienny@gmail.com",
    url="https://github.com/0x8b/pydmtx",
    py_modules=["pydmtx"],
    tests_require=[
        "pytest",
    ],
    classifiers=[
        "Topic :: Text Processing :: General",
        "Operating System :: OS Independent"
    ],
    entry_points={
        "console_scripts": [
            "pydmtx=pydmtx.cli.main:main"
        ]
    },
    keywords="pydmtx datamatrix data matrix barcode ecc200",
)