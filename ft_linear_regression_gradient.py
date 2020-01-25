#!/usr/bin/python3

import os
from gestion_data import gestion_data
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing


class ft_linear_regression(gestion_data):
    def __init__(self, gestion_data):
        self.epochs = 10
        self.lr = 0.001

        # X = np.linspace(-1, 1, 100) + np.random.normal(0, 0.25, 100)
        # Y = np.linspace(-1, 1, 100) + np.random.normal(0, 0.25, 100)

        # self.km_values = X
        # self.price_values = Y

        self.km_values = gestion_data.array_km
        self.price_values = gestion_data.array_price

        self.normalized_km_values = preprocessing.normalize(self.km_values)
        self.normalized_price_values = preprocessing.normalize(
            self.price_values)

        # self.normalized_km_values = self.normalized_km_values(self.km_values)
        # self.normalized_price_values = self.normalized_price_values(
        #     self.price_values)

        # Exécution de l'algorithme
        teta1, teta0 = self.gradient_descent_LR(
            self.normalized_km_values, self.normalized_price_values, self.epochs, self.lr)
        self.normalize_teta0 = teta0
        self.normalize_teta1 = teta1

        self.teta0 = preprocessing.scale(self.normalize_teta0)
        self.teta1 = preprocessing.scale(self.normalize_teta1)

        self.line_km = self.calculate_line_km(
            self.km_values, self.price_values)
        self.line_price = self.calculate_line_price(
            self.teta1, self.teta0, self.line_km)

    def __str__(self):
        return 'linear regression calulator'

    def print_all_value(self):
        print("/* ******************** km_values    ******************** */")
        print(self.km_values)
        print("/* ******************** price_values ******************** */")
        print(self.price_values)
        print("/* ******************** teta0        ******************** */")
        print(self.teta0)
        print("/* ******************** teta1        ******************** */")
        print(self.teta1)
        print("/* ******************** line_km      ******************** */")
        print(self.line_km)
        print("/* ******************** line_price   ******************** */")
        print(self.line_price)
        print("/* ******************** ************ ******************** */")

    # def normalized_km_values(self, km_values):
    #     normalized_km_values = []
    #     idx_km_min = km_values.index(min(km_values))
    #     idx_km_max = km_values.index(max(km_values))
    #     for value in km_values:
    #         normalized_km_values.append(
    #             (value - km_values[idx_km_min]) / (km_values[idx_km_max] - km_values[idx_km_min]))
    #     return normalized_km_values

    # def normalized_price_values(self, price_values):
    #     normalized_price_values = []
    #     idx_price_min = price_values.index(min(price_values))
    #     idx_price_max = price_values.index(max(price_values))
    #     for value in price_values:
    #         normalized_price_values.append((value - price_values[idx_price_min]) / (
    #             price_values[idx_price_max] - price_values[idx_price_min]))
    #     return normalized_price_values

    # gradient teta1 calculator for 1 iteration
    def teta1_grad(self, teta1, teta0, km_values, price_values):
        return sum(-2 * x * (price_values[idx] - (teta1 * x + teta0)) for idx, x in enumerate(km_values)) / float(len(km_values))

    # gradient teta0 calculator for 1 iteration
    def teta0_grad(self, teta1, teta0, km_values, price_values):
        return sum(-2 * (price_values[idx] - (teta1 * x + teta0)) for idx, x in enumerate(km_values)) / float(len(km_values))

    # gradient algo start
    def gradient_descent_LR(self, km_values, price_values, epochs, lr):
        assert(len(km_values) == len(price_values))
        teta1 = 0
        teta0 = 0
        for e in range(epochs):
            teta1 = teta1 - lr * \
                self.teta1_grad(teta1, teta0, km_values, price_values)
            teta0 = teta0 - lr * \
                self.teta0_grad(teta1, teta0, km_values, price_values)
        return teta1, teta0

    # calcul usefull for the Visualisation of teta1 and teta0
    def calculate_line_km(self, km_values, price_values):
        return [min(km_values), max(price_values)]

    # calcul usefull for the Visualisation of teta1 and teta0
    def calculate_line_price(self, teta1, teta0, line_km):
        return [(teta1 * i) + teta0 for i in line_km]

    def matploit_printer(self, line_km, line_price, km_values, price_values):
        plt.plot(line_km, line_price, color='blue', linewidth=3)
        plt.scatter(km_values, price_values, color='black')
        plt.xticks()
        plt.yticks()
        plt.show()


if __name__ == '__main__':
    try:
        gestion_data = gestion_data()

        ft_linear_regression = ft_linear_regression(gestion_data)

        ft_linear_regression.print_all_value()
        # ft_linear_regression.create_result(
        #     ft_linear_regression.teta0, ft_linear_regression.teta1)

        ft_linear_regression.matploit_printer(
            ft_linear_regression.line_km, ft_linear_regression.line_price, ft_linear_regression.km_values,  ft_linear_regression.price_values
        )

        del gestion_data
        del ft_linear_regression
    except:
        exit(42)
