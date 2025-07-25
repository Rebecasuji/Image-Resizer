# 🖼️ Image Resizer & Format Converter Tool (Batch Processing)

This Python tool resizes and converts all images in a folder using the **Pillow** library. It's ideal for batch image processing where you need consistent dimensions or format conversion.

## 📌 Features

- ✅ Resize all images in a folder to a fixed resolution
- ✅ Convert image formats (e.g., PNG to JPG)
- ✅ Batch process using simple Python script
- ✅ Skips non-image files and nested folders
- ✅ Lightweight, beginner-friendly, and open-source

## 📁 Project Structure

Image-Resizer/
├── image_resizer.py # Main script
├── input_images/ # Place your images here
└── output_images/ # Resized images will be saved here
## ⚙️ Requirements

- Python 3.x
- Pillow (Python Imaging Library)

### Install Pillow:

```bash
pip install pillow
download this repository:

git clone https://github.com/Rebecasuji/Image-Resizer.git
cd Image-Resizer

Create the following folders:
input_images/ — Add all images you want to resize
output_images/ — Output will be saved here

Configuration Options
Inside image_resizer.py:

RESIZE_TO = (800, 600)         # Target resolution
OUTPUT_FORMAT = 'JPEG'         # Format: 'JPEG', 'PNG', 'WEBP', etc.
OUTPUT_EXTENSION = '.jpg'      # File extension
