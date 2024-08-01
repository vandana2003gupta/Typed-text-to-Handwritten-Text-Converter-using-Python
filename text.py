import numpy as np
import cv2

# Function to generate handwriting style image
def text_to_handwriting(text, save_to):
    # Create a white canvas
    img = np.ones((500, 1000, 3), dtype=np.uint8) * 255

    # Set the font type and scale
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2

    # Starting position for the text
    position = (50, 100)

    # Add text to the image
    cv2.putText(img, text, position, font, font_scale, (0, 0, 0), font_thickness, cv2.LINE_AA)

    # Save the image
    cv2.imwrite(save_to, img)

# Convert text to handwriting
text_to_handwriting(" Hello Everyone! ", "image.png")

# Verify the file creation
from PIL import Image

if os.path.exists("image.png"):
    print("Image created successfully")
    try:
        # Open the image using PIL
        img = Image.open("image.png")
        img.show()
    except IOError:
        print("Cannot open image.png, file might be corrupted.")
else:
    print("Failed to create image")