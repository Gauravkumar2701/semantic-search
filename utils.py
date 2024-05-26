import re
from pdfminer.high_level import extract_text_to_fp
from io import BytesIO
def extract_text_from_pdf(pdf_file):
    output_string = BytesIO()
    extract_text_to_fp(pdf_file, output_string)
    text = output_string.getvalue().decode()
    return text

def clean_text(text):
    # Remove unwanted characters
    text = re.sub(r'\s+', ' ', text)  
    text = text.strip() 
    # Normalize text
    text = text.lower()
    return text


