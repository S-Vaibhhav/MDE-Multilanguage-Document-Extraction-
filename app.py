### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE API KEY"))

## Function to load Google Gemini Pro Vision API And get response
def get_gemini_repsonse(input, image, prompt):
    model=genai .GenerativeMode1( ' gemini-pro-vision')
    response=model. generate_content ( [input, image [e] , prompt] )
    return response. text


input_prompt='''
You are expert in understanding invoices.
We will upload a image as invoice and you will have to answer any questions based on the uploaded invoce image.'''

# input=st.text_input("lnput Prompt: " ,
uploaded_fi1e=st.fi1e_up10ader("Choose an image of the document: ",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=lmage.open(uploaded_file)
    st.image(image,caption="lJp10aded Image" ,use_column_width=True)
submit=st.button("Te11 me about the document")