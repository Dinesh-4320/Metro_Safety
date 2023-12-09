import requests
import base64
import os

url = "http://192.168.180.172:8000/predict"

# List to store image payloads
image_payloads = []

# Path to the directory containing your images
image_directory = "./images"

# Iterate through each image in the directory
for filename in os.listdir(image_directory):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        # Add path of each image to the list 
        image_path = os.path.join(image_directory, filename)
        image_payloads.append(payload)

files=[]
i=1
for image_path in image_payloads:
    files.append(("files",(f"image/image{i}.jpg",open(image_path,"rb"))))
    i+=1

# Make POST requests 
response = requests.post(url, files=files)
print(response.json())