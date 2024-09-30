[![Python 3.9](https://img.shields.io/badge/Python3-%3E%3D3.9-blue)](https://www.python.org/downloads)

# pyGraylog
Graylog User Script
```bash
pyGraylog
├── LICENSE
├── README.md
├── graylog
│   ├── __init__.py
│   ├── users.py
│   └── utils
│       ├── createUser.py
│       └── output.py
├── main.py
└── requirements.txt

3 directories, 8 files
```
#
## Requirements
```bash
requests
```
#
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.
```bash
pip3 install -r requirements.txt
```
#
## Usage
```python
usage: main.py [-h] [-u USER] [-a] [-c CREATE] [-p] [-s] [-o OUTPUT] [-m]

Graylog User Script

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Get a specific user
  -a, --all             List all users
  -c CREATE, --create CREATE
                        Create an user
  -p, --permission      Include user's permissions
  -s, --session         Include user's sessions
  -o OUTPUT, --output OUTPUT
                        Output to a csv file
  -m, --migrate         Migrate LDAP user to normal user


Author: _wiky
```
## License
[MIT](https://choosealicense.com/licenses/mit/)