# Portable Image Classifier

This is a Python application that allows you to classify images using the VGG16 model from Keras. It provides a graphical user interface (GUI) built with Tkinter for selecting and classifying images.\

Requirements

- Python 3.11
- Tkinter
- PIL (Python Imaging Library)
- NumPy
- TensorFlow
- Keras

# Installation

1. Clone or download the code from the repository.
2. Install the required dependencies mentioned above using pip or any other package manager.

`pip install tkinter pillow numpy tensorflow keras`

## Usage

Run the main.py script to launch the application.
The application window will open, titled "Portable Image Classifier".
Click the "Choose Image" button to select an image for classification. Supported image formats include JPG and PNG.
Once an image is selected, it will be displayed in the GUI.
Click the "Classify Image" button to initiate the classification process.
The application will use the VGG16 model to classify the image into different classes.
The top image class predictions and their confidences will be displayed in a table format below the image.

## Notes

- The application resizes the selected image to 150 pixels width while maintaining the aspect ratio for display purposes.
- The VGG16 model is pretrained on the ImageNet dataset and provides accurate image classification.
- The application supports both single and multiple predictions for the image classes.

Please ensure that you have the necessary dependencies installed before running the application.

Feel free to explore and modify the code to suit your requirements.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

For any questions or support, please contact volcanbozkurt@gmail.com

Hope this helps! Let me know if you have any further questions.
