# tokenish

![Code Coverage](https://img.shields.io/badge/Coverage-96%25-brightgreen.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple tool to fill pattern with tokens from file or directory.

- [Installation](#installation)
- [How to use](#how-to-use)
- [Examples](#examples)
- [License](#license)

## Installation

## How to use

```txt
usage: tokenish [-h] [-t TOKENS [TOKENS ...]] [-e ENCODING] [-o OUTPUT_DIRECTORY] [-om MAX_FILE_ROWS] pattern

Generate rows from pattern for each token combinations

positional arguments:
  pattern               text to fill with links or usernames/passwords

optional arguments:
  -h, --help            show this help message and exit
  -t TOKENS [TOKENS ...], --tokens TOKENS [TOKENS ...]
                        list of tokens file or directory path
  -e ENCODING, --encoding ENCODING
                        type of encoding to apply
  -o OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
                        directory where results will write, print is None
  -om MAX_FILE_ROWS, --max-file-rows MAX_FILE_ROWS
                        maximum number of rows per file, default 10 000
```

Available token path:

- file: all lines in file are consider like tokens.
- directory: all lines of all files in directory are consider like tokens.

Available encoding:

- base64

## Examples

Print all combination of username/password, where usernames replace &TOKEN_0& and passwords replace &TOKEN_1&.

```sh
python tokenish.py "Authentication: Basic &TOKEN_0&:&TOKEN_1&" -t /path/to/usernames/dir/ /path/to/passwords.txt
```

Save all combination of username/password in directory /path/output/ composed by files of 10 000 lines.

```sh
python tokenish.py "Authentication: Basic &TOKEN_0&:&TOKEN_1&" -t /path/to/usernames/dir/ /path/to/passwords.txt -o /path/output/
```

Save all combination of username/password in directory /path/output/ composed by files of 500 lines.

```sh
python tokenish.py "Authentication: Basic &TOKEN_0&:&TOKEN_1&" -t /path/to/usernames/dir/ /path/to/passwords.txt -o /path/output/ -om 500
```

Print all combination of username/password, where usernames replace &TOKEN_0& and passwords replace &TOKEN_1&.
Expression in tag &ENC[...]ODE& will encode in base64.

```sh
python tokenish.py "Authentication: Basic &ENC[&TOKEN_0&:&TOKEN_1&]ODE&" -t /path/to/usernames/dir/ /path/to/passwords.txt -e base64
```

## License

tokenish is released under MIT license. See [LICENSE](https://gitlab.com/hack8883509/tokenish/-/blob/main/LICENSE).