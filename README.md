# pydmtx

**pydmtx** is a Python library that enables programs to **write** Data Matrix barcodes of the modern ECC200 variety.

## Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [CLI](#cli)
- [Export plugins](#export-plugins)
  - [Create your own export plugin](#create-your-own-export-plugin)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## Features

- Implemented in accordance with ISO/IEC 16022:2006(E)
- Usually produce the shortest codeword stream
- Supports rectangular symbols
- [Plugins](#export-plugins)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pydmtx.

```bash
pip install TODO
```

## Usage

TODO

## Examples

```py
import pydmtx

text_representation = pydmtx.encode("hello").format("text")
```

## CLI

TODO

## Export plugins

Additional export mechanism can be installed as plugins. They can be found on the [Python Package Index](https://pypi.org/search/?q=pydmtx). Here's a few picks:

- [pydmtx-export-svg](https://github.com/pydmtx/pydmtx-export-svg)
- [pydmtx-export-raster](https://github.com/pydmtx/pydmtx-export-raster)

### Create your own export plugin

TODO

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact

If you want to contact me you can reach me at <mkgumienny@gmail.com>

## License

[MIT](LICENSE)
