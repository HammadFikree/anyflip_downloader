from PIL import Image
import os

# Define the folders relative to the user's home directory
home_dir = os.path.expanduser('~')
image_folder = os.path.join(home_dir, 'Downloads', 'curl_dl', 'curl_imgs')
output_folder = os.path.join(home_dir, 'Downloads', 'curl_dl')
pdf_output = os.path.join(output_folder, 'combined_images.pdf')

# Check if the image folder exists
if not os.path.exists(image_folder):
    print(f"Image folder not found: {image_folder}")
    exit(1)

# Get list of images sorted by the number in the filename
image_files = sorted(
    [file for file in os.listdir(image_folder) if file.endswith(('.jpg', '.jpeg', '.png'))],
    key=lambda x: int(x.split('_')[1].split('.')[0])  # Extracting the number from 'image_X.jpg'
)

# Load images and convert to PDF
images = []
for file in image_files:
    img_path = os.path.join(image_folder, file)
    image = Image.open(img_path).convert('RGB')
    images.append(image)

# Save as PDF
if images:
    images[0].save(pdf_output, save_all=True, append_images=images[1:])
    print(f"PDF created successfully: {pdf_output}")
else:
    print("No images found to create PDF.")
