# Puar

Simple tool to transform file from one format to another using template string

## Usage

```shell
$ python puar.py --help
usage: puar.py [-h] input_file template_string

Puar - shape-shifter

positional arguments:
  input_file       CSV input file
  template_string  Python format string

optional arguments:
  -h, --help       show this help message and exit
```

For further details about the template string format see [Python Format String](https://docs.python.org/3.10/library/string.html#formatstrings).

## Example

Let's generate SQL insert queries from heroes.csv.

```
id,name
1,"Muten Roshi"
2,"Son Goku"
```

```shell
$ python puar.py heroes.csv "INSERT INTO heroes (id, name) VALUES ({id}, '{name}');"
INSERT INTO heroes (id, name) VALUES (1, 'Muten Roshi');
INSERT INTO heroes (id, name) VALUES (2, 'Son Goku');
```