#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 23:51:43 2017

Line Class

@author: ucalegon
"""
import numpy as np
# Define a class to receive the characteristics of each line detection
class Lane():
    def __init__(self):
        # When initialized, set first_frame property as True:
        self.first_frame = True
        # was the line detected in the last iteration?
        self.detected = False
        # x values of the last n fits of the line
        self.recent_xfitted = []
        #average x values of the fitted line over the last n iterations
        self.bestx = None
        #polynomial coefficients averaged over the last n iterations
        self.best_fit = None
        #polynomial coefficients for the most recent fit
        self.current_fit = [np.array([False])]
        #radius of curvature of the line in some units
        self.radius_of_curvature = None
        #distance in meters of vehicle center from the line
        self.line_base_pos = None
        #difference in fit coefficients between last and new fits
        self.diffs = np.array([0,0,0], dtype='float')
        #x values for detected line pixels
        self.allx = None
        #y values for detected line pixels
        self.ally = None
