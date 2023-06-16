import torch
from torch import nn # nn contains all the building blocks to build a neural network'
import matplotlib.pyplot as plt

#create parameters

weight = 0.7
bias = 0.3

#create data
start = 0
end = 1
step = 0.02

X = torch.arange(start, end, step).unsqueeze(dim=1)
y = weight * X + bias


#create a train/test set
train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]
len(X_train), len(y_train), len(X_test), len(y_test)


# better visualizing the data
# Visualize, visualize, visualize!

def plot_predictions(train_data=X_train,
                     train_labels=y_train,
                     test_data=X_test,
                     test_labels=y_test,
                     predictions=None):
    """
    Plots training data, test data and compares predictions if not None.
    """
    plt.figure(figsize=(10, 7))
    # Plot training data in blue
    plt.scatter(train_data, train_labels, c="b", label="Training data")
    # Plot test data in green
    plt.scatter(test_data, test_labels, c="g", label="Testing data")

    # check for predictions
    if predictions is not None:
        # plot the predictions if they exist
        plt.scatter(test_data, predictions, c="r", label="Predictions")
    
    # show the legend
    plt.legend(prop={"size": 14})
#print
plot_predictions()

