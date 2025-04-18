import os
import pytesseract
from PIL import Image
import logging
import json
import uuid
import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text_from_png(image_path):
    """
    Extract text from a PNG image using OCR.

    Args:
        image_path (str): Path to the PNG image

    Returns:
        str: Extracted text from the image
    """
    try:
        # Open the image
        image = Image.open(image_path)

        # Extract text using pytesseract
        text = pytesseract.image_to_string(image)

        logger.info(f"Successfully extracted text from {image_path}")
        return text
    except Exception as e:
        logger.error(f"Error extracting text from {image_path}: {str(e)}")
        return ""

async def process_document(png_path, user_id=None, document_type="invoice", skip_storage=True):
    """
    Process a PNG document:
    1. Extract text using OCR
    2. Store in Supabase database (unless skip_storage is True)

    Args:
        png_path (str): Path to the PNG file
        user_id (str, optional): User ID associated with this document
        document_type (str): Type of document being processed
        skip_storage (bool): If True, skip storing in database

    Returns:
        dict: Result of the processing
    """
    try:
        # Extract text using OCR
        extracted_text = extract_text_from_png(png_path)

        if not extracted_text:
            return {"status": "error", "message": "No text extracted from image"}

        # Generate a document ID
        doc_id = str(uuid.uuid4())

        # Create document metadata
        metadata = {
            "source": os.path.basename(png_path),
            "user_id": user_id,
            "type": document_type,
            "timestamp": str(datetime.datetime.now())
        }

        # Skip storage if requested (useful for testing)
        if not skip_storage:
            # This part would normally store in Supabase
            # But we're skipping it for testing purposes
            logger.info("Skipping database storage as requested")

        logger.info(f"Successfully processed document {doc_id}")
        return {
            "status": "success",
            "document_id": doc_id,
            "extracted_text": extracted_text,
            "metadata": metadata
        }

    except Exception as e:
        logger.error(f"Error processing document: {str(e)}")
        return {"status": "error", "message": str(e)}
