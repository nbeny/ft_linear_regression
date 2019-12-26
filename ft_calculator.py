#!/usr/bin/python3

import argparse


class ft_calculator:
    def __init__(self):
        self.options = self.get_arguments()
        self.file = self.options.file

    def __str__(self):
        return "calcul the price of you're car."

    def print_all_value(self):
        print("/* ******************** Options     ******************** */")
        print("/* ******************** File        ******************** */")
        print("/* ******************** Content     ******************** */")
        print("/* ******************** Array Km    ******************** */")
        print("/* ******************** Array Price ******************** */")
        print("/* ******************** *********** ******************** */")

    def get_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--file', dest='file',
                            default='./result.txt', help='set the path to result.txt file')
        parser.add_argument('-k', '--km', dest='km',
                            help="set the kilometer of you're car.")
        options = parser.parse_args()
        return options


if __name__ == '__main__':
    ft_calculator = ft_calculator()
