# Puar

Simple tool to transform file from one format to another using template string

## Usage

```shell
$ python puar.py --help
usage: puar.py [-h] input_file template_string

Puar - Template based data transformation

positional arguments:
  input_file       Input file (csv, xls, xlsx)
  template_string  printf-style format string

optional arguments:
  -h, --help       show this help message and exit
```

For further details about the template string format see [Python Format String](https://docs.python.org/3.10/library/string.html#formatstrings).

## Example

Let's generate SQL insert queries from heroes.csv.

```
id,name
1,"Son Goku"
2,"Muten Roshi"
```

```shell
$ python puar.py heroes.csv "INSERT INTO heroes (id, name) VALUES (%(id)s, '%(name)s');"
INSERT INTO heroes (id, name) VALUES (1, 'Son Goku');
INSERT INTO heroes (id, name) VALUES (2, 'Muten Roshi');
```