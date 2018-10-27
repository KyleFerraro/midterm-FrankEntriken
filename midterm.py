#!/usr/bin/env python3

"""
Frank Entriken
2298368
entriken@chapman.edu
Scientific Computing 220
Midterm
"""

import matplotlib.pyplot as plt
import numpy as np

class MysterySequence(object):
    def __init__(self, r, x0 = 0.5, N = 100):
        self.r = r
        self.x0 = x0
        self.N = N
        self.xs = None

    def evaluate(self):
        r = self.r
        x = self.x0
        N = self.N
        self.xs = []
        for n in range(N+1):
            self.xs.append(x)
            x=(r*x*(1-x))

    def __call__(self):
        if (self.xs == None):
            self.evaluate()
            return(self.xs)
        else:
            return(self.xs)

class SequencePlotter(MysterySequence):
    def plot(self):
        self.evaluate()
        y = self.xs
        x = list(range(self.N+1))
        f = plt.figure(figsize=(12,8))
        a = plt.axes()
        a.plot(x, y, marker = '.', color = 'r')
        a.plot(x, y, linestyle = "--", color = 'k')
        a.set(ylim = (0,1), xlabel = 'Iteration K', ylabel = 'Population x(k)', title = "Sequence Parameters: x0={}, r={}, N={}".format(self.x0,self.r,self.N))

def scatterplot():
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

"""
    r = 2.9
    X = []
    Y = []
    while(r<=4):
        X = X + [r for i in range(1,151)]
        temp = MysterySequence(r, 0.5, 300)
        y = temp()
        del y[0:150]
        Y = Y + y
        r += 0.001

    N = 300
    x = 0.5
    r = np.arange(2.9, 4, 0.001)

    xs = []
    for i in r:
        xs.append(i)
    ys = []

    f = plt.figure(figsize=(12,8))
    for r in (xs):
        for n in range(N+1):
            ys.append(x)
            x=(r*x*(1-x))
    xs = [xs]*len(ys)
    print("Length of x's: ", len(xs),"Length of y's: ", len(ys))
    plt.scatter(xs, ys, marker='.', color='r')



    plt.scatter([xs]*len(ys), ys, marker='.', color='r')

    for r in xs:
        plt.scatter(r, ys, marker='.', color='r')


    for n in range(N+1):
        ys.append(x)
        x=(r*x*(1-x))
        for r in range(len(r)):
            plt.scatter
    f = plt.figure(figsize=(12,8))
    print(xs, ys)
    plt.scatter(xs, ys, marker='.', color='r')
"""
