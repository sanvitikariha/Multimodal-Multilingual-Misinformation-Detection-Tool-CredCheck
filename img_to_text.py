from PIL import Image
import pytesseract
import os
import platform

# Dynamically set the path to the Tesseract executable
if platform.system() == "Windows":
    TESSERACT_CMD = os.getenv("TESSERACT_CMD", r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
else:
    # For Linux and macOS, assume tesseract is in the PATH
    pytesseract.pytesseract.tesseract_cmd = "tesseract"

def extract_text_from_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Extract text from image
        extracted_text = pytesseract.image_to_string(img)
        
        return extracted_text.strip()
    except Exception as e:
        return f"Error: {e}"
