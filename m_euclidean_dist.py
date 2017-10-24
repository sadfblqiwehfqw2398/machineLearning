#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:05:54 2017

@author: Har
"""
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {'k':[[1,2], [2,3], [3,1]], 'r':[[6,5], [7,7], [8,6]], 'm':[[2,6],[2,7],[6,2],[7,2]]}
new_features = [5,5]



def k_nearest(data, predict, k=3):
    if len(data) >= k:
        warnings.war('k value less than something')
        
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])
            
    votes = [i[1] for i in sorted(distances)[:k]]
    print(votes)
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    
    return vote_result

results = k_nearest(dataset, new_features, 4)
print(results)

for i in dataset: 
    for ii in dataset[i]:
        plt.scatter(ii[0], ii[1], s = 100, color = i)
plt.scatter(new_features[0], new_features[1], color = results)
plt.show()