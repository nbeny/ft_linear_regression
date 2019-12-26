#!/usr/bin/python3

import os
import argparse


class ft_calculator:
    def __init__(self):
        self.options = self.get_arguments()
        self.file = self.options.file
        self.km = self.options.km
        if self.km != None:
            self.content = self.read_file(self.file)
            teta0, teta1 = self.get_teta(self.content)
            self.teta0 = teta0
            self.teta1 = teta1
            self.result = self.calcul_price_with_teta_value(
                self.teta0, self.teta1, self.km)
        else:
            print('no km set in argument')
            exit(42)

    def __str__(self):
        return "calcul the price of you're car."

    def get_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--file', dest='file',
                            default='result.txt', help='set the path to result.txt file')
        parser.add_argument('-k', '--km', dest='km',
                            help="set the kilometer of you're car.")
        options = parser.parse_args()
        return options

    def read_file(self, file):
        if os.path.exists(file):
            f = open(file, "r")
            content = f.read()
            f.close()
            return content
        print("file doesn't exists.")
        exit(42)

    def get_teta(self, content):
        try:
            white_space = content.split('\n')
            coma_split = white_space[0].split(',')
            teta0 = float(coma_split[0])
            teta1 = float(coma_split[1])
            return teta0, teta1
        except:
            print("check you're result file.")
            exit(42)

    def calcul_price_with_teta_value(self, teta0, teta1, km):
        return teta0 + (teta1 * float(km))


if __name__ == '__main__':
    ft_calculator = ft_calculator()
    print(ft_calculator.result)
