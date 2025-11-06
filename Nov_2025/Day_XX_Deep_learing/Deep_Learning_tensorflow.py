import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import  mnist
from tensorflow.keras.models import Sequential

# 1. Load and prepare the MNIST dataset
# The data is automatically split into training and testing sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values from [0, 255] to [0, 1] for better model performance
x_train, x_test = x_train / 255.0, x_test / 255.0

print(f"Training data shape: {x_train.shape}")
print(f"Test data shape: {x_test.shape}")

# Optional: Visualize a sample image
# plt.imshow(x_train[0], cmap='gray')
# plt.title(f"Label: {y_train[0]}")
# plt.show()

# 2. Build the neural network model using the Sequential API
model = Sequential([
    # Flatten layer converts the 28x28 2D image into a 1D vector of 784 pixels
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    # Dense hidden layer with 128 neurons and ReLU activation
    tf.keras.layers.Dense(128, activation='relu'),
    # Output dense layer with 10 neurons (one for each digit 0-9) and softmax activation
    tf.keras.layers.Dense(10, activation='softmax')
])

# 3. Compile the model
# Adam optimizer is a good default choice, and sparse_categorical_crossentropy
# is used because the labels are integers (0, 1, ..., 9) not one-hot encoded vectors
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 4. Train the model
print("\nStarting model training...")
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# 5. Evaluate the model
print("\nEvaluating model on test data...")
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc*100:.2f}%')

# 6. Make predictions
predictions = model.predict(x_test[:5]) # Predict the first 5 images
predicted_labels = np.argmax(predictions, axis=1)
actual_labels = y_test[:5]

print(f"\nActual labels for first 5 test images: {actual_labels}")
print(f"Predicted labels for first 5 test images: {predicted_labels}")
