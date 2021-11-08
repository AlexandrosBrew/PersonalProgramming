import matplotlib.pyplot as plt
import NeuralNetworkModule as nnm

input_vectors = ([1.5, 4], [3, 5], [8,0.5], [12, 3], [4,6], [.30,1], [9.8, 2], [10, 3.4])
targets = [0 , 2, 3, 0, 3, 4, 6, 8]
learning_rate = 0.1
neuralnet = nnm.NeuralNetwork(learning_rate)
trainingerr = neuralnet.train(input_vectors, targets, 10000)

plt.plot(trainingerr)
plt.xlabel("Iterations")
plt.ylabel("Error for all training instances")
plt.savefig("Cumulative_error.png")