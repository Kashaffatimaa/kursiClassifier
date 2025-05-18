# Kursi Plastic Object Classifier

## Project Overview
This project implements a simple rule-based plastic object classifier for Kursi's recycling facility. It classifies images of plastic objects into three categories — black, transparent, or colorful — and assigns each to the correct conveyor belt for recycling.

## How to Run
1. Place your plastic object images in the `dataset/black/`, `dataset/transparent/`, or `dataset/colorful/` folders.
2. Run the Python script `kursiClassifier.py`.
3. When prompted, enter the full path to an image file (use forward slashes `/`).
4. The program will output the classification label and conveyor belt assignment.

## Code Structure
- `load_image(path)`: Loads an image from the given path.
- `analyze_image(image)`: Analyzes the image brightness and color to classify it.
- `assign_belt(label)`: Assigns the conveyor belt based on the classification.
- `main()`: The main function to run the classifier interactively.

## Challenges
- Differentiating between transparent and colorful plastics was tricky; used brightness thresholds.
- Ensured simplicity for quick classification using average brightness and color variance.

## Author
Kashaf Fatima