#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:10:20 2017

@author: Har using sentdex

This is an optimisation problem
book to learn convex optimisation(only 1 max or min(possibly global)) from stanford :
    https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf
"""

import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

class SupportVectorMachine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors = {1: 'r', -1:'b'}
        if(self.visualization):
            self.fig = plt.figure() #actual figure to the  whole window
            self.ax = self.fig.add_subplot(1,1,1) #1X1 grid and plot 1 but theres only 1 in this case
    # train
    def fit(self, data):
        self.data = data
        # { ||w|| : [w, b] }
        opt_dict = {}
        
        transforms = [[1,1],
                      [-1,1]
                      [-1,-1]
                      [-1,-1]] # linear combinations??? as same magnitude can be obtained using these tranforms
        
        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)
        
        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None
        
        step.sizes = [self.max_feature_value * 0.1,
                      self.max_feature_value * 0.01,
                      # point of expense: 100th of a percent
                      self.max_feature_value * 0.001,]
        
        b_range_multiple = 5 # very expensive 
        
        b_multiple = 5 #
        latest_optimum = self.max_feature_value * 10 #
        
        for step in step_sizes:
            
            w = np.array([latest_optimum, latest_optimum]) #starting point
            
            optimized = False # since convex problem we know when optimised
            
            while not optimized:
                pass
            
            
        
    
    def predict(self, features):
        # sign( x.w+b )
        classification = np.sign( np.dot(np.array(features), self.w) + self.b) #need w and b very important
        
        return classification
        
data_dict = {-1: np.array([[1,7],[2,8], [3,8]]),
             1:np.array([[5,1], [6,-1], [7,3]]) }

