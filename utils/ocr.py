import pytesseract
from PIL import Image
import io

# Path to Tesseract (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_bytes: bytes) -> str:
    """Extract text from an uploaded image using Tesseract OCR."""
    image = Image.open(io.BytesIO(image_bytes))
    return pytesseract.image_to_string(image)
