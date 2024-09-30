# Optical-Character-Recognition-OCR-application-using-Streamlit


This code implements an Optical Character Recognition (OCR) application using Streamlit. It allows users to upload images and extracts text using two methods: Hugging Face's TrOCR model and Tesseract OCR. Here’s a concise overview of its components:

1. **Libraries Imported**:
   - **Streamlit**: For building the web interface.
   - **Transformers**: For loading the TrOCR model for text extraction.
   - **Pillow**: For image processing.
   - **Pytesseract**: For OCR capabilities.
   - **PyTorch**: For tensor computations.

2. **Tesseract Configuration**:
   - Sets the path to the Tesseract executable for proper functioning.

3. **Model Loading**:
   - Loads the TrOCR processor and model (`microsoft/trocr-base-handwritten`) from Hugging Face.

4. **Functions**:
   - **`extract_text_from_image(image)`**: 
     - Converts the image to RGB, preprocesses it, and generates text predictions from both TrOCR and Tesseract, returning a dictionary of results.
   - **`keyword_search(text, keyword)`**: 
     - Searches for a specified keyword in the Tesseract output and returns a message indicating its presence.

5. **Streamlit Interface**:
   - **File Uploader**: Allows users to upload images (JPG, PNG, etc.).
   - **Image Display**: Shows the uploaded image.
   - **Text Extraction**: Displays extracted text from both models.
   - **Keyword Search Input**: Users can input a keyword to search in the Tesseract output.
   - **Search Functionality**: Returns a message about the keyword's presence in the extracted text.

Overall, this application efficiently extracts text from images and enables keyword searches within the extracted content.
