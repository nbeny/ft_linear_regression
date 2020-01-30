#!/usr/bin/python3

import os
from gestion_data import gestion_data
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler


class ft_linear_regression(gestion_data):
    def __init__(self, gestion_data):
        self.epochs = 10
        self.lr = 0.001

        self.km_values = gestion_data.array_km
        self.price_values = gestion_data.array_price

        # Normalize dataframe
        self.normalized_km_values = self.normalized_km(self.km_values)
        self.normalized_price_values = self.normalized_price(self.price_values)

        # Exécution de l'algorithme
        normalized_array_teta1, normalized_array_teta0 = self.gradient_descent_LR(
            self.normalized_km_values, self.normalized_price_values, self.epochs, self.lr)

        # Unnormalize dataframe
        self.array_teta0 = self.unnormalized_teta0(normalized_array_teta0)
        self.array_teta1 = self.unnormalized_teta1(normalized_array_teta1)

        self.teta0 = self.get_real_teta(self.array_teta0)
        self.teta1 = self.get_real_teta(self.array_teta1)

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

    def get_real_teta(self, array):
        teta_total = 0
        idx = 0
        for value in array:
            teta_total += value
            idx += 1
        teta = teta_total / idx
        return teta

    def normalized_km(self, km_values):
        normalized_km_values = []
        idx_km_min = km_values.index(min(km_values))
        idx_km_max = km_values.index(max(km_values))
        for value in km_values:
            normalized_km_values.append(
                (value - km_values[idx_km_min]) / (km_values[idx_km_max] - km_values[idx_km_min]))
        return normalized_km_values

    def normalized_price(self, price_values):
        normalized_price_values = []
        idx_price_min = price_values.index(min(price_values))
        idx_price_max = price_values.index(max(price_values))
        for value in price_values:
            normalized_price_values.append((value - price_values[idx_price_min]) / (
                price_values[idx_price_max] - price_values[idx_price_min]))
        return normalized_price_values

    # unnormalized data set frame
    # ^x = ( x - min(x) ) / ( max(x) - min(x) )
    # ^x * ( max(x) - min(x) ) = x - min(x)
    # x = ^x * ( max(x) - min(x) ) + min(x)
    def unnormalized_teta0(self, normalized_array_teta0):
        array_teta0 = []
        print(normalized_array_teta0)
        teta0_min = min(float(normalized_teta0_min)
                        for normalized_teta0_min in normalized_array_teta0)
        teta0_max = max(float(normalized_teta0_max)
                        for normalized_teta0_max in normalized_array_teta0)
        for value in normalized_array_teta0:
            array_teta0.append(
                value * (teta0_max - teta0_min) + teta0_min
            )
        return array_teta0

    # unnormalized data set frame
    # ^x = ( x - min(x) ) / ( max(x) - min(x) )
    # ^x * ( max(x) - min(x) ) = x - min(x)
    # x = ^x * ( max(x) - min(x) ) + min(x)
    def unnormalized_teta1(self, normalized_array_teta1):
        array_teta1 = []
        print(normalized_array_teta1)
        teta1_min = min(float(normalized_teta1_min)
                        for normalized_teta1_min in normalized_array_teta1)
        teta1_max = max(float(normalized_teta1_max)
                        for normalized_teta1_max in normalized_array_teta1)
        for value in normalized_array_teta1:
            array_teta1.append(
                value * (teta1_max - teta1_min) + teta1_min
            )
        return array_teta1

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
        array_teta1 = []
        array_teta0 = []
        for e in range(epochs):
            teta1 = teta1 - lr * \
                self.teta1_grad(teta1, teta0, km_values, price_values)
            teta0 = teta0 - lr * \
                self.teta0_grad(teta1, teta0, km_values, price_values)
            array_teta1.append(teta1)
            array_teta0.append(teta0)
        return array_teta1, array_teta0

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
    # try:
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
    # except:
    # exit(42)
