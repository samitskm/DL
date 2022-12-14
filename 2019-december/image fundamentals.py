import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

path = "C:/Users/Algorithmica/Downloads/digit-recognizer"
np.random.seed(100)

digit_train = pd.read_csv(os.path.join(path, "train.csv"))
print(digit_train.shape)
print(digit_train.info())

X_train = digit_train.iloc[:,1:].values.astype('float32')
train_features_images=X_train.reshape(X_train.shape[0],28,28)
labels = digit_train["label"].values

def show_images(features_images,labels,start, howmany):
    for i in range(start, start+howmany):
        plt.figure(i)
        plt.imshow(features_images[i], cmap=plt.get_cmap('gray'))
        plt.title(labels[i])
    plt.show()
    
show_images(train_features_images, labels, 100, 10)
