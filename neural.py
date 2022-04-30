# https://www.freecodecamp.org/news/how-to-build-your-first-neural-network-to-predict-house-prices-with-keras-f8db83049159/
import numpy as np
import pandas
import csv

# STEP 1: Import data
data = pandas.read_csv(r"C:\Users\Esmeralda\github\Python-ML\data.csv")
# convert data to numerical
dNationality = {"UK" : 0, "USA" : 1, "N" : 2}
dGo = {"YES" : 1, "NO" : 0}

data["Nationality"] = data["Nationality"].map(dNationality)
data["Go"] = data["Go"].map(dGo)
dataset = data.values
dataset

# input features = age, experience, rank, nationality

# STEP 2: define features and target
# features = ["Age", "Experience", "Rank", "Nationality"]
# make feature columns "x"
# assign first 4 coloumns in array to variable x (features)
x = dataset[:,0:4] #[: = does not split row, all rows, 0]
# make target column "y"
y = dataset[:,4]

# STEP 3: Preprocessing
# scaler preserves the shape of original distribution
# minmax scaler subtracts the min value in the feature and then divides by the range
# the range is the difference between the original maximum and original minimm
# robust scaler for when dataset has many outliers
# standard scaler for normal distrbution

# min max scaler for transforming features to 0 - 1
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
x_scale = min_max_scaler.fit_transform(x)

x_scale

# STEP 4: Split train_test_validation
from sklearn.model_selection import train_test_split

# training = 70% ; split validation & test = 30% (combined)
x_train, x_val_and_test, y_train, y_val_and_test = train_test_split(x_scale, y, test_size = 0.3)

# split validation & test with each 15% (split of 0.5 from the original 30%)
x_val, x_test, y_val, y_test = train_test_split(x_val_and_test, y_val_and_test, test_size = 0.5)

print("Summary")
print("x_train & y_train : 4 features & 1 target, 70% of full dataset")
print("x_val & y_val: 4 features & 1 target, 15% of full dataset ")
print("x_test & y_test : 4 features & 1 target, 15% of full dataset")

print(x_train.shape, x_val.shape, x_test.shape, y_train.shape, y_val.shape, y_train.shape)
28/40

# ******************************************************************************
                     ### Multilayer Perceptron ###
# Input layer : Size 4
# Hidden Layer 1 : Size 15 (ReLU activation)
# Hidden Layer 2 : Size 15 (ReLu activation)
# Output Layer L : Size 1 (Sigmoid)

# Step 1: Build model
from keras.models import Sequential
from keras.layers import Dense

n = 3
# no of neurons in input layer = no of features
model = Sequential ([  # store model in variable model
        Dense(n, activation = 'relu', input_shape = (4,)), # defining first layer
    #    Dense(n, activation = 'relu'), # defining second layer
        Dense(1, activation = 'sigmoid'), # defining output layer
        ])

model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
# sgd = stochastic gradient descent
 # loss function for outputs = binary crossentropy for output 0 or 1


# Step 2: Train model
hist = model.fit(x_train,y_train,batch_size = n, epochs = 50, validation_data=(x_val, y_val))


#batch size = size of hidden layer, epochs = training iteration
model.evaluate(x_test, y_test)[1] # second element [1] = accuracy
# first element [0] = loss


# plot loss
import matplotlib.pyplot as plt
plt.plot(hist.history['loss']) # plot loss
plt.plot(hist.history['val_loss']) # plot val_loss
plt.title('Model loss') # title
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.show()

# plot accuracy
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='lower right')
plt.show()



# ******************************************************************************
# Optimize for overfitting
from keras.layers import Dropout
from keras import regularizers

n2 = 3
# no of neurons in input layer = no of features
model_2 = Sequential([
    Dense(n2, activation='relu', kernel_regularizer=regularizers.l2(0.01), input_shape=(4,)),
    Dropout(0.3),
    Dense(n2, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(n2, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(1, activation='sigmoid', kernel_regularizer=regularizers.l2(0.01)),
    ])

# kernel regularizer = include squared values of the parameters in overall loss function and weight them by 0.1
model_2.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

hist_2 = model_2.fit(x_train,y_train,batch_size = n, epochs = 50, validation_data=(x_val, y_val))

#batch size = size of hidden layer, epochs = training iteration
model_2.evaluate(x_test, y_test)[1] # second element [1] = accuracy
# first element [0] = loss


# plot loss
import matplotlib.pyplot as plt
plt.plot(hist_2.history['loss']) # plot loss
plt.plot(hist_2.history['val_loss']) # plot val_loss
plt.title('Model loss') # title
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.show()


# plot accuracy
plt.plot(hist_2.history['accuracy'])
plt.plot(hist_2.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='lower right')
plt.show()
