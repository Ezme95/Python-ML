# all data has to be numerical
# non numerical columns must be converted to numerical
# use map() method to take a dictionary with infomation and convert it to values
# import modules

import pandas
# sklearn is a useful Machine Learning library in python
# import tree refers to importing decision tree module in skLearn
import csv
from sklearn import tree
# for graph
import pydotplus

# decision tree DecisionTreeClassifier is a class for multi-class classification
# a class is a code template for creating objects (the tree is the object)
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
# to split data to training and testing set
from sklearn import model_selection
from sklearn.model_selection import train_test_split
# for plots
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import pygraphviz
# numpy supports maths for data in multiple arrays
import numpy as np
# ******************************************************************************
# STEP 1: READ DATA

# always copy file path
# DO NOT JUST PLACE THE FILE NAME BECAUSE IT DOES NOT REFLECT ABSOLUTE PATH
# data is about individuals and whether they would go to a comedy Show
data = pandas.read_csv(r"C:\Users\Esmeralda\github\Python-ML\data.csv")

# ******************************************************************************

# STEP 2: CONVERT VALUES TO NUMERICAL

# initiate dictionary X (key) : Y (value) -> keypair value
# Must convert values to numerical, in the dataset convert Nationality and Go
# use dictionary to put keyvalue keypair {}
# make UK: 0, USA: 1, N: 2
dNationality = {"UK" : 0, "USA" : 1, "N" : 2}
# make Yes : 1, No : 0
dGo = {"YES" : 1, "NO" : 0}
# data["Go"].head().values # check datatype
# df is now the file, [column for change] = file.map(the dictionary for replacement)
data["Nationality"] = data["Nationality"].map(dNationality)
data["Go"] = data["Go"].map(dGo)

print(data)
# ******************************************************************************

# STEP 3: IDENTIFY FEATURES AND TARGET

# Separate the feature columns from the target columns
# Feature columns are columns where prediction is made from
# Target columns are columns with the values that is to be predicted

features = ["Age", "Experience", "Rank", "Nationality"]
# make feature columns "x"
x = data[features]
# make target column "y"
y = data["Go"]



print(x)
print(y)


# ******************************************************************************

# STEP 4: TRAIN THE DATA -> TRAINING DATASET

# the decision tree class, creating classifier object
dataTree = DecisionTreeClassifier()
# fit data to the model
dataTree = dataTree.fit(x,y)
# ******************************************************************************

# STEP 5: VISUALIZE THE DATA

dataPlot = tree.export_graphviz(dataTree, out_file=None, feature_names = features)
# draw graph using pydotplus
graph = pydotplus.graph_from_dot_data(dataPlot)
# convert graph to png
graph.write_png("comDecisionTree.png")
img=pltimg.imread("comDecisionTree.png")
imgplot = plt.imshow(img)
# show the plot
plt.show()
