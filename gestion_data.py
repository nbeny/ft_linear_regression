#!/usr/bin/python3

import sys
import argparse
import csv
from csvvalidator import (
    CSVValidator,
    write_problems
)


class gestion_data:
    def __init__(self):
        self.fd = []
        self.options = self.get_arguments()
        self.file = self.options.file
        if self.validate_csv_file(self.file):
            self.content = self.open_and_read_csv_file(self.file)
            self.array_km = self.get_kilometer_from_csv(self.content)
            self.array_price = self.get_price_from_csv(self.content)

    def __str__(self):
        return 'Gestionnary of CSV file'

    def print_all_value(self):
        print("/* ******************** Options     ******************** */")
        print(self.options)
        print("/* ******************** File        ******************** */")
        print(self.file)
        print("/* ******************** Content     ******************** */")
        print(self.content)
        print("/* ******************** Array Km    ******************** */")
        print(self.array_km)
        print("/* ******************** Array Price ******************** */")
        print(self.array_price)
        print("/* ******************** *********** ******************** */")

    def get_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--file', dest='file',
                            help='set the path to csv file.')
        options = parser.parse_args()
        return options

    def validate_csv_file(self, file):
        try:
            field_names = (
                'km',
                'price'
            )
            validator = CSVValidator(field_names)
            validator.add_value_check('km', str, 'km must be a float')
            validator.add_value_check('price', str, 'km must be a float')
            data = csv.reader(file, delimiter=',')
            problems = validator.validate(data)
            # write_problems(problems, sys.stdout)
            if not problems:
                return True
            else:
                return False
        except:
            print('usage:')
            print(
                '\tpython ft_linear_regression.py -f CSV_FILE')
            print('\tOR')
            print(
                '\tpython ft_linear_regression.py --file CSV_FILE')
            print('')
            print('for exit the matploit graph in the terminal use :')
            print('\tcontol + shift + \\')
            print('')
            print('=D')
            exit(42)

    def open_and_read_csv_file(self, file):
        fd = open(file, "r")
        self.fd.append(fd)
        content = fd.read()
        return content

    def close_all_file(self, fd):
        for file in fd:
            file.close()

    def get_kilometer_from_csv(self, content):
        try:
            whitespace_split = content.split('\n')
            array_km = []
            i = 0
            for line in whitespace_split:
                if i != 0 and i != len(whitespace_split) - 1:
                    coma_split = line.split(',')
                    array_km.append(float(coma_split[0]))
                i += 1
            return array_km
        except:
            print('bad csv file, value can only be number.')
            exit(42)

    def get_price_from_csv(self, content):
        try:
            whitespace_split = content.split('\n')
            array_price = []
            i = 0
            for line in whitespace_split:
                if i != 0 and i != len(whitespace_split) - 1:
                    coma_split = line.split(',')
                    array_price.append(float(coma_split[1]))
                i += 1
            return array_price
        except:
            print('bad csv file, value can only be number.')
            exit(42)
