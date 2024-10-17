from diffusers import StableDiffusionPipeline
import torch

# Use your access token
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
pipe.save_pretrained("./models/stable-diffusion-v1-4")
