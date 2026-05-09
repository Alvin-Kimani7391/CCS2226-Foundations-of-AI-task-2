# mnist_load.py

from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Print dataset shape
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Display first image
plt.imshow(x_train[0], cmap='gray')
plt.title(f"Digit: {y_train[0]}")
plt.show()