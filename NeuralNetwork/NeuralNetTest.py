import matplotlib.pyplot as plt
import NeuralNetworkModule as nnm
import random
import numpy as np

input_vectors = [] #!([1.5, 4], [3, 5], [8,0.5], [12, 3], [4,6], [.30,1], [9.8, 2], [10, 3.4])

for y in range(0, 10):
    rand1 = random.randrange(0, 10)
    rand2 = random.randrange(0, 10)
    input_vectors.append(np.array([rand1, rand2]))

print(*input_vectors)

targets = [0 , 1, 0, 0, 1, 0, 1, 0]
learning_rate = 0.1
neuralnet = nnm.NeuralNetwork(learning_rate)
trainingerr = neuralnet.train(input_vectors, targets, 10000)

file = open("trainingerr.txt", "w")
it = 0
for i in trainingerr:
    file.write(f'Training error {it}: {str(i)}\n')
    it += 1
file.write('---------------------------------')
it = 0
for x in input_vectors:
    file.write(f'Input Vector {it}: {str(x)}\n')
    it += 1
file.close()

plt.plot(trainingerr)
plt.xlabel("Iterations")
plt.ylabel("Error for all training instances")
plt.savefig("Cumulative_error.png")