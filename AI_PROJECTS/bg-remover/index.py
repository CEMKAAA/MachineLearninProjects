import cv2
import numpy as np
import tensorflow as tf

def load_model():
    model = tf.keras.applications.DenseNet201(weights='imagenet')
    return model

def preprocess_image(image_path):
    # Load and preprocess the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))  # Resize for the model input size
    image = tf.keras.applications.densenet.preprocess_input(image)
    return np.expand_dims(image, axis=0)


def remove_background(image_path, model):
    image = preprocess_image(image_path)
    
    # Make predictions using the pre-trained model
    predictions = model.predict(image)
    
    # Get the mask where the object is present
    mask = predictions.argmax(axis=-1)
    
    # Create a binary mask with 1s where the object is present
    binary_mask = np.where(mask == 15, 1, 0)  # Assuming class 15 corresponds to the object of interest
    
    # Apply the binary mask to the original image to remove the background
    result = image[0] * binary_mask[:, :, np.newaxis]
    
    return result.astype(np.uint8)


def main():
    image_path = r'C:\Users\Cem\Downloads\minus.png'
    model = load_model()
    result = remove_background(image_path, model)

    # Display the original and processed images
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Background Removed', cv2.cvtColor(result, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
