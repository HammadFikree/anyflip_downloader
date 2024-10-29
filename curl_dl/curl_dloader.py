import os
import requests  # Using requests to download files

# Define the paths relative to the current script location
script_dir = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(script_dir, 'curl_imgs')  # Folder to save images

# Create the folder if it doesn't exist
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Open urls.txt and download each URL in it
with open(os.path.join(script_dir, 'urls.txt'), 'r') as file:
    for idx, url in enumerate(file):
        url = url.strip()
        if url:
            try:
                # Request the image
                response = requests.get(url)
                response.raise_for_status()
                
                # Save the image with an incremental filename
                img_path = os.path.join(image_folder, f'image_{idx + 1}.jpg')
                with open(img_path, 'wb') as img_file:
                    img_file.write(response.content)
                print(f"Downloaded: {img_path}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {url}: {e}")
