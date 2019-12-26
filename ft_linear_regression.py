#!/usr/bin/python3

import os
from gestion_data import gestion_data
import matplotlib.pyplot as plt


class ft_linear_regression(gestion_data):
    def __init__(self, gestion_data):
        self.km_values = gestion_data.array_km
        self.price_values = gestion_data.array_price
        self.mean_km = self.calculate_mean_km(self.km_values)
        self.mean_price = self.calculate_mean_price(self.price_values)
        self.mean_km_values = self.calculate_mean_km_values(
            self.km_values, self.mean_km)
        self.mean_price_values = self.calculate_mean_price_values(
            self.price_values, self.mean_price)
        self.square_mean_km_values = self.calculate_square_mean_km_values(
            self.mean_km_values)
        self.square_mean_price_values = self.calculate_square_mean_price_values(
            self.mean_price_values)
        self.mean_km_x_price_values = self.calculate_mean_km_x_price_values(
            self.mean_km_values, self.mean_price_values)
        self.sum_square_km = self.calculate_sum_square_km(
            self.square_mean_km_values)
        self.sum_mean_km_x_price_values = self.calculate_sum_mean_km_x_price_values(
            self.mean_km_x_price_values)
        self.teta1 = self.calculate_teta1(
            self.sum_square_km, self.sum_mean_km_x_price_values)
        self.teta0 = self.calculate_teta0(
            self.mean_price, self.mean_km, self.teta1)
        self.price_linear_regression_values = self.calculate_price_linear_regression_values(
            self.km_values,
            self.teta0,
            self.teta1
        )

    def __str__(self):
        return 'linear regression calulator'

    def print_all_value(self):
        print("/* ******************** km_values                  ******************** */")
        print(self.km_values)
        print("/* ******************** price_values               ******************** */")
        print(self.price_values)
        print("/* ******************** mean_km                    ******************** */")
        print(self.mean_km)
        print("/* ******************** mean_price                 ******************** */")
        print(self.mean_price)
        print("/* ******************** mean_km_values             ******************** */")
        print(self.mean_km_values)
        print("/* ******************** mean_price_values          ******************** */")
        print(self.mean_price_values)
        print("/* ******************** square_mean_km_values      ******************** */")
        print(self.square_mean_km_values)
        print("/* ******************** square_mean_price_values   ******************** */")
        print(self.square_mean_price_values)
        print("/* ******************** mean_km_x_price_values     ******************** */")
        print(self.mean_km_x_price_values)
        print("/* ******************** sum_square_km              ******************** */")
        print(self.sum_square_km)
        print("/* ******************** sum_mean_km_x_price_values ******************** */")
        print(self.sum_mean_km_x_price_values)
        print("/* ******************** sum_square_km              ******************** */")
        print(self.sum_square_km)
        print("/* ******************** teta1                      ******************** */")
        print(self.teta1)
        print("/* ******************** teta0                      ******************** */")
        print(self.teta0)
        print("/* ******************** ************************** ******************** */")

    def calculate_mean_km(self, km_values):
        mean_km = 0
        for value in km_values:
            mean_km += value
        mean_km = mean_km / len(km_values)
        return mean_km

    def calculate_mean_price(self, price_values):
        mean_price = 0
        for value in price_values:
            mean_price += value
        mean_price = mean_price / len(price_values)
        return mean_price

    def calculate_mean_km_values(self, km_values, mean_km):
        mean_km_values = []
        for value in km_values:
            mean_km_values.append(value - mean_km)
        return mean_km_values

    def calculate_mean_price_values(self, price_values, mean_price):
        mean_price_values = []
        for value in price_values:
            mean_price_values.append(value - mean_price)
        return mean_price_values

    def calculate_square_mean_km_values(self, mean_km_values):
        square_mean_km_values = []
        for value in mean_km_values:
            square_mean_km_values.append(value ** 2)
        return square_mean_km_values

    def calculate_square_mean_price_values(self, mean_price_values):
        square_mean_price_values = []
        for value in mean_price_values:
            square_mean_price_values.append(value ** 2)
        return square_mean_price_values

    def calculate_mean_km_x_price_values(self, mean_km_values, mean_price_values):
        mean_km_x_price_values = []
        i = 0
        while i < len(mean_km_values):
            mean_km_x_price_values.append(
                mean_km_values[i] * mean_price_values[i])
            i += 1
        return mean_km_x_price_values

    def calculate_sum_square_km(self, square_mean_km_values):
        sum_square_km = 0
        for value in square_mean_km_values:
            sum_square_km += value
        return sum_square_km

    def calculate_sum_mean_km_x_price_values(self, mean_km_x_price_values):
        sum_mean_km_x_price_values = 0
        for value in mean_km_x_price_values:
            sum_mean_km_x_price_values += value
        return sum_mean_km_x_price_values

    def calculate_teta1(self, sum_square_km, sum_mean_km_x_price_values):
        return sum_mean_km_x_price_values / sum_square_km

    def calculate_teta0(self, mean_price, mean_km, teta1):
        return mean_price - (teta1 * mean_km)

    def calculate_price_linear_regression_values(self, km_values, teta0, teta1):
        price_linear_regression_values = []
        for value in km_values:
            price_linear_regression_values.append(teta0 + (teta1 * value))
        return price_linear_regression_values

    def generate_matploit_graph(self, km_values, price_values, price_linear_regression_values):
        plt.scatter(km_values, price_values, color='black')
        plt.plot(km_values, price_linear_regression_values,
                 color='blue', linewidth=3)

        plt.xticks()
        plt.yticks()
        plt.show()

    def create_result(self, teta0, teta1):
        if os.path.exists("result.txt"):
            os.remove("result.txt")
        f = open("result.txt", "w+")
        f.write(str(teta0) + "," + str(teta1) + "\n")
        f.close()


if __name__ == '__main__':
    gestion_data = gestion_data()
    gestion_data.print_all_value()

    ft_linear_regression = ft_linear_regression(gestion_data)
    ft_linear_regression.print_all_value()
    ft_linear_regression.create_result(
        ft_linear_regression.teta0, ft_linear_regression.teta1)
    ft_linear_regression.generate_matploit_graph(
        ft_linear_regression.km_values, ft_linear_regression.price_values, ft_linear_regression.price_linear_regression_values)

    del gestion_data
    del ft_linear_regression
