#!/usr/bin/env python3
# -*- coding: utf-8 -*-
####
# Frank Entriken
# Email: entriken@chapman.edu
# Midterm
# PHYS 220
# 10/26/2018
####

import matplotlib.pyplot as plt
import numpy as np

class MysterySequence(object):
    """
    Creates object with four attributes: (r) - value that is evaluated, (x0) - initial x value, (N) - number of iterations, (xs) - list of x values
    """
    def __init__(self, r, x0 = 0.5, N = 100):
        """
        Initializes object with four attributes which default to specific values
        """
        self.r = r
        self.x0 = x0
        self.N = N
        self.xs = None

    def evaluate(self):
        """
        Evaluates using equation according to given r value, initial x value, and number of iterations N
        Creates list of computed values in xs
        """
        r = self.r
        x = self.x0
        N = self.N
        self.xs = []
        for n in range(N+1):
            self.xs.append(x)
            x=(r*x*(1-x))

    def __call__(self):
        """
        Evaluates and returns list of x values if evaluate equals 'None'
        """
        if (self.xs == None):
            self.evaluate()
            return(self.xs)
        else:
            return(self.xs)

class SequencePlotter(MysterySequence):
    """
    Plots graph according to given list of x values (xs)
    """
    def plot(self):
        """
        Plots graph by representing list of x values as the y-axis and list of r values according to N as x-axis
        Plots graph with points, lines connecting points, labels, and title
        """
        self.evaluate()
        y = self.xs
        x = list(range(self.N+1))
        f = plt.figure(figsize=(12,8))
        a = plt.axes()
        a.plot(x, y, marker = '.', color = 'r')
        a.plot(x, y, linestyle = "--", color = 'k')
        a.set(ylim = (0,1), xlabel = 'Iteration K', ylabel = 'Population x(k)', title = "Sequence Parameters: x0={}, r={}, N={}".format(self.x0,self.r,self.N))

def scatterplot():
    """
    Graphs a scatterplot of computed values at every r value in range [2.9, 4] with an iteration of 0.001
    Sets r value at 2.9
    """
    xs = []
    ys = []
    r = 2.9

    for r in np.arange(2.9, 4, 0.001):
        temp_mystery = MysterySequence(r, 0.5, 300)
        temp_ys = temp_mystery()
        del temp_ys[0 : 151]
        xs = xs + [r for i in range(1,151)]
        ys = ys + temp_ys

    fig, ax = plt.subplots(figsize=(12,8))
    ax.scatter(xs, ys, marker='.', color='r')
    ax.set(ylim = (0,1), xlim = (2.9,4), xlabel = 'Iteration R', ylabel = 'Asymptotic Value', title = "Sequence Parameters: x0={0.5}, r={[2.9,4]}, N={300}")
