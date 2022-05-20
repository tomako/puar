import csv
from argparse import ArgumentParser


def main(input_file, template):
    with open(input_file) as ifo:
        csv_reader = csv.DictReader(ifo)
        for row in csv_reader:
            print(template.format(**row))


if __name__ == '__main__':
    parser = ArgumentParser(description='Puar - shape-shifter')
    parser.add_argument('input_file', help='CSV input file')
    parser.add_argument('template_string', help='Python format string')
    args = parser.parse_args()

    main(args.input_file, args.template_string)
