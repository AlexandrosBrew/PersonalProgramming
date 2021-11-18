import matplotlib.pyplot as plt
import NeuralNetworkModule as nnm
import random
import numpy as np

rand1 = random.randrange(0, 10)
rand2 = random.randrange(0, 10)

input_vectors = np.array([rand1, rand2]) #!([1.5, 4], [3, 5], [8,0.5], [12, 3], [4,6], [.30,1], [9.8, 2], [10, 3.4])
targets = [0 , 1, 0, 0, 1, 0, 1, 0]
learning_rate = 0.1
neuralnet = nnm.NeuralNetwork(learning_rate)
trainingerr = neuralnet.train(input_vectors, targets, 10000)

file = open("trainingerr.txt", "w")
for i in trainingerr:
    file.write(f'Training error: {str(i)}\n')
file.close()

plt.plot(trainingerr)
plt.xlabel("Iterations")
plt.ylabel("Error for all training instances")
plt.savefig("Cumulative_error.png")