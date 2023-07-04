#Deep Learning is a subfield of Machine Learning that involves training artificial neural networks with multiple layers to make predictions or decisions based on input data.
#Neural Networks are a type of machine learning model that are loosely modeled after the structure of the brain. They consist of layers of interconnected "neurons" that process input data and make predictions.
#Machine Learning is a subfield of artificial intelligence that involves the development of algorithms that can learn from and make predictions or decisions based on data, without being explicitly programmed to do so.
#Artificial Intelligence (AI) refers to the ability of machines to perform tasks that would normally require human intelligence, such as understanding natural language or recognizing patterns in data.
#The weights of a neural network are the parameters that are learned during the training process
#Layers are the building blocks of a neural network. They consist of multiple neurons that process input data and pass output to the next layer. There are several types of layers, including input, output, and hidden layers.
#Backpropagation is an algorithm used to train neural networks. It involves calculating the gradient of the loss function with respect to the weights and biases of the network, and using this gradient to update the parameters iteratively through stochastic gradient descent.
#A loss function—How the network will be able to measure its performance on the training data, and thus how it will be able to steer itself in the right direc- tion.
#An optimizer—The mechanism through which the network will update itself based on the data it sees and its loss function.
#Tensor is a container for data—almost always numerical data. So, it’s a container for numbers.
#A tensor that contains only one number is called a scalar (or scalar tensor, or 0-dimensional tensor, or 0D tensor). In Numpy, a float32 or float64 number is a scalar tensor (or scalar array).
#The number of axes of a tensor is also called its rank
#An array of numbers is called a vector, or 1D tensor. A 1D tensor is said to have exactly one axis.
#An array of vectors is a matrix, or 2D tensor. A matrix has two axes (often referred to rows and columns).
#Shape—This is a tuple of integers that describes how many dimensions the tensor has along each axis.
#Selecting specific elements in a tensor is called tensor slicing.
#The relu operation and addition are element-wise operations: operations that are applied independently to each entry in the tensors being considered.
#Broadcasting consists of two steps: 1 Axes (called broadcast axes) are added to the smaller tensor to match the ndim of the larger tensor. 2 The smaller tensor is repeated alongside these new axes to match the full shape of the larger tensor.
#The tensor dot operation, also known as tensor multiplication or tensor contraction, is a mathematical operation that takes two tensors as inputs and returns a new tensor. It involves multiplying corresponding elements of the two tensors and summing them over one or more axes.
#Tensor reshaping is the process of changing the shape of a tensor without changing its contents. In NumPy, you can reshape a tensor using the reshape() function. The reshape() function takes the tensor as its input and a new shape as a tuple. The new shape specifies the dimensions of the reshaped tensor.)
import numpy as np

# Create a scalar tensor
scalar_tensor = np.array(5)
print("Scalar Tensor:\n", scalar_tensor)

# Create a vector tensor
vector_tensor = np.array([1, 2, 3])
print("\nVector Tensor:\n", vector_tensor)

# Create a matrix tensor
matrix_tensor = np.array([[1, 2], [3, 4]])
print("\nMatrix Tensor:\n", matrix_tensor)

# Create a 3D tensor
tensor_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Tensor:\n", tensor_3d)
print(tensor_3d.shape)

# Create a random tensor (as a NumPy array)
random_tensor = np.random.normal(size=(3, 3))
print("\nRandom Tensor:\n", random_tensor)



import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.dot(a, b)
print(result)




import numpy as np
# Create a 3D tensor
tensor_3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                      [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
# Reshape the tensor to a 2D tensor
tensor_2d = tensor_3d.reshape((2, 12))
# Print the shapes of the tensors
print("Original Tensor Shape:", tensor_3d.shape)
print("Reshaped Tensor Shape:", tensor_2d.shape)