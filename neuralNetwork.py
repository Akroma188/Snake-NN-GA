import numpy as np
from scipy.stats import truncnorm


# make neural network with bias and 2 hidden layers
# use sigmoid as activation funtion
@np.vectorize
def activation_function(x):
    return 1 / (1 + np.e ** -x)

def truncated_normal(mean, sd, low, upp):
    return truncnorm((low - mean)/sd, (upp - mean)/sd, mean, sd)

class NeuralNetwork:
    def __init__(self, num_input, num_first_hidden, num_sec_hidden, num_output):
        self.num_input = num_input
        self.num_first_hidden = num_first_hidden
        self.num_sec_hidden = num_sec_hidden
        self.num_output = num_output
        self.bias = 1

    def create_weight_matrices(self):
        # generate random distribution for weights between input and 1st hidden layer
        rad = 1 / np.sqrt(self.num_input + self.bias)
        X = truncated_normal(0, 1, -rad, rad)
        self.wih = np.round(X.rvs((self.num_first_hidden, self.num_input + self.bias)), 4)

        # generate random distribution for weights between 1st hidden layer and 2nd hidden layer
        rad = 1 / np.sqrt(self.num_first_hidden + self.bias)
        X = truncated_normal(0, 1, -rad, rad)
        self.whh = np.round(X.rvs((self.num_sec_hidden, self.num_first_hidden + self.bias)), 4)

        # generate random distribution for weights between 2nd hidden layer and output layer
        rad = 1 / np.sqrt(self.num_sec_hidden + self.bias)
        X = truncated_normal(0, 1, -rad, rad) 
        self.who = np.round(X.rvs((self.num_output, self.num_sec_hidden + self.bias)), 4)

    def output(self, input):
        input = np.concatenate((input, [1])) # add bias node
        input = np.array(input, ndmin=2).T

        first_h_layer_node_values = np.dot(self.wih, input)
        first_h_layer_node_values = activation_function(first_h_layer_node_values)
        first_h_layer_node_values = np.concatenate((first_h_layer_node_values, [[1]])) # add bias node

        sec_h_layer_node_values = np.dot(self.whh, first_h_layer_node_values)
        sec_h_layer_node_values = activation_function(sec_h_layer_node_values)
        sec_h_layer_node_values = np.concatenate((sec_h_layer_node_values, [[1]]))

        output = np.dot(self.who, sec_h_layer_node_values)

        return list(output)



# neural = NeuralNetwork(2,4,4,4)
# neural.create_weight_matrices()
# print('output: \n', neural.output([20,10]))

# print('wih: \n', neural.wih)
# [r, c] = neural.wih.shape

# print(neural.wih * 50 + neural.wih *20)
