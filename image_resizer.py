import os
from PIL import Image

# === CONFIGURATION ===
INPUT_FOLDER = 'input_images'
OUTPUT_FOLDER = 'output_images'
RESIZE_TO = (800, 600)  # width x height
OUTPUT_FORMAT = 'JPEG'  # Options: 'JPEG', 'PNG', 'WEBP', etc.
OUTPUT_EXTENSION = '.jpg'  # Extension matching OUTPUT_FORMAT

# === DEBUG INFO ===
print(f"📁 Current Working Directory: {os.getcwd()}")

# === VALIDATE INPUT FOLDER ===
if not os.path.isdir(INPUT_FOLDER):
    print(f"❌ ERROR: '{INPUT_FOLDER}' is not a valid folder.")
    exit(1)

# === ENSURE OUTPUT FOLDER EXISTS ===
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
elif not os.path.isdir(OUTPUT_FOLDER):
    print(f"❌ ERROR: '{OUTPUT_FOLDER}' exists but is not a folder.")
    exit(1)

# === PROCESS EACH FILE ===
for filename in os.listdir(INPUT_FOLDER):
    input_path = os.path.join(INPUT_FOLDER, filename)

    # Skip folders
    if os.path.isdir(input_path):
        print(f"⚠️ Skipped folder: {filename}")
        continue

    # Skip non-image files
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):
        print(f"⚠️ Skipped (Not an image): {filename}")
        continue

    try:
        with Image.open(input_path) as img:
            img_resized = img.resize(RESIZE_TO)
            base_name = os.path.splitext(filename)[0]
            output_filename = f"{base_name}_resized{OUTPUT_EXTENSION}"
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)

            img_resized.convert("RGB").save(output_path, OUTPUT_FORMAT)
            print(f"✅ Processed: {filename} → {output_filename}")

    except Exception as e:
        print(f"❌ Failed to process {filename}: {e}")
