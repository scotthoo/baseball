from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow import keras

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt


column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD',
                'TAX', 'PTRATIO', 'B', 'LSTAT']


boston_housing = keras.datasets.boston_housing

#this loads in the pre-supported boston housing data. 
#you can optionally pass this .load_data() function a path for where to cache the dataset locally
#you can select which fraction of the data to reserve as test set
#you can also provide a random seed for shuffling the data before computing the test split
#it returns a tuple of numpy arrays as is below

(train_data, train_labels), (test_data, test_labels) = boston_housing.load_data()

# Shuffle the training set
#argsort takes an array to sort, and if you want, the sorting algorithm to use
order = np.argsort(np.random.random(train_labels.shape))
train_data = train_data[order]
train_labels = train_labels[order]

#print("Training set: {}".format(train_data.shape))  # 404 examples, 13 features
#print("Testing set:  {}".format(test_data.shape))   # 102 examples, 13 features

#print(train_data[0])  # Display sample features, notice the different scales

df = pd.DataFrame(train_data, columns=column_names)
df.head()

#print(train_labels[0:10])  # Display first 10 entries

# Test data is *not* used when calculating the mean and std

#argument is Axis or axes along which the means are computed. The default is to compute the mean of the flattened array.
mean = train_data.mean(axis=0)
std = train_data.std(axis=0)
train_data = (train_data - mean) / std
test_data = (test_data - mean) / std

# #print(train_data[0])  # First training sample, normalized

def build_model():
  model = keras.Sequential([
    keras.layers.Dense(64, activation=tf.nn.relu,
                       input_shape=(train_data.shape[1],)),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(1)
  ])

  optimizer = tf.train.RMSPropOptimizer(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae'])
  return model

model = build_model()
model.summary()



#A callback is a set of functions to be applied at given stages of the training procedure. 
#You can use callbacks to get a view on internal states and statistics of the model during training. 
#You can pass a list of callbacks (as the keyword argument callbacks) to the .fit() method 
#of the Sequential or  Model classes. 
#The relevant methods of the callbacks will then be called at each stage of the training.

# Display training progress by printing a single dot for each completed epoch
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 500

# Store training stats
history = model.fit(train_data, train_labels, epochs=EPOCHS,
                    validation_split=0.2, verbose=0,
                    callbacks=[PrintDot()])


def plot_history(history):
  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [1000$]')
  plt.plot(history.epoch, np.array(history.history['mean_absolute_error']),
           label='Train Loss')
  plt.plot(history.epoch, np.array(history.history['val_mean_absolute_error']),
           label = 'Val loss')
  plt.legend()
  plt.ylim([0, 5])

plot_history(history)

plt.show()


model = build_model()

# The patience parameter is the amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)

history = model.fit(train_data, train_labels, epochs=EPOCHS,
                    validation_split=0.2, verbose=0,
                    callbacks=[early_stop, PrintDot()])

#plot_history(history)

#plt.show()


[loss, mae] = model.evaluate(test_data, test_labels, verbose=0)

print("Testing set Mean Abs Error: ${:7.2f}".format(mae * 1000))

test_predictions = model.predict(test_data).flatten()

# plt.scatter(test_labels, test_predictions)
# plt.xlabel('True Values [1000$]')
# plt.ylabel('Predictions [1000$]')
# plt.axis('equal')
# plt.xlim(plt.xlim())
# plt.ylim(plt.ylim())
# _ = plt.plot([-100, 100], [-100, 100])

#plt.show()


error = test_predictions - test_labels
plt.hist(error, bins = 50)
plt.xlabel("Prediction Error [1000$]")
_ = plt.ylabel("Count")

#plt.show()