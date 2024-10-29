# Only for Windows 11
(might be compatible with other windows versions)

__Required `pip install`s:__
- os
- requests
- PIL

__Steps:__
1. Go To Anyflip URL > Fullscreen Mode.
2. Three Dots (Top Right Corner) > More Tools > Dev Tools > Img.
3. Reload Page & wait to load Anyflip, then hold down right-array to flip through all pages (You will see all the imgs fill Dev Tools Img tab).
4. Right-click one img > Copy > Copy all listed URLs.
5. Paste all listed URLs in urls.txt, then only keep the numbered image urls.
6. Save and run curl_dloader.py (to generate all images in curl_imgs).
7. Run imgs_to_pdf.py (to generate full pdf from images in curl_imgs).
8. You will get the pdf as combined_images.pdf in curl_dl and you're done.
9. Don't forget to clear URLS in urls.txt, delete all images in curl_imgs, and Empty Recycle Bin.
