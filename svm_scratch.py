#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:10:20 2017

@author: Har
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
            self.fig = plt.gigure()
            self.ax = self.fig.add_subplot(1,1,1)

data_dict = {-1: np.arrar([[1,7],[2,8], [3,8]]),
             1:np.array([[5,1], [6,-1], [7,3]]) }

