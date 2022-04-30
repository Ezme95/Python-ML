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
dGo = {"YES" : "1", "NO" : "0"}
# data["Go"].head().values # check datatype
# df is now the file, [column for change] = file.map(the dictionary for replacement)
data["Nationality"] = data["Nationality"].map(dNationality)
data["Go"] = data["Go"].map(dGo)

# print(data)
# ******************************************************************************

# STEP 3: SPLIT DATA TO TRAINING AND TESTING

# splitting data using pandas, split by 80:20
training_data = data.sample(frac=0.8,random_state=42)
testing_data = data.drop(training_data.index)

# ******************************************************************************

# STEP 4: IDENTIFY FEATURES AND TARGET

# Separate the feature columns from the target columns
# Feature columns are columns where prediction is made from
# Target columns are columns with the values that is to be predicted

features = ["Age", "Experience", "Rank", "Nationality"]
# make feature columns "x"
x_train = training_data[features]
# make target column "y"
y_train = training_data["Go"]

x_test = testing_data[features]
y_test = testing_data["Go"]

# print(x)
# print(y)

# ******************************************************************************

# STEP 6: TRAIN THE DATA -> TRAINING DATASET

# the decision tree class, creating classifier object
dataTree = DecisionTreeClassifier()
# fit data to the model
dataTreez = dataTree.fit(x_train,y_train)
#dataTreez.get_params()
# ******************************************************************************

# STEP 7: VISUALIZE THE DATA (training)


dataPlot = tree.export_graphviz(dataTreez, out_file=None, feature_names = features)
# draw graph using pydotplus
graph = pydotplus.graph_from_dot_data(dataPlot)
# convert graph to png
graph.write_png("comDecisionTree.png")
img=pltimg.imread("comDecisionTree.png")
imgplot = plt.imshow(img)
# show the plot
plt.show()

# ******************************************************************************

# STEP 8: PREDICTION VIA TESTING DATA
print(testing_data)

predictions = dataTree.predict(x_test)
predictions

from sklearn.metrics import accuracy_score
# Accuracy is the measure of the number of correct predictions off the total
#ACC = (TP+TN)/(TP+FP+FN+TN)
accuracy = round(accuracy_score(y_test,predictions),2)


from sklearn.metrics import confusion_matrix
# confusion matrix is equal to the number of observations in first group and prediction in the second group
# i.e. confusion matrix C, is given C[i][j], where i is known observations, and j is predicted
CM = confusion_matrix (y_test, predictions)
TP = CM[1][1] # true positive
FP = CM[0][1] # false positive
TN = CM[0][0] # true negative
FN = CM[1][0] # false negative


# Precision is the number of correct positive predictions
# true positives / (true positives + false positives)
precision = round(TP/(TP + FP),2)


# recall is the number of correct positive predictions out of all the positive predictions
# true positives / (true positives + false negatives)
recall = round(TP/ (TP + FN),2)
print("Data Analysis")
print(f"No. of testing examples: {training_data.shape[0]}")
print(f"No. of testing examples: {testing_data.shape[0]}")
# .shape[] returns the number of elements in an array i.e. no of datapoints
# print (f"...{}) = print the strings that contain changing fields identified by {}
#print(f"No. of testing examples: {testing_data.shape[0]}")
# print(f"Total : {data.shape[0]}")


# F score measures how accurate a model is using precision and recall
# F score is the harmonic mean of precision and recall

f_score = round(2 * ((precision * recall)/(precision + recall)),2)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F Score: {f_score}")
