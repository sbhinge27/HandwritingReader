import tensorflow as tf
from preprocess import extract_handwritten_digits
from tensorflow.keras.models import load_model
import numpy as np

# Load the pre-trained model
model = load_model('models/mnist_model.h5')

# Extract handwritten digits from the PDF
digits_images = extract_handwritten_digits('path_to_pdf_file.pdf')

# Preprocess the images for the model
digits_images = np.array(digits_images) / 255.0  # Normalize the images

# Use the model to predict each digit
predictions = model.predict(digits_images)

# Get the most likely predicted digit
predicted_digits = np.argmax(predictions, axis=1)

# Output predictions
print(f"Predicted digits: {predicted_digits}")
