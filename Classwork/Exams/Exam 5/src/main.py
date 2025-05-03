from modules.userClass import *
import matplotlib.pyplot as plt
import numpy as np

weights1 = [134.67, 124.89, 120.45, 119.67, 118.90, 117.45, 116.78, 115.90, 115.45, 114.67, 114.45, 113.89]
weights = [134.67, 124.89, 120.45, 119.67, 118.90, 117.45]

user1 = User("Maaz", weights)

try:
    user1.plotGraph()
except Exception as e:
    print(e)