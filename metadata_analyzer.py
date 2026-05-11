import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(file_path):
    try:
        metadata = {}
        # Open the image file
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata[tag_name] = value
        return metadata
    except Exception as e:
        print(f"Error reading metadata: {e}")
        return None

def main():
    print("Metadata Analyzer\n")
    file_path = input("Enter the path to the image file: ")
    if not os.path.exists(file_path):
        print("File not found. Please try again.")
        return

    metadata = extract_metadata(file_path)
    if metadata:
        print("\nExtracted Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print("No metadata found or failed to extract metadata.")

if __name__ == "__main__":
    main()