import cv2
import numpy as np
import os

def load_image(path):
    """Load an image from the given path."""
    image = cv2.imread(path)
    return image

def analyze_image(image):
    """
    Analyze the image to classify it as black, transparent, or colorful.
    
    Rules:
    - Dark image with low brightness and low color mean → 'black'
    - Bright image with low color variance → 'transparent'
    - High color variance → 'colorful'
    """
    # Resize image to speed up processing
    image = cv2.resize(image, (100, 100))

    # Convert to grayscale to get brightness
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    avg_brightness = gray.mean()

    # Average color per channel (B, G, R)
    avg_color = image.mean(axis=0).mean(axis=0)

    # Standard deviation of colors to measure color variation
    color_std = np.std(image)

    # Debug info - you can comment these out after testing
    print(f"Avg Brightness: {avg_brightness:.2f}")
    print(f"Avg Color (BGR): {avg_color}")
    print(f"Color Std Dev: {color_std:.2f}")

    # Classification logic
    if avg_brightness < 70 and np.mean(avg_color) < 70:
        return 'black'
    elif avg_brightness > 180 and color_std < 20:
        return 'transparent'
    elif color_std > 40:
        return 'colorful'
    else:
        # Default fallback
        return 'black'

def assign_belt(label):
    """Assign conveyor belt based on label."""
    if label == 'black':
        return 'Conveyor Belt A'
    elif label == 'transparent':
        return 'Conveyor Belt B'
    elif label == 'colorful':
        return 'Conveyor Belt C'
    else:
        return 'No belt assigned'

def main():
    print("Welcome to Kursi Object Classifier")
    print("Make sure to provide full image path (use forward slashes '/')")

    path = input("Enter full image path: ")

    img = load_image(path)

    if img is None:
        print("Error: Image not found or could not be loaded.")
        return

    label = analyze_image(img)
    belt = assign_belt(label)

    print(f"Label: {label}")
    print(f"Send to: {belt}")

if __name__ == "__main__":
    main()
