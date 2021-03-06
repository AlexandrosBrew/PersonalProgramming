import numpy as np
import matplotlib.pyplot as plt
import random

class NeuralNetwork:
    def __init__(self, learning_rate):
        self.weights = np.array([np.random.randn(), np.random.randn()])
        self.bias = np.random.randn()
        self.learning_rate = learning_rate

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _sigmoid_deriv(self, x):
        return self._sigmoid(x) * (1 - self._sigmoid(x))

    def predict(self, input_vector):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self._sigmoid(layer_1)
        prediction = layer_2
        return prediction

    def _compute_gradients(self, input_vector, target):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self._sigmoid(layer_1)
        prediction = layer_2

        derror_dprediction = 2 * (prediction - target)
        dprediction_dlayer1 = self._sigmoid_deriv(layer_1)
        dlayer1_dbias = 1
        dlayer1_dweights = (0 * self.weights) + (1 * input_vector)

        derror_dbias = (
            derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
        )
        derror_dweights = (
            derror_dprediction * dprediction_dlayer1 * dlayer1_dweights
        )

        return derror_dbias, derror_dweights

    def _update_parameters(self, derror_dbias, derror_dweights):
        self.bias = self.bias - (derror_dbias * self.learning_rate)
        self.weights = self.weights - (
            derror_dweights * self.learning_rate
        )

    def train(self, input_vectors, targets, iterations):
            cumulative_errors = []
            for current_iteration in range(iterations):
                # Pick a data instance at random
                random_data_index = np.random.randint(len(input_vectors))

                input_vector = input_vectors[random_data_index]
                target = targets[random_data_index]

                # Compute the gradients and update the weights
                derror_dbias, derror_dweights = self._compute_gradients(
                    input_vector, target
                )

                self._update_parameters(derror_dbias, derror_dweights)

                # Measure the cumulative error for all the instances
                if current_iteration % 100 == 0:
                    cumulative_error = 0
                    # Loop through all the instances to measure the error
                    for data_instance_index in range(len(input_vectors)):
                        data_point = input_vectors[data_instance_index]
                        target = targets[data_instance_index]

                        prediction = self.predict(data_point)
                        error = np.square(prediction - target)

                        cumulative_error = cumulative_error + error
                    cumulative_errors.append(cumulative_error)

            return cumulative_errors

def main():
    input_vectors = [] #!([1.5, 4], [3, 5], [8,0.5], [12, 3], [4,6], [.30,1], [9.8, 2], [10, 3.4])

    for y in range(0, 10):
        rand1 = random.randrange(0, 10)
        rand2 = random.randrange(0, 10)
        input_vectors.append(np.array([rand1, rand2]))
    targets = [0 , 1, 0, 0, 1, 0, 1, 0]
    learning_rate = 0.1
    neuralnet = NeuralNetwork(learning_rate)
    trainingerr = neuralnet.train(input_vectors, targets, 100000)

    plt.plot(trainingerr)
    plt.xlabel("Iterations")
    plt.ylabel("Error for all training instances")
    plt.savefig("Cumulative_error.png")

if __name__ == "__main__":
    main()
