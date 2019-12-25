#!/usr/bin/python3

import argparse
import csv


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='file',
                        help='set the path to csv file.')
    parser.add_argument('-k', '--km', dest='km',
                        help='the kilometer of your car')
    parser.add_argument('-p', '--price', dest='price',
                        help='the price of your car')
    options = parser.parse_args()
    return options


# def accept_csv_file(file):
#     try:
#         csv_fileh = open(file, 'rb')
#         csv.Sniffer().sniff(csv_fileh.read(1024))
#         csv_fileh.seek(0)
#         return True
#     except csv.Error:
#         return False


class gestion_csv:
    def __init__(self):
        self.fd = []
        self.options = get_arguments()
        # if accept_csv_file(self.options.file):
        #     exit(code="CSV file incorrect.")
        self.file = self.options.file
        self.km = self.options.km
        self.price = self.options.price
        self.content = self.open_and_read_csv_file(self.file)
        self.array_km = self.get_kilometer_from_csv(self.content)
        self.array_price = self.get_price_from_csv(self.content)

    def __str__(self):
        return 'Gestionnary of CSV file'

    def open_and_read_csv_file(self, file):
        fd = open(file, "r")
        self.fd.append(fd)
        content = fd.read()
        return content

    def close_all_file(self, fd):
        for file in fd:
            file.close()

    def print_all_value(self):
        print("/* ******************** Options     ******************** */")
        print(self.options)
        print("/* ******************** File        ******************** */")
        print(self.file)
        print("/* ******************** Km          ******************** */")
        print(self.km)
        print("/* ******************** Price       ******************** */")
        print(self.price)
        print("/* ******************** Content     ******************** */")
        print(self.content)
        print("/* ******************** Array Km    ******************** */")
        print(self.array_km)
        print("/* ******************** Array Price ******************** */")
        print(self.array_price)
        print("/* ******************** *********** ******************** */")

    def get_kilometer_from_csv(self, content):
        whitespace_split = content.split('\n')
        array_km = []
        i = 0
        for line in whitespace_split:
            if i != 0 and i != len(whitespace_split) - 1:
                coma_split = line.split(',')
                array_km.append(coma_split[0])
            i += 1
        return array_km

    def get_price_from_csv(self, content):
        whitespace_split = content.split('\n')
        array_price = []
        i = 0
        for line in whitespace_split:
            if i != 0 and i != len(whitespace_split) - 1:
                coma_split = line.split(',')
                array_price.append(coma_split[1])
            i += 1
        return array_price


if __name__ == '__main__':
    gestion_csv = gestion_csv()
    gestion_csv.print_all_value()
    del gestion_csv
