import os
import requests

# Directory where images will be saved
download_folder = "curl_imgs"
os.makedirs(download_folder, exist_ok=True)

# Read URLs from the text file
with open("urls.txt", "r") as file:
    urls = [line.strip() for line in file if line.strip().startswith("https://")]

# Download each image
for count, url in enumerate(urls, start=1):
    try:
        # Request the image
        response = requests.get(url, headers={
            "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.9",
            "cookie": "G_ENABLED_IDPS=google",
            "priority": "i",
            "referer": "https://online.anyflip.com/vjcbu/nfmh/mobile/index.html",
            "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-fetch-dest": "image",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36"
        })

        # Check if the request was successful
        if response.status_code == 200:
            file_path = os.path.join(download_folder, f"image_{count}.jpg")
            with open(file_path, "wb") as img_file:
                img_file.write(response.content)
            print(f"Downloaded: {file_path}")
        else:
            print(f"Failed to download {url} - Status code: {response.status_code}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

print("Download complete.")
