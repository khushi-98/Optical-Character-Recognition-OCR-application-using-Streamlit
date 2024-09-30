
import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import pytesseract
import torch


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

def extract_text_from_image(image):
 
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    
    
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    additional_text = pytesseract.image_to_string(image, lang='eng+hin')
    
    return {"model_output": generated_text, "tesseract_output": additional_text}


def keyword_search(text, keyword):
    if keyword.lower() in text.lower():
        return f"Keyword found: {keyword}"
    else:
        return f"Keyword '{keyword}' not found in the text."


st.title("OCR and Keyword Search")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg", "bmp", "tiff"])

if uploaded_file is not None:
    
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    result = extract_text_from_image(image)
    model_text = result['model_output']
    tesseract_text = result['tesseract_output']
    
    st.subheader("Extracted Text (Huggingface Model):")
    st.text_area("Model Output", model_text)
    
    st.subheader("Extracted Text (Tesseract):")
    st.text_area("Tesseract Output", tesseract_text)
    
    keyword = st.text_input("Enter a keyword to search within the Tesseract extracted text")
    

    if st.button("Search"):
        search_result = keyword_search(tesseract_text, keyword)  
        st.write(search_result)



