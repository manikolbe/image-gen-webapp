import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Load the pre-trained model
model_path = "./models/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float32)
pipe.to("cpu")  # If you have a compatible GPU, you can change to "cuda"

st.title("AI Image Generator")
st.write("Generate images from text prompts using Stable Diffusion.")

prompt = st.text_input("Enter your prompt:", "A futuristic cityscape at sunset")

if st.button("Generate"):
    with st.spinner("Generating..."):
        # image = pipe(prompt).images[0]
        # st.image(image, caption="Generated Image", use_column_width=True)
        for image in pipe(prompt).images:
            st.image(image, caption="Generated Image", use_column_width=True)
