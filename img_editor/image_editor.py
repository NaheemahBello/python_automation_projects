from PIL import Image, ImageFilter, ImageEnhance
import os

images = './image'
edited_images = '/edited_images'

for filename in os.listdir(images):
    img = Image.open(f"{images}/{filename}")
    
    edit = img.filter(ImageFilter.BLUR)
    
    clean_name = os.path.splitext(filename)[0]
    
    edit.save(f".{edited_images}/{clean_name}_edited.jpg")