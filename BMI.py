#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:16:50 2023

@author: markwin
"""

import streamlit as st

st.title("Welcome to BMI calculator 📏")

#Input

weight = st.number_input("Enter your weight in KG", min_value = 0.0, step = 0.1)

height = st.number_input("Enter your height in Meters", min_value = 0.0, step = 0.01)

def calculate_bmi():
    if height <= 0:
        st.error('Height needs to be more than zero. Please enter a valid number.')
    elif weight <=0:
        st.error('Weight needs to be more than zero. Please enter a valid number.')
    else:
        bmi = weight/(height)**2
        bmi_thresholds = [18.5, 23, 27.5]
        level_labels = ['Risk of nutritional deficiency','Low Risk','Moderate Risk','High Risk']
        
        if bmi <= bmi_thresholds[0]:
            level = level_labels[0]
        elif bmi <= bmi_thresholds[1]:
            level = level_labels[1]
        elif bmi <= bmi_thresholds[2]:
            level = level_labels[2]
        else:
            level = level_labels[3]
        st. success(f"Your BMI is {bmi}. You are at {level}")

button = st.button("Calculate BMI")
if button:
    calculate_bmi()
