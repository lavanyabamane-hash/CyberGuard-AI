print("======== OCR FILE LOADED ========")

import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


keywords = [
    "verify your account",
    "login now",
    "password",
    "urgent",
    "click here",
    "security alert",
    "suspended",
    "confirm identity",
    "bank",
    "otp"
]


def analyze_image(image_file):

    print("======== OCR FUNCTION RUNNING ========")

    image = Image.open(image_file)

    text = pytesseract.image_to_string(image)

    text_lower = text.lower()

    detected_keywords = []

    for word in keywords:
        if word in text_lower:
            detected_keywords.append(word)


    if detected_keywords:

        result = {
            "status": "⚠️ Suspicious Image Detected",
            "risk": "HIGH",
            "keywords": detected_keywords,
            "text": text
        }

    else:

        result = {
            "status": "✅ No suspicious content detected",
            "risk": "LOW",
            "keywords": [],
            "text": text
        }


    return result
